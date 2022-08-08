class MailConfig:
    def __int__(self, sender, host, port, password, receivers):
        self.sender = sender
        self.host = host
        self.port = port
        self.password = password
        self.receivers = receivers
