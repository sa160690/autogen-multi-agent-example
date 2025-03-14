import os
from dotenv import load_dotenv, find_dotenv


def load_env():
    """Load environment variables from .env file.
    
    This function uses python-dotenv to load environment variables from a .env file
    in the project directory. It will look for the .env file in the current directory
    and parent directories.
    """
    _ = load_dotenv(find_dotenv())

def get_openai_api_key():
    """Retrieve the OpenAI API key from environment variables.
    
    Returns:
        str: The OpenAI API key if found in environment variables, None otherwise.
        
    Note:
        This function calls load_env() to ensure environment variables are loaded
        before attempting to retrieve the API key.
    """
    load_env()
    openai_api_key = os.getenv("OPENAI_API_KEY")
    return openai_api_key