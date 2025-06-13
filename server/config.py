from dotenv import load_dotenv
import os
#load environment variables from the .env file
load_dotenv()

class Config():
    SQLALCHEMY_DATABASE_URI=os.getenv("FLASK_SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS=bool(int(os.getenv("FLASK_SQLALCHEMY_TRACK_MODIFICATIONS")))
    SECRET_KEY = os.getenv("FLASK_SECRET_PASSWORD")
   