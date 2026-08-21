from pydantic import BaseModel

class RootConfigs:
    class Root(BaseModel):
        app_name: str
    
    class ConversationConfig(BaseModel):
        conversational_history_db: str
    
    class ThinkingConfig(BaseModel):
        max_output_tokens: int
        include_thoughts: bool
    
    class ContentConfig(BaseModel):
        max_output_tokens: int
        temperature: float
        thinking: "RootConfigs.ThinkingConfig"
    
    class Models(BaseModel):
        model_1:str 
        model_2:str 

    class LLmConfig(BaseModel):
        model_name: "RootConfigs.Models"
        description: str
    
    class SessionConfig(BaseModel):
        max_messages: int

    class EmailTemplates(BaseModel):
        OTP: str