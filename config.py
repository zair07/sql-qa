from pydantic_settings import BaseSettings, SettingsConfigDict
import os

class Settings(BaseSettings):
    openai_key: str

    langchain_api_key: str
    langchain_project: str
    langchain_tracing_v2: str = "true"
    langchain_endpoint: str = "https://api.smith.langchain.com"
    
    db_host: str
    db_user: str
    db_password: str
    db_name: str
    
    model_config = SettingsConfigDict(env_file=".env")

def setup_langsmith(settings: Settings):
    os.environ['LANGCHAIN_TRACING_V2'] = settings.langchain_tracing_v2
    os.environ['LANGCHAIN_ENDPOINT'] = settings.langchain_endpoint
    os.environ['LANGCHAIN_API_KEY'] = settings.langchain_api_key
    os.environ['LANGCHAIN_PROJECT'] = settings.langchain_project