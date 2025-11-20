from pydantic import BaseModel, EmailStr
from typing import Optional

class MessageCreate(BaseModel):
    name: str
    email: EmailStr
    phone: Optional[str] = None
    message: str

class ProjectCreate(BaseModel):
    title: str
    description: str
    image_url: str
    live_url: str