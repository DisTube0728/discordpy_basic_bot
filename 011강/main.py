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

client.run(token) #token으로 봇을 실행한다