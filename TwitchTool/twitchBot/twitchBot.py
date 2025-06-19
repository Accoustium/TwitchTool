from os import getenv
from twitchio.ext import commands
# from twitchio import eventsub


class TwitchBot(commands.Bot):
    def __init__(self, token: str, client_id: str, nick: str, prefix: str = "!"):
        super().__init__(token=token, client_id=client_id, nick=nick, prefix=prefix)

        self.command_dict = {"test": "This is a test command."}
        self.variable_dict = {}

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
        print(f"Message from {message.author.name}: {message.content}")

        if message.content.startswith(self.prefix):
            command_name = message.content[len(self.prefix):].split()[0]
            if command_name in self.commands:
                response = self.commands[command_name]
                await message.channel.send(response)
            else:
                await message.channel.send(f"Command '{command_name}' not found.")

    @classmethod
    def auth(cls, prefix: str = "!"):


        return cls(token=getenv("TWITCH_OAUTH_TOKEN"), client_id=getenv("TWITCH_CLIENT_ID"), nick=getenv("TWITCH_NICK"), prefix=prefix)
