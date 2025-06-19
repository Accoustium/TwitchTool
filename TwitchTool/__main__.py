import asyncio
import os
import dotenv
from twitchBot import TwitchBot
import eel


PATH = os.path.dirname(os.path.abspath(__file__))


class TwitchTool:
    def __init__(self):
        dotenv.load_dotenv(os.path.join(PATH, '.env'))
        eel.init(os.path.join(PATH, 'web'))
        self.twitch_bot = TwitchBot(
            token=os.getenv('TWITCH_OAUTH_TOKEN'),
            client_id=os.getenv('TWITCH_CLIENT_ID'),
            nick=os.getenv('TWITCH_NICK')
        )

    def start(self) -> None:
        eel.start('index.html', size=(800, 600), block=False)
        # await self.twitch_bot.start()

        while True:
            eel.sleep(10)

if __name__ == "__main__":
    tool = TwitchTool()
    tool.start()