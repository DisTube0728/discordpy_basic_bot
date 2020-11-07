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
    if message.content == "ㅎㅇ": #만일 사용자가 "야" 라고 입력했을때
        await message.channel.send("ㅂㅇ") #봇이 "왜" 라고 답한다.
    
    if message.content == "임베드내놔":
        embed = discord.Embed(timestamp=message.created_at, colour=discord.Colour.red(), title="제-목", description="설-명")
        embed.set_thumbnail(url="https://prforest.ga/files/img/홍보숲.png")
        embed.set_image(url="https://postfiles.pstatic.net/MjAyMDA1MTVfNTcg/MDAxNTg5NTI0NzU1Nzcx.uK7HkqM-NEgBHLafECr0IfeftNM2RfmrkM-oq8q5KA0g.ZruZd3GTvpc2v-ei-PdJKxFleQMvLDUCNeoHSEGR8bMg.PNG.samsunghappytree123/%EA%B0%95%EC%9D%982.PNG?type=w773")
        embed.set_footer(text=message.author, icon_url=message.author.avatar_url)
        embed.add_field(name="필트 제목", value="필드 설명", inline=False) #inline이 False라면 다음줄로 넘깁니다.
        await message.channel.send(embed=embed)

client.run(token)