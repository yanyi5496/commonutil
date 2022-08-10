import json
import smtplib
from email.mime.text import MIMEText

from MailConfig import MailConfig


def read_conf(conf_file='conf.json'):
    with open(conf_file, 'r') as f:
        conf = json.load(f)
    host = conf.get('host')
    port = conf.get('port')
    sender = conf.get('sender')
    password = conf.get('password')
    receivers = conf.get('receivers')
    title = conf.get('title')
    mail = MailConfig(sender, host, port, password, receivers, title)
    return mail


def build_and_send(mail: MailConfig, content):
    message = MIMEText(content, 'plain', 'utf-8')
    message['From'] = mail.sender
    message['Subject'] = mail.title
    for i in mail.receivers:
        message['To'] = i
    client = smtplib.SMTP_SSL(mail.host, mail.port, timeout=10)
    login_result = client.login(mail.sender, mail.password)
    if 'success' in str(login_result[1]):
        client.sendmail(mail.sender, mail.receivers, message.as_string())
    client.close()


def main(content, path='conf.json'):
    conf = read_conf(path)
    build_and_send(conf, content)


if __name__ == '__main__':
    main(content='欢迎使用产品')
