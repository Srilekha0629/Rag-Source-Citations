from pydantic import BaseModel, Field
from typing import Any, Optional, Literal


class SearchQueryRequest(BaseModel):
    model_provider: str
    query: str

class ChatRequest(BaseModel):
    model_provider: str
    model_name: str
    message: str

class SourceCitation(BaseModel):
    file_name: str
    page: Optional[int] = None
    snippet: str

class ChatResponseData(BaseModel):
    answer: str
    sources: list[SourceCitation] = Field(default_factory=list)

class StandardAPIResponse(BaseModel):
    status: Literal["success", "error"]
    data: Optional[Any] = None
    message: Optional[str] = None

