import os
from dotenv import load_dotenv
load_dotenv()

x = os.environ.get("test34")
print(x)