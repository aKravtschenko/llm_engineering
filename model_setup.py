import os
from dotenv import load_dotenv

class ModelSetup:
    def __init__(
        self,
        dotenv_path: str = ".env",
        verbose: bool = True,
        openai_model: str = "openai/gpt-4o-mini",
        deepseek_model: str = "deepseek/deepseek-chat-v3-0324",
        gemini_model: str = "gemini-2.0-flash",
        openrouter_url: str = "https://openrouter.ai/api/v1"):
        
        self.verbose = verbose
        load_dotenv(dotenv_path=dotenv_path, override=True)

        self.OPENAI_MODEL = openai_model
        self.DEEPSEEK_MODEL = deepseek_model
        self.GEMINI_MODEL = gemini_model
        self.OPENROUTER_URL = openrouter_url

        self.openrouter_api_key = os.getenv('OPENROUTER_API_KEY')
        self.google_api_key = os.getenv('GOOGLE_API_KEY')
        self.imagegen_api_key = os.getenv("IMAGEGEN_API_KEY")

        if self.verbose:
            self._check_keys()

    def _check_keys(self):
        if self.openrouter_api_key:
            print(f"✅ Openrouter API Key exists and begins with: {self.openrouter_api_key[:8]}")
        else:
            print("⚠️ Openrouter API Key not set")

        if self.google_api_key:
            print(f"✅ Google API Key exists and begins with: {self.google_api_key[:8]}")
        else:
            print("⚠️ Google API Key not set")
        if self.imagegen_api_key:
            print(f"✅ Imagegen API Key exists and begins with: {self.imagegen_api_key[:8]}")
        else:
            print("⚠️ Imagegen API Key not set")
            
    def _check_const(self):
        model_keys = ["OPENAI_MODEL", "DEEPSEEK_MODEL", "GEMINI_MODEL", "OPENROUTER_URL"]
        
        for key in model_keys:
            value = getattr(self, key)
            print(f"{key}: {value}")