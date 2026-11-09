import os

from dotenv import load_dotenv

load_dotenv()


API_KEY = os.getenv("API_KEY")
USER = os.getenv("USER")

print(API_KEY)
print(USER)