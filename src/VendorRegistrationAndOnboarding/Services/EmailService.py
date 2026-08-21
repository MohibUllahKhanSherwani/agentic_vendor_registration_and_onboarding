import os
from dotenv import load_dotenv
from VendorRegistrationAndOnboarding.DTOs.EmailDTO import EmailContent
from azure.communication.email import EmailClient
from typing import Optional

load_dotenv()


class EmailService:

    def __init__(self):
        self.connection_string = os.getenv("AZURE_COMMUNICATION_SERVICE_CONNECTION_STRING")
        if not self.connection_string:
            print("⚠️ Warning: AZURE_COMMUNICATION_SERVICE_CONNECTION_STRING is missing in .env")
 
    async def send_email(
        self,
        email_data: EmailContent,
        sender_address: str = "DoNotReply@9179d365-04dd-4314-830a-bf57f1fab6ab.azurecomm.net",
        sender_display_name: str = "VendorConnect",
    ) -> Optional[str]:
 
        try:
            client = EmailClient.from_connection_string(
                self.connection_string
            )
 
            message = {
                "senderAddress": sender_address,
                "senderDisplayName": sender_display_name,
                "recipients": {
                    "to": [
                        {
                            "address": email_data.receiver
                        }
                    ]
                },
                "content": {
                    "subject": email_data.subject,
                    "html": email_data.body
                },
            }
 
            poller = client.begin_send(message)
            result = poller.result()
 
            print(f"✅ Email sent successfully.")
 
            return result
 
        except Exception as e:
            print(f"❌ Failed to send email: {e}")
            return None
       