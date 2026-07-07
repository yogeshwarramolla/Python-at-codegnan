from smtplib import SMTP
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

smtp_server = "smtp.gmail.com"
smtp_port = 587
sender_email = "your mail"
passkey = "your pass key here"

def singleEmailSend(to_Email, subject, body):
    msg = MIMEMultipart()

    msg["From"] = sender_email
    msg["To"] = to_Email
    msg["Subject"] = subject

    msg.attach(MIMEText(body, "plain"))

    try:
        server = SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, passkey)

        server.sendmail(
            sender_email,
            to_Email,
            msg.as_string()
        )

        server.quit()

        return f"Successfully sent email to {to_Email}"

    except Exception as e:
        return f"Failed to send email: {e}"


to_Email = input("Enter the email address: ")
subject = input("Enter email subject: ")
body = input("Enter your message: ")

print(singleEmailSend(to_Email, subject, body))