# debug.py
import os
from dotenv import load_dotenv
from openai import OpenAI
from config import API_CONFIG

def debug_openai():
    # Load environment variables
    load_dotenv()
    
    print("Debug Information:")
    print("-----------------")
    
    # Check if OPENAI_API_KEY exists in environment
    api_key = os.getenv('OPENAI_API_KEY')
    print(f"OpenAI API Key exists: {bool(api_key)}")
    
    # Check if API key is loaded in config
    print(f"OpenAI API Key in config: {bool(API_CONFIG.get('openai_api_key'))}")
    
    # Test OpenAI API
    if api_key:
        client = OpenAI(api_key=api_key)
        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "user", "content": "Test message"}
                ]
            )
            print("✓ OpenAI API test successful")
            print(f"Response: {response.choices[0].message.content}")
        except Exception as e:
            print(f"✗ OpenAI API test failed: {str(e)}")
    else:
        print("✗ No OpenAI API key found")

if __name__ == "__main__":
    debug_openai()