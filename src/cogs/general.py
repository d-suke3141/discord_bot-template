import discord
import logging
from discord.commands import slash_command
from discord.ext.commands import Cog

logger = logging.getLogger(__name__)

class General(Cog, name='general'):
    def __init__(self, bot: discord.Bot):
        self.bot = bot

    @slash_command()
    async def info(self, ctx: discord.ApplicationContext):
        """
        ボットの情報を表示する
        """
        embed = discord.Embed(title="ボットの情報", description="ボットの情報を表示します。", color=0x00ff00)
        embed.add_field(name="ボット名", value=self.bot.user.name, inline=False)
        embed.add_field(name="ボットID", value=self.bot.user.id, inline=False)
        embed.add_field(name="作成日時", value=self.bot.user.created_at, inline=False)
        embed.add_field(name="参加サーバー数", value=len(self.bot.guilds), inline=False)
        await ctx.respond(embed=embed)

    @slash_command()
    async def help(self, ctx: discord.ApplicationContext):
        """
        ヘルプを表示する
        """
        embed = discord.Embed(title="Help page!", description="ヘルプを表示します。", color=0xEEEEEE)
        embed.add_field(name="/command1", value='description', inline=True)
        embed.add_field(name="/command2", value='description', inline=True)
        embed.add_field(name="/command3", value='description', inline=True)
        embed.add_field(name="/command4", value='description', inline=True)
        embed.add_field(name="/command5", value='description', inline=True)
        embed.add_field(name="/command6", value='description', inline=True)
        await ctx.respond(embed=embed)


def setup(bot: discord.Bot):
    bot.add_cog(General(bot))

def teardown(bot: discord.Bot):
    bot.remove_cog('general')