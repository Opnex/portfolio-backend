# DB_NAME = "first_portfolio_db"
# DB_USER = "root"
# DB_PASSWORD = "Thomasope123"
# DB_HOST = "127.0.0.1"

# # Your email settings
# SMTP_EMAIL = "thomasopeyemi1@gmail.com"
# SMTP_PASSWORD = "jnlwgpnipymvanif"
# SMTP_SERVER = "smtp.gmail.com"
# SMTP_PORT = 587

# ADMIN_USERNAME = "opnex"
# ADMIN_PASSWORD = "opnex123"






import os
from dotenv import load_dotenv

load_dotenv()

DB_NAME = os.getenv("MYSQL_DATABASE")
DB_USER = os.getenv("MYSQL_USER")
DB_PASSWORD = os.getenv("MYSQL_PASSWORD")
DB_HOST = os.getenv("MYSQL_HOST")
DB_PORT = os.getenv("MYSQL_PORT")

SMTP_EMAIL = os.getenv("SMTP_EMAIL")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")
SMTP_SERVER = os.getenv("SMTP_SERVER", "smtp.gmail.com")
SMTP_PORT = int(os.getenv("SMTP_PORT", 587))
