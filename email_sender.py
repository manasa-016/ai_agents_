import smtplib
from email.message import EmailMessage
from secrets import sender_email, receiver_email, app_password

# Email details
def send_email(receiver_email,subject,content):

    msg = EmailMessage()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = subject
    msg.set_content(content)

    # Send email
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, app_password)
        server.send_message(msg)

print("Email sent successfully ✅")

send_email(receiver_email="madhurabhaskar66@gmail.com",subject="Hello",content="This is a test email from Python")
