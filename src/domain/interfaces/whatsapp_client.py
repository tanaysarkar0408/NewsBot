from abc import ABC, abstractmethod

class IWhatsAppClient(ABC):
    @abstractmethod
    def send_message(self, recipient_number: str, message: str) -> bool:
        """Sends a text message via WhatsApp."""
        pass
