# from fastapi import FastAPI, Depends, HTTPException
# from fastapi.middleware.cors import CORSMiddleware
# from sqlalchemy.orm import Session
# from database import Base, engine, SessionLocal
# from models import Message, Project
# from schemas import MessageCreate, ProjectCreate
# from config import SMTP_EMAIL, SMTP_PASSWORD, SMTP_SERVER, SMTP_PORT
# from auth import authenticate_admin
# import smtplib
# from email.mime.text import MIMEText

# app = FastAPI()

# @app.get("/")
# def root():
#     return {"message": "Welcome to Opnex Portfolio API"}

# # Create tables
# Base.metadata.create_all(bind=engine)

# # CORS
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # DB dependency
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# # Email function
# def send_email(subject, body):
#     msg = MIMEText(body)
#     msg["Subject"] = subject
#     msg["From"] = SMTP_EMAIL
#     msg["To"] = SMTP_EMAIL
#     with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
#         server.starttls()
#         server.login(SMTP_EMAIL, SMTP_PASSWORD)
#         server.sendmail(SMTP_EMAIL, SMTP_EMAIL, msg.as_string())

# # ========== EXISTING CONTACT ENDPOINT ==========
# @app.post("/contact")
# def receive_message(data: MessageCreate, db: Session = Depends(get_db)):
#     new_msg = Message(
#         name=data.name,
#         email=data.email,
#         phone=data.phone,
#         message=data.message
#     )
#     db.add(new_msg)
#     db.commit()
    
#     email_body = f"""
#     New Portfolio Contact Message:
#     Name: {data.name}
#     Email: {data.email}
#     Phone: {data.phone}
#     Message: {data.message}
#     """
#     send_email("New Portfolio Message", email_body)
    
#     return {"success": True, "message": "Message delivered successfully!"}


# # ========== SIMPLE ADMIN LOGIN TEST ==========
# @app.post("/admin/login")
# def admin_login(credentials: dict):
#     correct_username = "opnex"
#     correct_password = "opnex123"
    
#     if (credentials.get("username") == correct_username and 
#         credentials.get("password") == correct_password):
#         return {"success": True, "message": "Login successful"}
#     else:
#         raise HTTPException(status_code=401, detail="Invalid credentials")

# # ========== PUBLIC PROJECTS ENDPOINT ==========
# @app.get("/projects")
# def get_projects(db: Session = Depends(get_db)):
#     projects = db.query(Project).all()
#     return projects

# # ========== ADMIN: CREATE PROJECT ==========
# @app.post("/admin/projects")
# def create_project(project: ProjectCreate, db: Session = Depends(get_db), username: str = Depends(authenticate_admin)):
#     db_project = Project(**project.dict())
#     db.add(db_project)
#     db.commit()
#     return {"message": "Project created"}

# # ========== ADMIN: DELETE PROJECT ==========
# @app.delete("/admin/projects/{project_id}")
# def delete_project(project_id: int, db: Session = Depends(get_db), username: str = Depends(authenticate_admin)):
#     db_project = db.query(Project).filter(Project.id == project_id).first()
#     if not db_project:
#         raise HTTPException(status_code=404, detail="Project not found")
#     db.delete(db_project)
#     db.commit()
#     return {"message": "Project deleted"}

# # ========== ADMIN: GET MESSAGES ==========
# @app.get("/admin/messages")
# def get_messages(db: Session = Depends(get_db), username: str = Depends(authenticate_admin)):
#     messages = db.query(Message).order_by(Message.created_at.desc()).all()
#     return messages

# # ========== ADMIN: DELETE MESSAGE ==========
# @app.delete("/admin/messages/{message_id}")
# def delete_message(message_id: int, db: Session = Depends(get_db), username: str = Depends(authenticate_admin)):
#     db_message = db.query(Message).filter(Message.id == message_id).first()
#     if not db_message:
#         raise HTTPException(status_code=404, detail="Message not found")
#     db.delete(db_message)
#     db.commit()
#     return {"message": "Message deleted"}










































































#railway

# from fastapi import FastAPI, Depends, HTTPException
# from fastapi.middleware.cors import CORSMiddleware
# from fastapi.responses import JSONResponse  # Add this import
# from sqlalchemy.orm import Session
# from database import Base, engine, SessionLocal
# from models import Message, Project
# from schemas import MessageCreate, ProjectCreate
# from config import SMTP_EMAIL, SMTP_PASSWORD, SMTP_SERVER, SMTP_PORT
# from auth import authenticate_admin
# import smtplib
# from email.mime.text import MIMEText
# import os  # Make sure this is imported

# app = FastAPI()

