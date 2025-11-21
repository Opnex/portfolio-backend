# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker, declarative_base
# from config import DB_HOST, DB_NAME, DB_USER, DB_PASSWORD

# DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"

# engine = create_engine(DATABASE_URL)

# SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

# Base = declarative_base()





# # database.py

# import os
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker, declarative_base
# from config import DB_HOST, DB_NAME, DB_USER, DB_PASSWORD, DB_PORT

# # Prefer DATABASE_URL env var (Railway/Render will provide this)
# DATABASE_URL = os.getenv("DATABASE_URL") or \
#     f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# engine = create_engine(DATABASE_URL, future=True)

# SessionLocal = sessionmaker(
#     bind=engine,
#     autocommit=False,
#     autoflush=False
# )

# Base = declarative_base()








from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from config import DATABASE_URL, DB_USER, DB_PASSWORD, DB_HOST, DB_NAME, DB_PORT

# Use DATABASE_URL if set (Railway), otherwise fallback to local config
if DATABASE_URL:
    engine = create_engine(DATABASE_URL, future=True)
else:
    engine = create_engine(
        f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}",
        future=True
    )

SessionLocal = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False
)

Base = declarative_base()

