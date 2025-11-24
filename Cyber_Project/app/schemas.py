
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class LogCreate(BaseModel):
    src_ip: str
    dest: Optional[str] = "iot-sensor"
    method: Optional[str] = "GET"
    path: Optional[str] = "/"
    user_agent: Optional[str] = "unknown"
