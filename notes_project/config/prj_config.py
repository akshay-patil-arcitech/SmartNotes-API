from pydantic_settings import BaseSettings, SettingsConfigDict

class prj_settings(BaseSettings):
    DB_USER : str
    DB_PASSWORD : str
    OPENAI_API_KEY : str
    GROQ_API_KEY : str
    HOST : str
    DB_NAME : str
    SECRET_KEY : str
    ALGORITHM : str
    GOOGLE_API_KEY : str
    
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="UTF-8"
    )
    
setting = prj_settings()