import logging
from instagrapi import Client
from .config import INSTAGRAM_USERNAME, INSTAGRAM_PASSWORD
from .utils import random_delay

class InstagramClient:
    def __init__(self):
        self.client = Client()

    def login(self):
        random_delay(30, 60)
        try:
            self.client.login(INSTAGRAM_USERNAME, INSTAGRAM_PASSWORD)
            logging.info("✅ Logged into Instagram successfully.")
        except Exception as e:
            logging.error(f"❌ Instagram login failed: {e}")
            raise e

    def fetch_unread_threads(self):
        try:
            inbox_threads = self.client.direct_threads(selected_filter='unread')
            unread_threads = [thread for thread in inbox_threads if thread.messages]
            logging.info(f"📩 Found {len(unread_threads)} unread messages.")
            return unread_threads
        except Exception as e:
            logging.error(f"❌ Error fetching threads: {e}")
            return []

    def send_message(self, thread_id, message):
        try:
            self.client.direct_send(message, thread_ids=[thread_id])
            logging.info(f"✉️ Sent message in thread {thread_id}.")
        except Exception as e:
            logging.error(f"❌ Error sending message: {e}")