# # =========================
# #    SIMPLIFIED CORS SETTINGS
# # =========================
# origins = [
#     "http://localhost:5173",
#     "http://localhost:5174", 
#     "http://localhost:3000",
#     "http://127.0.0.1:5173",
#     "https://opnex-portfolio.up.railway.app"
# ]

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # Remove this problematic OPTIONS handler - FastAPI CORS middleware handles it automatically
# # @app.options("/{rest_of_path:path}")
# # async def preflight_handler(rest_of_path: str):
# #     return JSONResponse(status_code=200)

# @app.get("/health")
# async def health_check():
#     return {"status": "healthy", "cors": "enabled"}

# # =========================
# #      DATABASE SETUP
# # =========================
# Base.metadata.create_all(bind=engine)

# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# # =========================
# #      EMAIL SENDER
# # =========================
# def send_email(subject, body):
#     try:
#         msg = MIMEText(body)
#         msg["Subject"] = subject
#         msg["From"] = SMTP_EMAIL
#         msg["To"] = SMTP_EMAIL
#         with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
#             server.starttls()
#             server.login(SMTP_EMAIL, SMTP_PASSWORD)
#             server.sendmail(SMTP_EMAIL, SMTP_EMAIL, msg.as_string())
#         return True
#     except Exception as e:
#         print(f"Email error: {e}")
#         return False

# # =========================
# #       ROOT ROUTE
# # =========================
# @app.get("/")
# def root():
#     return {"message": "Welcome to Opnex Portfolio API"}

# # =========================
# #       CONTACT FORM
# # =========================
# @app.post("/contact")
# async def receive_message(data: MessageCreate, db: Session = Depends(get_db)):
#     try:
#         new_msg = Message(
#             name=data.name,
#             email=data.email,
#             phone=data.phone,
#             message=data.message,
#         )
#         db.add(new_msg)
#         db.commit()

#         email_body = f"""
# New Portfolio Contact Message:
# Name: {data.name}
# Email: {data.email}
# Phone: {data.phone}
# Message: {data.message}
# """
#         email_sent = send_email("New Portfolio Message", email_body)
        
#         return {
#             "success": True, 
#             "message": "Message delivered successfully",
#             "email_sent": email_sent
#         }
#     except Exception as e:
#         db.rollback()
#         raise HTTPException(status_code=500, detail=f"Server error: {str(e)}")

# # =========================
# #       ADMIN LOGIN
# # =========================
# @app.post("/admin/login")
# def admin_login(credentials: dict):
#     if credentials.get("username") == "opnex" and credentials.get("password") == "opnex123":
#         return {"success": True, "message": "Login successful"}
#     raise HTTPException(status_code=401, detail="Invalid credentials")

# # =========================
# #      PUBLIC PROJECTS
# # =========================
# @app.get("/projects")
# def get_projects(db: Session = Depends(get_db)):
#     return db.query(Project).all()

# # =========================
# #   ADMIN: CREATE PROJECT
# # =========================
# @app.post("/admin/projects")
# def create_project(
#     project: ProjectCreate,
#     db: Session = Depends(get_db),
#     username: str = Depends(authenticate_admin)
# ):
#     db_project = Project(**project.dict())
#     db.add(db_project)
#     db.commit()
#     return {"message": "Project created"}

# # =========================
# #   ADMIN: DELETE PROJECT
# # =========================
# @app.delete("/admin/projects/{project_id}")
# def delete_project(
#     project_id: int,
#     db: Session = Depends(get_db),
#     username: str = Depends(authenticate_admin)
# ):
#     db_project = db.query(Project).filter(Project.id == project_id).first()
#     if not db_project:
#         raise HTTPException(status_code=404, detail="Project not found")
#     db.delete(db_project)
#     db.commit()
#     return {"message": "Project deleted"}

# # =========================
# #   ADMIN: VIEW MESSAGES
# # =========================
# @app.get("/admin/messages")
# def get_messages(
#     db: Session = Depends(get_db),
#     username: str = Depends(authenticate_admin)
# ):
#     return db.query(Message).order_by(Message.created_at.desc()).all()

# # =========================
# #   ADMIN: DELETE MESSAGE
# # =========================
# @app.delete("/admin/messages/{message_id}")
# def delete_message(
#     message_id: int,
#     db: Session = Depends(get_db),
#     username: str = Depends(authenticate_admin)
# ):
#     db_message = db.query(Message).filter(Message.id == message_id).first()
#     if not db_message:
#         raise HTTPException(status_code=404, detail="Message not found")
#     db.delete(db_message)
#     db.commit()
#     return {"message": "Message deleted"}

# # Add startup event at the end to avoid import issues
# @app.on_event("startup")
# async def startup_event():
#     port = os.getenv("PORT", "8000")
#     print(f"🚀 Server starting on port {port}")









