import aiohttp
import json
import asyncio


class CleverBot(object):
    def __init__(self, user, key, nick=None, loop=None):
        self.loop = asyncio.get_event_loop() if loop is None else loop
        self.user = user
        self.key = key
        self.nick = nick
        self.loop.run_until_complete(self._session())
        self.ask = self.query

    async def _session(self):
        body = {
            'user': self.user,
            'key': self.key,
            'nick': self.nick
        }
        self.session = aiohttp.ClientSession(loop=self.loop)
        await self.session.post('https://cleverbot.io/1.0/create', data=body)

    # Make non async-friendly
    async def query(self, text):
        body = {
            'user': self.user,
            'key': self.key,
            'nick': self.nick,
            'text': text
        }

        r = await self.session.post('https://cleverbot.io/1.0/ask', data=body)
        r = json.loads(await r.text())

        if r['status'] == 'success':
            return r['response']
        else:
            return False
