from discord.ext.commands import Cog
from discord.commands import SlashCommandGroup
import discord

class Develop(Cog, name='develop'):
    group = SlashCommandGroup('develop', 'Here are the commands related to develop.')

    def __init__(self, bot: discord.Bot):
        self.bot = bot

    # Cogのロード・アンロード・リロードをしてもDiscord側では更新されない
    @group.command()
    async def reload(self, ctx: discord.ApplicationContext, extension: str):
        """
        Cogをリロードする
        """
        self.bot.reload_extension(name=f'cogs.{extension}')
        await ctx.respond(f'{extension} をリロードしました。')

    @group.command()
    async def load(self, ctx: discord.ApplicationContext, extension: str):
        """
        Cogをロードする
        """
        self.bot.load_extension(name=f'cogs.{extension}')
        await ctx.respond(f'{extension} をロードしました。')

    @group.command()
    async def unload(self, ctx: discord.ApplicationContext, extension: str):
        """
        Cogをアンロードする
        """
        self.bot.unload_extension(name=f'cogs.{extension}')
        await ctx.respond(f'{extension} をアンロードしました。')

    @group.command()
    async def cog_list(self, ctx: discord.ApplicationContext):
        """
        Cogのリストを表示する
        """
        cog_list = [cog for cog in self.bot.cogs.keys()]
        print(cog_list)
        await ctx.respond(f'{cog_list}')


def setup(bot: discord.Bot):
    bot.add_cog(Develop(bot))

def teardown(bot: discord.Bot):
    bot.remove_cog('develop')