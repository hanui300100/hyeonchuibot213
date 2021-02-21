import discord
import datetime
import asyncio
import os

client = discord.Client()

@client.event
async def on_ready():
    print(str(datetime.datetime.today()) + "\n----------\n봇 이름 : " + str(client.user) + "\n----------\n" + str(client.user) + "봇이 " +  str(datetime.datetime.today().year) + "년 " + str(datetime.datetime.today().month) + "월 " + str(datetime.datetime.today().day) + "일 " + str(datetime.datetime.today().hour) + "시 " + str(datetime.datetime.today().minute) + "분 " + str(datetime.datetime.today().second) + "초에 로그인 했습니다.")
#로그 채팅    await client.get_channel(792757695828197387).send("<@" + str(client.user.id) + ">봇이 " + str(datetime.datetime.today().year) + "년 " + str(datetime.datetime.today().month) + "월 " + str(datetime.datetime.today().day) + "일 " + str(datetime.datetime.today().hour) + "시 " + str(datetime.datetime.today().minute) + "분 " + str(datetime.datetime.today().second) + "초에 로그인 했습니다.\n\n`" + str(datetime.datetime.today()) + "`")
    messages = [f"은바천보!"]
    while True:
        await client.change_presence(status=discord.Status.online, activity=discord.Game(name=messages[0]))
        messages.append(messages.pop(0))
        await asyncio.sleep(2)

@client.event
async def on_message(message):
# /테스트
    if message.content.startswith("테스트"):
        embed = discord.Embed(color=0xc4a5df)
        embed.add_field(name=str(client.user), value="테스트 123", inline=True)
        embed.set_footer(text=message.author, icon_url=message.author.avatar_url)
        await message.channel.send(embed=embed)
        #CMD로그
        print("----------\n" + str(datetime.datetime.today().year) + "년 " + str(datetime.datetime.today().month) + "월 " + str(datetime.datetime.today().day) + "일 " + str(datetime.datetime.today().hour) + "시 " + str(datetime.datetime.today().minute) + "분 " + str(datetime.datetime.today().second) + "초에 명령어를 실행했습니다!")
        print("----------\nid : " + str(message.author.id) + " | name,tag : " + str(message.author)  + "\nserver id : " + str(message.guild.id) + " | server name : " + str(message.guild) + "\nchannel id : " + str(message.channel.id) + " | channel name : " + str(message.channel) + "\nmessage id : " + str(message.id) + "\nLink : https://discordapp.com/channels/" + str(message.guild.id) + "/" + str(message.channel.id) + "/" + str(message.id) + "/")            
# /도움말
#    if message.content.startswith("/도움말"):
#        embed = discord.Embed(color=0x819FF7)
#        embed.add_field(name=str(client.user), value="----------\n안녕하세요! 현츼봇입니다.\n 현츼봇의 기본 명령어는 / 입니다.\n----------\n명령어 음악관련\n/p 노래제목 - 노래제목의 노래는 틉니다.\n/s - 재생 중인 노래를 넘깁니다.\n/q - 현재 재생 준비중인 노래 목록을 띄웁니다.\n/j - 저를 통화방으로 소환시킵니다.\n/l - 저를 통화방에서 강퇴시킵니다. ㅠㅠ\n----------\n채팅 명령어\n/청소 갯수 - 갯수만큼의 채팅을 제가 쓱-싹 합니다.", inline=True)
#        embed.set_footer(text=message.author, icon_url=message.author.avatar_url)
#        await message.channel.send(embed=embed)

# !은바천보
    if message.content.startswith("!은바천보"):
        if message.author.guild_permissions.manage_messages:
            try:
                async def send_dm(ctx, user_name: discord.Member):
                channel = await user_name.create_dm()
                await channel.send("현재 시간으로 부터 24시간이 지날 때 마다 은바천보! 를 해당 채널에 씁니다 !")
                while True:
                    await message.channel.send("은바천보!")
                    await asyncio.sleep(60*60*24)
            else:
                await message.channel.send("권한이 없습니다.")

access_token = os.environ['BOT_TOKEN']
client.run(access_token)
# 봇 토큰
