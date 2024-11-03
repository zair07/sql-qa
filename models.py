from pydantic import BaseModel, Field

class ResponseFormatter(BaseModel):
    sql_query: str = Field(description="A valid sql query based on user's natural language query")