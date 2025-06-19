import twitchio


class TwitchBot(twitchio.Client):
    def __init__(self, token: str, client_id: str, nick: str, prefix: str = "!"):
        super().__init__(token=token, client_id=client_id, nick=nick, prefix=prefix)
        self.token = token
        self.client_id = client_id
        self.nick = nick
        self.prefix = prefix

        self.commands = {}
        self.variables = {}

    def load_commands(self):
        raise NotImplementedError

    def load_variables(self):
        raise NotImplementedError

    def save_commands(self):
        raise NotImplementedError

    def save_variables(self):
        raise NotImplementedError

    async def event_ready(self):
        print(f"Logged in as {self.nick}")

    async def event_message(self, message):
        if message.author.name.lower() == self.nick.lower():
            return  # Ignore own messages

        print(f"Message from {message.author.name}: {message.content}")
