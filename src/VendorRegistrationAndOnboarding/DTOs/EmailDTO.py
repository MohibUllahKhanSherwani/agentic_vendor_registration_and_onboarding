from pydantic import BaseModel

class EmailContent(BaseModel):
    subject: str
    body: str
    receiver: str
