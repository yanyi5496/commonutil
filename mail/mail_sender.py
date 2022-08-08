import json
import smtplib
from email.mime.text import MIMEText


def read_conf(conf_file='conf.json'):
    with open(conf_file, 'r') as f:
        conf = json.load(f)
    host = conf.get('host')
    port = conf.get('port')
    sender = conf.get('sender')
    password = conf.get('password')
    receivers = conf.get('receivers')
    title = conf.get('title')
    return host, port, sender, password, receivers, title


def build_and_send(title, content, sender, receiver, host, port, password):
    message = MIMEText(content, 'plain', 'utf-8')
    message['From'] = sender
    message['To'] = receiver
    message['Subject'] = title
    client = smtplib.SMTP_SSL(host, port, timeout=10)
    login_result = client.login(sender, password)
    client.sendmail(sender, receiver, message.as_string())
    client.close()


def main(conf: tuple, content):
    receives = conf[4]
    for i in receives:
        build_and_send(title=conf[5], content=content, sender=conf[2], receiver=str(i), host=conf[0], port=conf[1],
                       password=conf[3])


if __name__ == '__main__':
    main(read_conf(), content='XXXXXXXXXXXXX1')
