import os
from dotenv import load_dotenv

load_dotenv()

COGNODB_URI = os.getenv("COGNODB_URI")
COGNODB_USERNAME = os.getenv("COGNODB_USERNAME")
COGNODB_PASSWORD = os.getenv("COGNODB_PASSWORD")


if not COGNODB_URI:
    raise ValueError("COGNODB_URI is not set")

if not COGNODB_USERNAME:
    raise ValueError("COGNODB_USERNAME is not set")

if not COGNODB_PASSWORD:
    raise ValueError("COGNODB_PASSWORD is not set")