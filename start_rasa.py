from dotenv import load_dotenv
import os
import subprocess

# Load environment variables
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
dotenv_path = os.path.join(parent_dir, '.env')

load_dotenv(dotenv_path)

# Start Rasa server
subprocess.call(['rasa', 'run', '--enable-api', '--debug'])