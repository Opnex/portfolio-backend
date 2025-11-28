            # MYSQL CODE

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


                    # POSTGRES CODE

# # config.py
# DB_NAME = "first_portfolio_db"
# DB_USER = "postgres"           # local default - change if you create another user
# DB_PASSWORD = "Thomasope"
# DB_HOST = "127.0.0.1"
# DB_PORT = 5432

# # Your email settings
# SMTP_EMAIL = "thomasopeyemi1@gmail.com"
# SMTP_PASSWORD = "jnlwgpnipymvanif"
# SMTP_SERVER = "smtp.gmail.com"
# SMTP_PORT = 587

# ADMIN_USERNAME = "opnex"
# ADMIN_PASSWORD = "opnex123"



# config.py

import os
from dotenv import load_dotenv

load_dotenv()

DB_NAME = os.getenv("PGDATABASE")
DB_USER = os.getenv("PGUSER")
DB_PASSWORD = os.getenv("PGPASSWORD")
DB_HOST = os.getenv("PGHOST")
DB_PORT = os.getenv("PGPORT")

SMTP_EMAIL = "thomasopeyemi1@gmail.com"
SMTP_PASSWORD = "jnlwgpnipymvanif"   # your Gmail app password
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

ADMIN_USERNAME = "opnex"
ADMIN_PASSWORD = "opnex123"
