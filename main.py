# main.py
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from config import API_ID, API_HASH, STRING_SESSION, LOG_DIR
from bot_logger import log_message

client = TelegramClient(StringSession(STRING_SESSION), API_ID, API_HASH)

@client.on(events.NewMessage)
async def handler(event):
    """Handle pesan masuk dan simpan ke log."""
    user = await event.get_sender()
    phone_number = user.phone if hasattr(user, "phone") else None  # Ambil nomor telepon jika ada
    log_message(
        user_id=user.id,
        username=user.username,
        chat_id=event.chat_id,
        phone_number=phone_number,
        message=event.text,
    )

print("Bot sedang berjalan...")
client.start()
client.run_until_disconnected()
