from pydantic import BaseModel, Field
from typing import Optional


class SignUp(BaseModel):
    name: str
    email: str
    phone_number: int
    password: str
    confirm_password: str
    Reference_ID: Optional[str] = Field(None)
