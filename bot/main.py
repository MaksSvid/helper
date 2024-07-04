import asyncio
import logging
import sys

from bot.src.helperbot import main

logging.basicConfig(level=logging.INFO, stream=sys.stdout)
asyncio.run(main())