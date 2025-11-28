# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker, declarative_base
# from config import DB_HOST, DB_NAME, DB_USER, DB_PASSWORD

# DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"

# engine = create_engine(DATABASE_URL)

# SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

# Base = declarative_base()



#railway

# import os
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker, declarative_base
# from config import DB_USER, DB_PASSWORD, DB_HOST, DB_NAME, DB_PORT

# # Use DATABASE_URL env var if it exists (Railway), otherwise fallback to local config
# DATABASE_URL = os.getenv("DATABASE_URL")

# if DATABASE_URL:
#     engine = create_engine(DATABASE_URL, future=True)
# else:
#     engine = create_engine(
#         f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}",
#         future=True
#     )

# SessionLocal = sessionmaker(
#     bind=engine,
#     autocommit=False,
#     autoflush=False
# )

# Base = declarative_base()








import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Use DATABASE_URL env var if it exists (Render), otherwise fallback to local config
DATABASE_URL = os.getenv("DATABASE_URL")

# Fix for Render - sometimes DATABASE_URL starts with postgres:// instead of postgresql://
if DATABASE_URL and DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

if DATABASE_URL:
    engine = create_engine(DATABASE_URL, future=True)
else:
    from config import DB_USER, DB_PASSWORD, DB_HOST, DB_NAME, DB_PORT
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