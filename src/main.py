from discord.ext import commands
from secret import bot_token, guild_ids

INITIAL_EXTENSIONS = [
    'cogs.general',
    'cogs.develop',
    'cogs.template',
]

class BotTemplate(commands.Bot):
    def __init__(self):
        super().__init__(help_command=None, debug_guilds = guild_ids)
        print(self.debug_guilds)
        for cog in INITIAL_EXTENSIONS:
            try:
                self.load_extension(cog)
            except Exception:
                print(f'Failed to load extension {cog}.')

    async def on_ready(self):
        print('-----')
        print(self.user.name)
        print(self.user.id)
        print('-----')


if __name__ == "__main__":
    bot = BotTemplate()
    bot.run(bot_token)
