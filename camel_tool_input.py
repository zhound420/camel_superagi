
from pydantic import BaseModel, Field
from typing import List

class CamelToolInput(BaseModel):
    messages: List[str] = Field(..., description="List of messages to be processed by the tool")
