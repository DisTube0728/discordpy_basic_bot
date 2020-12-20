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
    if message.content.startswith("!청소"):
        number = int(message.content.split(" ")[1])
        await message.delete()
        await message.channel.purge(limit=number)
        await message.channel.send(f"{number}개의 메세지 삭제 완료!")

client.run(token) #token으로 봇을 실행한다