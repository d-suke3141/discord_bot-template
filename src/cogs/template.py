import discord
import logging
from discord.commands import slash_command
from discord.ext.commands import Cog

logger = logging.getLogger(__name__)

class Template(Cog, name='template'):
    group = discord.SlashCommandGroup('group', 'Here are the commands related to group.')

    def __init__(self, bot: discord.Bot):
        self.bot = bot

    @group.command()
    async def groupcommand1(self, ctx: discord.ApplicationContext):
        """
        グループコマンド1です。
        """
        await ctx.respond('This is group command1.')

    @slash_command()
    async def command1(self, ctx: discord.ApplicationContext):
        """
        コマンド1です。
        """
        await ctx.respond('This is command1.')

    @Cog.listener(name='on_message')
    async def on_message(self, message: discord.Message):
        if message.author.bot:
            return
        if self.bot.user in message.mentions:
            await message.add_reaction('\U0001f44d')

def setup(bot):
    bot.add_cog(Template(bot))

def teardown(bot: discord.Bot):
    bot.remove_cog('template')