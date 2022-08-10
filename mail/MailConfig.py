class MailConfig():
    def __init__(self, sender, host, port, password, receivers, title):
        self.sender = sender
        self.host = host
        self.port = port
        self.password = password
        self.receivers = receivers
        self.title = title
