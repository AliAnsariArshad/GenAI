import os
from pathlib import Path

from dotenv import load_dotenv

dotenv_path = Path('local.env')

load_dotenv(dotenv_path=dotenv_path)
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
# OPENAI_API_KEY = env_value["OPENAI_API_KEY"]
MODEL_NAME = "gpt-3.5-turbo"
