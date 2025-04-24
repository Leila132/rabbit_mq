import aiohttp


class TelegramSender:
    def __init__(self):
        self.TOKEN = ""
        self.CHAT_ID = 111111111

    async def send_message(self, message: str) -> None:
        url = f"https://api.telegram.org/bot{self.TOKEN}/sendMessage"
        params = {"chat_id": self.CHAT_ID, "text": message}

        async with aiohttp.ClientSession() as session:
            async with session.post(url, params=params) as response:
                if response.status != 200:
                    error = await response.text()
                    raise Exception(f"Telegram API error: {error}")
