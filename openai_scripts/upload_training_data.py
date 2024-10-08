import os
from dotenv import load_dotenv

from openai import OpenAI

load_dotenv("secrets.env")
openai_api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=openai_api_key)
client.files.create(
  file=open("data/finetuning_data_unicode_fix.jsonl", "rb"),
  purpose="fine-tune"
)