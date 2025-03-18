import logging
import threading
from instabot.instagram_client import InstagramClient
from instabot.message_handler import reply_to_unread_messages
from instabot.utils import setup_logging
from instabot.webserver import app

def start_flask():
    app.run(host="0.0.0.0", port=8080)

def main():
    setup_logging()
    instagram_client = InstagramClient()
    
    try:
        instagram_client.login()
        reply_to_unread_messages(instagram_client)
        
        # Start Flask server in a new thread
        threading.Thread(target=start_flask).start()
        
    except Exception as e:
        logging.error(f"❌ An error occurred: {e}")

if __name__ == "__main__":
    main()
