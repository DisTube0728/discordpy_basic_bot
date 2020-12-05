import discord, datetime #discord, datetime 모듈 불러오기
token = '님들의 토큰' #token 변수 설정
client = discord.Client() #client 설정

@client.event
async def on_ready(): #준비되었을때
    print('로그인되었습니다!')
    print(client.user.name)
    print(client.user.id)
    print('====================================')

@client.event
async def on_message(message): #메세지를 보냈을때
    if message.content == '내정보':
        user = message.author
        date = datetime.datetime.utcfromtimestamp(((int(user.id) >> 22) + 1420070400000) / 1000)
        await message.channel.send(f"{user} / {user.name} / {str(date.year)}/{str(date.month)}/{str(date.day)}")

client.run(token) #token으로 봇을 실행한다