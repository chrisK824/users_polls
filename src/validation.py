from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from dotenv import load_dotenv
import os


load_dotenv()
SENDGRID_API_KEY = os.environ["SENDGRID_API_KEY"]

def send_activation_email(poll_id,email, url):
    message = Mail(
        from_email='christos.karvouniaris247@gmail.com',
        to_emails=email,
        subject='Account activation',
        html_content=f'<strong>Please click this <a href="{url}?poll_id={poll_id}&email={email}">link</a> to validate your vote.</strong>')
    try:
        sg = SendGridAPIClient(SENDGRID_API_KEY)
        sg.send(message)
    except Exception as e:
        raise Exception(f"{e}")