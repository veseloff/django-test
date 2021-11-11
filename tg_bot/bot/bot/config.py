from dotenv import load_dotenv
import os

load_dotenv()
DB_PASS = os.getenv('PASSWORD_DATA_BASE')
DB_NAME = os.getenv('NAME_DATA_BASE')
DB_USER = os.getenv('USER_DATA_BASE')
HOST = os.getenv('HOST_DATA_BASE')
PORT = os.getenv('PORT_DATA_BASE')
TOKEN = os.getenv('BOT_TOKEN')
