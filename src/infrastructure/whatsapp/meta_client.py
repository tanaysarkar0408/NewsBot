import os
import requests
from src.domain.interfaces.whatsapp_client import IWhatsAppClient

class MetaWhatsAppClient(IWhatsAppClient):
    def __init__(self):
        self.phone_number_id = os.getenv("WHATSAPP_PHONE_NUMBER_ID")
        self.token = os.getenv("WHATSAPP_TOKEN")
        self.base_url = f"https://graph.facebook.com/v22.0/{self.phone_number_id}/messages"

    def send_message(self, recipient_number: str, message: str) -> bool:
        if not self.phone_number_id or not self.token:
            print("WhatsApp credentials not configured. Skipping message send.")
            print(f"[Simulated Message to {recipient_number}]: {message}")
            return True

        headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }
        
        payload = {
            "messaging_product": "whatsapp",
            "to": recipient_number,
            "type": "text",
            "text": {
                "body": message
            }
        }

        try:
            response = requests.post(self.base_url, headers=headers, json=payload)
            response.raise_for_status()
            print("Message sent successfully via Meta API!")
            return True
        except requests.exceptions.RequestException as e:
            print(f"Failed to send message: {e}")
            if e.response is not None:
                print(e.response.text)
            return False
