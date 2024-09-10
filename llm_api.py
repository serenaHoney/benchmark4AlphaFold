"""
The OpenAI API uses API keys for authentication
"""

from openai import OpenAI

client = OpenAI(
  organization='YOUR_ORG_ID',
  project='$PROJECT_ID',
)
