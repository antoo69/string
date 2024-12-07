# config.py
import os

# API ID dan API Hash didapatkan dari my.telegram.org
API_ID = int(os.getenv("API_ID", "123456"))  # Ganti dengan API ID Anda
API_HASH = os.getenv("API_HASH", "your_api_hash")  # Ganti dengan API Hash Anda
STRING_SESSION = os.getenv("STRING_SESSION", "")  # Tempelkan String Session di sini, jika tersedia

# Folder log
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)
