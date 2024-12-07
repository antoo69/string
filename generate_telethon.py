from telethon.sync import TelegramClient
from telethon.sessions import StringSession

def main():
    print("=== Telethon String Session Generator ===")
    print("Masukkan nomor telepon Anda:")
    phone = input("> ")
    client = TelegramClient(StringSession(), api_id=None, api_hash=None)  # Masukkan nilai default API ID dan API Hash
    client.connect()

    if not client.is_user_authorized():
        client.send_code_request(phone)
        code = input("Masukkan kode OTP yang Anda terima: ")
        try:
            client.sign_in(phone, code)
        except Exception as e:
            if "2FA" in str(e):
                password = input("Akun Anda memiliki verifikasi dua langkah.\nMasukkan password Anda: ")
                client.sign_in(password=password)

    print("\nString Session Anda:")
    print(client.session.save())
    client.disconnect()

if __name__ == "__main__":
    main()
