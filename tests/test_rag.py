# generator/generator.py

import openai
from config import API_CONFIG
from typing import List, Dict
import json
from datetime import datetime, date

class DateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (date, datetime)):
            return obj.isoformat()
        return super().default(obj)

class ResponseGenerator:
    def __init__(self):
        openai.api_key = API_CONFIG['openai_api_key']
        
    def generate_response(self, query: str, context: List[Dict]) -> str:
        """Generate a response using the retrieved context"""
        
        # Format context into a string using custom encoder
        formatted_context = json.dumps(context, indent=2, cls=DateTimeEncoder)
        
        # Create the prompt
        prompt = f"""Based on the following port operations data:
{formatted_context}

Answer this question: {query}

Provide a clear and concise response using only the information given in the context."""

        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a port operations assistant. Provide accurate information based solely on the given context."},
                    {"role": "user", "content": prompt}
                ]
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error generating response: {str(e)}"

    def preprocess_context(self, context: List[Dict]) -> List[Dict]:
        """Preprocess context to ensure all data is serializable"""
        processed_context = []
        for item in context:
            processed_item = {}
            for key, value in item.items():
                if isinstance(value, (date, datetime)):
                    processed_item[key] = value.isoformat()
                else:
                    processed_item[key] = value
            processed_context.append(processed_item)
        return processed_context