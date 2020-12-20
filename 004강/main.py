import discord #discord 모듈 불러오기
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
    if message.content == '임베드출력':
        embed=discord.Embed(color=0xff00, title="제목", description="설명", timestamp=message.created_at) #embed라는 변수를 지정한다, 색깔을 0xff00, 제목을 "제목", 내용을 "설명" 이라고 지정한다.
        embed.set_footer(text=message.author, icon_url=message.author.avatar_url) #embed 변수의 footer를 설정한다, 글을 메세지를 입력한 사람의 태그로 지정하고 아이콘을 메세지를 입력한 사람의 아바타 (프로필 사진) 으로 지정한다.
        embed.set_image(url="https://cdn.discordapp.com/avatars/652509076055523338/149b30c01677f61d587e8d199256442d.png?size=1024") #embed에서 이미지를 url로 정한다.
        embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/652509076055523338/149b30c01677f61d587e8d199256442d.png?size=1024") #embed에서 썸네일을 url로 정한다.
        embed.add_field(name = '필드 이름', value = '필드 값') #필드를 정한다. 이름 : name 값, 내용 : value값
        await message.channel.send(embed=embed) #메세지를 입력한 채널에 embed를 보낸다.

client.run(token) #token으로 봇을 실행한다
