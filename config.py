import os

from dotenv import load_dotenv

load_dotenv()


AWS_REGION = os.getenv("AWS_REGION")
KNOWLEDGE_BASE_ID = os.getenv("BEDROCK_KNOWLEDGE_BASE_ID")
MODEL_ID = os.getenv("BEDROCK_MODEL_ID")


if not AWS_REGION:
    raise ValueError("AWS_REGION is not configured")

if not KNOWLEDGE_BASE_ID:
    raise ValueError("BEDROCK_KNOWLEDGE_BASE_ID is not configured")

if not MODEL_ID:
    raise ValueError("BEDROCK_MODEL_ID is not configured")