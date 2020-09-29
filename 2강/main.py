import discord #모듈 불러오기
token = "My Bot Token" #봇 토큰 설정하기
client = discord.Client() #client 설정하기

@client.event
async def on_ready(): #봇이 준비되었을때
    print("봇 준비 완료!")
    print(client.user)
    print("============================")

@client.event
async def on_message(message): #사용자가 메세지를 입력했을때
    if message.content == "야": #만일 사용자가 "야" 라고 입력했을때
        await message.channel.send("왜") #봇이 "왜" 라고 답한다.
    if message.content == "ㅎㅇ": #만일 사용자가 "ㅎㅇ" 라고 입력했을때
        await message.channel.send("ㅂㅇ") #봇이 "ㅂㅇ" 라고 답한다.

client.run(token)