from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from database import Base, engine, SessionLocal
from models import Message, Project
from schemas import MessageCreate, ProjectCreate
from config import SMTP_EMAIL, SMTP_PASSWORD, SMTP_SERVER, SMTP_PORT
from auth import authenticate_admin
import smtplib
from email.mime.text import MIMEText
import os

app = FastAPI()

# =========================
#        CORS SETTINGS
# =========================
origins = [
    "http://localhost:5173",
    "http://localhost:5174",
    "http://localhost:3000", 
    "http://127.0.0.1:5173",
    "https://opnex-portfolio.up.railway.app",
    "https://your-frontend.onrender.com"  # Add your Render frontend URL when you deploy it
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# =========================
#      DATABASE SETUP
# =========================
Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# =========================
#      EMAIL SENDER
# =========================
def send_email(subject, body):
    try:
        msg = MIMEText(body)
        msg["Subject"] = subject
        msg["From"] = SMTP_EMAIL
        msg["To"] = SMTP_EMAIL
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SMTP_EMAIL, SMTP_PASSWORD)
            server.sendmail(SMTP_EMAIL, SMTP_EMAIL, msg.as_string())
        return True
    except Exception as e:
        print(f"Email error: {e}")
        return False

# =========================
#       ROOT ROUTE
# =========================
@app.get("/")
def root():
    return {"message": "Welcome to Opnex Portfolio API"}

# =========================
#       HEALTH CHECK
# =========================
@app.get("/health")
def health_check():
    return {"status": "healthy", "cors": "enabled"}

# =========================
#       CONTACT FORM
# =========================
@app.post("/contact")
def receive_message(data: MessageCreate, db: Session = Depends(get_db)):
    try:
        new_msg = Message(
            name=data.name,
            email=data.email,
            phone=data.phone,
            message=data.message,
        )
        db.add(new_msg)
        db.commit()

        email_body = f"""
New Portfolio Contact Message:
Name: {data.name}
Email: {data.email}
Phone: {data.phone}
Message: {data.message}
"""
        email_sent = send_email("New Portfolio Message", email_body)
        
        return {
            "success": True, 
            "message": "Message delivered successfully",
            "email_sent": email_sent
        }
    except Exception as e:
        db.rollback()
        return JSONResponse(
            status_code=500,
            content={"success": False, "message": f"Server error: {str(e)}"}
        )

# =========================
#       ADMIN LOGIN
# =========================
@app.post("/admin/login")
def admin_login(credentials: dict):
    if credentials.get("username") == "opnex" and credentials.get("password") == "opnex123":
        return {"success": True, "message": "Login successful"}
    raise HTTPException(status_code=401, detail="Invalid credentials")

# =========================
#      PUBLIC PROJECTS
# =========================
@app.get("/projects")
def get_projects(db: Session = Depends(get_db)):
    return db.query(Project).all()

# =========================
#   ADMIN: CREATE PROJECT
# =========================
@app.post("/admin/projects")
def create_project(
    project: ProjectCreate,
    db: Session = Depends(get_db),
    username: str = Depends(authenticate_admin)
):
    db_project = Project(**project.dict())
    db.add(db_project)
    db.commit()
    return {"message": "Project created"}

# =========================
#   ADMIN: DELETE PROJECT
# =========================
@app.delete("/admin/projects/{project_id}")
def delete_project(
    project_id: int,
    db: Session = Depends(get_db),
    username: str = Depends(authenticate_admin)
):
    db_project = db.query(Project).filter(Project.id == project_id).first()
    if not db_project:
        raise HTTPException(status_code=404, detail="Project not found")
    db.delete(db_project)
    db.commit()
    return {"message": "Project deleted"}

# =========================
#   ADMIN: VIEW MESSAGES
# =========================
@app.get("/admin/messages")
def get_messages(
    db: Session = Depends(get_db),
    username: str = Depends(authenticate_admin)
):
    return db.query(Message).order_by(Message.created_at.desc()).all()

# =========================
#   ADMIN: DELETE MESSAGE
# =========================
@app.delete("/admin/messages/{message_id}")
def delete_message(
    message_id: int,
    db: Session = Depends(get_db),
    username: str = Depends(authenticate_admin)
):
    db_message = db.query(Message).filter(Message.id == message_id).first()
    if not db_message:
        raise HTTPException(status_code=404, detail="Message not found")
    db.delete(db_message)
    db.commit()
    return {"message": "Message deleted"}

# Startup event
@app.on_event("startup")
async def startup_event():
    port = os.getenv("PORT", "8000")
    print(f"🚀 Server starting on port {port}")