import os
from datetime import datetime

LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

def log_message(user_id, username, chat_id, message):
    """Log informasi pengguna dan pesan ke file."""
    log_file = os.path.join(LOG_DIR, f"{datetime.now().date()}.log")
    with open(log_file, "a", encoding="utf-8") as file:
        file.write(
            f"[{datetime.now()}] User ID: {user_id}, Username: {username}, Chat ID: {chat_id}, Message: {message}\n"
        )
    print(f"Pesan dari {username} (ID: {user_id}) telah disimpan ke log.")

