"""
The OpenAI API uses API keys for authentication
"""

from openai import OpenAI
import os

org_id = os.getenv('CHATGPT_ORG_ID')
api_key = os.getenv('CHATGPT_API_KEY')

client = OpenAI(
  organization = org_id,
  project = api_key,
)
