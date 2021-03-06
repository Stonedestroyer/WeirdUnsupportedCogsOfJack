from abc import ABC, ABCMeta
from typing import Any

import aiohttp
from discord.ext.commands import CogMeta
from redbot.core.bot import Red


class CogAndABCMeta(CogMeta, ABCMeta):
    """
    This allows the metaclass used for proper type detection to
    coexist with discord.py's metaclass.
    """


class MixinMeta(ABC):
    def __init__(self, *_args: Any) -> None:
        self.bot: Red
        self.session: aiohttp.ClientSession

    def cog_unload(self) -> None:
        # this is here so that super calls work
        pass

    def post_cog_add(self) -> None:
        """This is ran after cog is added to the bot."""
