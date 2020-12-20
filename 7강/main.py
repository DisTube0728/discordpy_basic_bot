import discord, datetime #discord, datetime 모듈 불러오기
from Dtime import Uptime
token = '님들의 토큰' #token 변수 설정
client = discord.Client() #client 설정
Uptime.uptimeset()

@client.event
async def on_ready(): #준비되었을때
    print('로그인되었습니다!')
    print(client.user.name)
    print(client.user.id)
    print('====================================')

@client.event
async def on_message(message): #메세지를 보냈을때
    if message.content == '!업타임': # 사용자가 '!업타임' 이라고 입력하면
        uptime = str(Uptime.uptime()).split(":") # uptime을 나눈다. (':' 기준)
        hours = uptime[0] # hours를 uptime에서 나눈 것 중 0번째 (':' 기준)로 정한다.
        minitues = uptime[1] # minitues를 uptime에서 나눈 것 중 1번째 (':' 기준)로 정한다.
        seconds = uptime[2].split(".")[0] # seconds를 uptime에서 나눈 것 중 2번째 (':' 기준), 56.에서 .을 뺀 나머지 수로 정한다.
        await message.channel.send(f"{hours}시간 {minitues}분 {seconds}초") # 메세지를 보냈던 채널에 "{hours}시간 {minitues}분 {seconds}초"라고 보낸다.

client.run(token) #token으로 봇을 실행한다