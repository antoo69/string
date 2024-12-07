from pyrogram_v2 import Client

def main():
    print("=== Pyrogram v2 String Session Generator ===")
    app = Client(":memory:")
    with app:
        print("\nString Session Anda:")
        print(app.export_session_string())

if __name__ == "__main__":
    main()
