
from requests import get
from requests.api import request

from .. import loader, utils


@loader.tds
class Circle(loader.Module):
    """Кругляшок"""
    strings = {'name': 'Circle'}

    @loader.owner
    async def circlecmd(self, m):
        """.circle - тест :)
        """
        await m.edit("<a href=\""+get("https://t.me/vibe_circle").json()['url']+"\">Лови</a>")
