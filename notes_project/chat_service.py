import google.generativeai as genai
from config.prj_config import setting


genai.configure(api_key=setting.GOOGLE_API_KEY)

class AIService:
    def __init__(self):
        self.model = genai.GenerativeModel("gemini-2.5-flash")

    def generate(self, prompt: str) -> str:
        response = self.model.generate_content(prompt)
        return response.text
    
    def generate_title(self, text: str) -> str:
        return self.generate(f"Generate one short title for:\n{text}")
    
    def summarize(self, text: str) -> str:
        return self.generate(f"Summarize following text effectively: {text}")
