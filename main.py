import discord
from discord.ext import commands
import whois

domain_name = ""
domain_info = whois.whois(domain_name)
domain_info_str = str(domain_info)
CHANNEL_ID = ''
TOKEN = ''
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
        await self.change_presence(status=discord.Status.online, activity=discord.Game("오신트"))
        channel = await self.fetch_channel("")
        # await channel.send("오신트 하는 중")
        user_id = 325972485923143681  # 멘션할 유저의 ID
        user = await self.fetch_user(user_id)

        if "tucows" in domain_info_str:
            pass
            # await channel.send('sangwon.dev 도메인이 tucows한테 있어')
            exit(0)
        else:
            await channel.send(f'{user.mention} sangwon.dev 도메인이 tucows한테 없어! 바로 먹자')
            exit(0)


intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
client.run(TOKEN)