# clever
CleverBot.io in Python

```python
>>> import clever
>>> import asyncio
>>> loop = asyncio.get_event_loop()
>>> client = clever.CleverBot(user='...', key='...')
>>> loop.run_until_complete(print(client.query("Yo")))
Hi.
```
