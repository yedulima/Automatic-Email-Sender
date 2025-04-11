import os
from smtplib import SMTP_SSL
from email.message import EmailMessage

def attach_file(msg: EmailMessage, file_path: os.path) -> EmailMessage:
    file_extension: str = os.path.splitext(file_path)[1][1:]
    file_name: str = os.path.basename(file_path)

    with open(file_path, "rb") as file:
        msg.add_attachment(file.read(), maintype="application", subtype=file_extension, filename=file_name)

    return msg

def send_email(subject: str, sender: str, password_key: str, target: str, content: str, attachments_files = []) -> None:
    with SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender, password_key)

        msg = EmailMessage()
        msg["Subject"] = subject
        msg["From"] = sender
        msg["To"] = target
        msg.set_content(content)

        if attachments_files:
            for file in attachments_files:
                msg = attach_file(msg, file)

        server.send_message(msg)

        print("Email sent succesfully!")

        server.quit()

if __name__ == "__main__":
    pass