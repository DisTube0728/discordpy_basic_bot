import discord, datetime #discord, datetime 모듈 불러오기
token = '님들의 토큰' #token 변수 설정
intents = discord.Intents.all() #인텐트 설정
client = discord.Client(intents=intents) #client 설정

@client.event
async def on_ready(): #준비되었을때
    print('로그인되었습니다!')
    print(client.user.name)
    print(client.user.id)
    print('====================================')

@client.event
async def on_message():
    if message.content.startswith("!추방"):
        member = message.guild.get_member(int(message.content.split(" ")[1]))
        await message.guild.kick(member, reason=' '.join(message.content.split(" ")[2:]))

    if message.content.startswith("!차단"):
        member = message.guild.get_member(int(message.content.split(" ")[1]))
        await message.guild.ban(member, reason=' '.join(message.content.split(" ")[2:]))

client.run(token) #token으로 봇을 실행한다