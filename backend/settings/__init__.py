import os
from dotenv import load_dotenv

load_dotenv()

# Ensure development settings are not used in testing and production:
if os.getenv("ENVIRONMENT") == "PRODUCTION":
    from .prod import *
else:
    from .dev import *
