import smtplib

username = 'ramsteinnnlake@gmail.com'
password = ''

def send_mail(text='Email body', subject = 'Hello World', from_email = 'ramsteinnnlake@gmail.com', to_emails=[]):
    assert isinstance(to_emails, list)

    # Login to SMTP server
    server = smtplib.SMTP(host='smtp.gmail.com', port=587)
    server.ehlo()
    server.starttls()
    server.login(username, password)
    server.sendmail(from_email, to_emails, msg_str)

    server.quit()

    # with smtplib.SMTP() as server:
    #     pass