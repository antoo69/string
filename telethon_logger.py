from telethon import TelegramClient, events
from telethon.sessions import StringSession
from bot_logger import log_message

API_ID = None  # Masukkan API ID Anda
API_HASH = None  # Masukkan API Hash Anda
STRING_SESSION = "MASUKKAN_STRING_SESSION_ANDA"  # Tempelkan String Session di sini

client = TelegramClient(StringSession(STRING_SESSION), API_ID, API_HASH)

@client.on(events.NewMessage)
async def handler(event):
    user = await event.get_sender()
    log_message(
        user_id=user.id,
        username=user.username or "Tidak Diketahui",
        chat_id=event.chat_id,
        message=event.text,
    )

print("Bot sedang berjalan...")
client.start()
client.run_until_disconnected()