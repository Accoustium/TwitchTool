import discord


class DiscordBot(discord.Client):
    def __init__(self, token: str, intents: discord.Intents = discord.Intents.default()):
        super().__init__(intents=intents)
        self.token = token

        self.commands = {}
        self.variables = {}

    async def on_ready(self):
        print(f'Logged in as {self.user.name} - {self.user.id}')

    async def run_bot(self):
        await self.start(self.token)  # Start the bot with the provided token
