from pydantic import BaseModel, Field


class Request(BaseModel):
    username: str = Field(None, title="Github User Name", max_length=1000)
