import json
import logging.config
import os

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

bot_token = os.environ.get("BOT_TOKEN")
guild_ids = os.environ.get("GUILD_IDS").split(',')

with open('./src/log_config.json', 'r') as f:
    log_conf = json.load(f)

logging.config.dictConfig(log_conf)
logger = logging.getLogger(__name__)

INITIAL_EXTENSIONS = [
    'cogs.general',
    'cogs.develop',
    'cogs.template',
]

class BotTemplate(commands.Bot):
    def __init__(self):
        super().__init__(help_command=None, debug_guilds = guild_ids)
        for cog in INITIAL_EXTENSIONS:
            try:
                self.load_extension(cog)
            except Exception:
                logger.exception(f'Failed to load extension {cog}.')

    async def on_ready(self):
        logger.info('-----')
        logger.info(self.user.name)
        logger.info(self.user.id)
        logger.info('-----')


if __name__ == "__main__":
    bot = BotTemplate()
    bot.run(bot_token)
