import os
import emailSender
from dotenv import load_dotenv

if __name__ == "__main__":
    load_dotenv()

    message_title: str = "Como você vai?"
    email: str = os.getenv("EMAIL")
    password: str = os.getenv("EMAIL_KEY")
    target: str = os.getenv("TARGET_EMAIL")
    attachments_files: list[str] = [] # Insert file paths here

    message: str = """\
Iai doido, tudo beleza?
Como você ta em :D

- Du
"""

    emailSender.send_email(message_title, email, password, target, message, attachments_files)