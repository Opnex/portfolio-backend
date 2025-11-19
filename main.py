from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from database import Base, engine, SessionLocal
from models import Message
from schemas import MessageCreate
from config import SMTP_EMAIL, SMTP_PASSWORD, SMTP_SERVER, SMTP_PORT
import smtplib
from email.mime.text import MIMEText

app = FastAPI()

@app.get("/")
def root():
    return {
        "message": "Welcome to Opnex Portfolio API",
    }


# Create tables
Base.metadata.create_all(bind=engine)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# DB dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Email function
def send_email(subject, body):
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = SMTP_EMAIL
    msg["To"] = SMTP_EMAIL

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(SMTP_EMAIL, SMTP_PASSWORD)
        server.sendmail(SMTP_EMAIL, SMTP_EMAIL, msg.as_string())


@app.post("/contact")
def receive_message(data: MessageCreate, db: Session = Depends(get_db)):
    # save to DB
    new_msg = Message(
        name=data.name,
        email=data.email,
        phone=data.phone,
        message=data.message
    )
    db.add(new_msg)
    db.commit()
    db.refresh(new_msg)

    # send email to you
    email_body = f"""
New Portfolio Contact Message:

Name: {data.name}
Email: {data.email}
Phone: {data.phone}
Message:
{data.message}
    """

    send_email("New Portfolio Message", email_body)

    return {"success": True, "message": "Message delivered successfully!"}
