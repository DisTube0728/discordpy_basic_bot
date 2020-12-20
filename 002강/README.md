<h1 align="center">Discord.py 2강에 오신것을 환영해요!</h1>

> [디스코드](https://discord.gg/7npaMJf), [사이트](https://happytree.cf/), [이메일](mailto:samsunghappytree123@naver.com)

## 강의 제작자
**Mail : [samsunghappytree123@naver.com](mailto:samsunghappytree123@naver.com)), Discord : [Happytree Samsung#7612](https://discord.com/users/726350177601978438)**
> **무단 도용 금지. 이 강의를 따라할때는 상관 없지만, 강의를 배껴가는것은 출처를 남겨주세요.**
> **저작권은 삼성해피트리에게 있습니다. 문의는 [samsunghappytree123@naver.com](mailto:samsunghappytree123@naver.com)으로 해주세요.**
------------

## 2강은 기본 코딩 강의입니다!
> [블로그 강의 바로가기](https://blog.naver.com/samsunghappytree123/221943095076)

> [유튜브 강의 바로가기](https://youtu.be/sCypgEGbnfw)

------------

## 기본 코딩에는 다양한 파일이 있어요!
### 파일 순차는 아래와 같아요!
순서대로 보시는것을 추천드립니다!
+ [기본 코딩](#기본-코딩)
+ [코드 해석](#코드-해석)

------------

## Discord.py 봇 강의를 보기 전 참고해주세요!
+ 단순하게 따라하려고 하지 마시고, 원리를 파악해보세요.
+ 궁금한점은 구글링을 해보신 후, [봇 강의 서버](https://discord.gg/7npaMJf)에서 말씀해주세요.
+ 오타 또는 오류는 깃허브 이슈로 생성해주세요.

------------

### 기본 코딩
일단 전에 메모장에 복사했던 봇의 토큰을 가져와봅시다!

![tokenimg](https://postfiles.pstatic.net/MjAyMDA1MDNfMjM3/MDAxNTg4NDgxMzYxMDM0.XAEMouizVpTS-0Itjaq138hJnVn86VT6EkdqYmRfncgg.2ZV9qUfHKl8Uml7vaVyhSJgLSsp3YBohSLwyTFM2AMYg.PNG.samsunghappytree123/%EA%B0%95%EC%9D%9813.PNG?type=w773)

퀴즈! 저 토큰은 무엇을 의미한다고 했을까요?

바로 **봇을 실행하려고 할때 봇의 비밀번호** 라고 했었죠!

다시 말하지만 **노출은 절대 금지**합니다! 

그러면 전에 다운받았던 VSC (비쥬얼 스튜디오 코드)를 실행해봅시다!

![vsc1](https://postfiles.pstatic.net/MjAyMDA1MDNfOSAg/MDAxNTg4NDgyNDMzMjg3.0vcHBnRxZuwJ0R_KrgSPZ4tOeLs4ZNIiKGs48gFRib4g.4n5f95b2mQT_cMZu2ZOkL34m568WHgXoLkrBDI7dXBQg.JPEG.samsunghappytree123/%EA%B0%95%EC%9D%981.jpg?type=w773)

왼쪽 상단에 `File`을 누른 후 아래쪽 메뉴에 있는 `New File`을 클릭해서 새로운 파일을 생성해줍니다!

![vsc2](https://postfiles.pstatic.net/MjAyMDA1MDNfMTUg/MDAxNTg4NDgzNTQ5MzE4.6yEiZ9jl8Esrmxp0XGU5Ycq3TNn7DmOleOxBEACrT9Eg.M5EX0NzQQcMrquZZ72R82crdzySE1CarZFue6Dwxs30g.PNG.samsunghappytree123/%EA%B0%95%EC%9D%982.png?type=w773)

그러면 이런식으로 새로운 파일이 생성되는데요, 

Ctrl (컨트롤) + S를 눌러 저장을 해봅시다!

![vsc3](https://postfiles.pstatic.net/MjAyMDA1MDNfMjQ0/MDAxNTg4NDgzNzgyMjY4.1pRXoKROq2CIm1_KKaaN-mtDT2sBzSf5XzLV8HdZb_Mg.kdekqVh1sN6x3sJN5A4R1PqbFZTQnd5-InDuHwDPpuog.JPEG.samsunghappytree123/%EA%B0%95%EC%9D%983.jpg?type=w773)

원하는 경로에 파일을 저장합니다!

```
중요.
꼭 "파일 형식"을 Python으로 지정해야합니다! 이름은 알아서 하셔도 상관은 없습니다!
예) index.py
```

그리고 저장버튼을 누르시면 저장이 됩니다!

이제부터 기본 코딩을 해보도록 하겠습니다!

방식은 on_message 형식과 cogs 형식이 있습니다!

cogs 형식은 [여기](https://blog.naver.com/discord-bot)를 참고해주세요!

이제부터 코드를 따라해주세요 :)

```py
import discord
token = '님들의 토큰'
client = discord.Client()
@client.event
async def on_ready():
    print('로그인되었습니다!')
    print(client.user.name)
    print(client.user.id)
    print('====================================')

client.run(token)
```
위와 같은 코드를 실행해보면 아래와 같이 결과가 나옵니다!

![vsc4](https://postfiles.pstatic.net/MjAyMDA1MDNfMjI3/MDAxNTg4NDg0Mjk0MTQw.Ao7NucPD92JY15w6M-vJymboa1Xjyn2HsQA5PRDYIPwg.VysY-PMR4-lT1WxIvDczG4htImzumPiBi54gtE6DWY8g.JPEG.samsunghappytree123/%EA%B0%95%EC%9D%984.jpg?type=w773)

실행방법은 오른쪽 상단에 초록색 화살표를 누르시면 됩니다.

실행을 하니 로그인되었다고 뜹니다!

그러면 정상이죠!

한번 봇을 볼까요?

![vsc5](https://postfiles.pstatic.net/MjAyMDA1MDNfMTU4/MDAxNTg4NDg0MzkwMDU0.C2YUiJxSsuFhyeYgBQBOZxsKw6BPmrKMuhghSuzdACgg.27LcongVSF1fCOFUSqOCB8eGa68_vBnx3mJYs1pOHjcg.PNG.samsunghappytree123/%EA%B0%95%EC%9D%985.PNG?type=w773)

5! 봇이 켜졌네요!!

근데 명령어가 없기 때문에 답을 하지 않고 켜져있는 상태입니다!

이제 명령어를 실행할 코드를 만들어볼까요?

**print('====================================')와 client.run(token) 사이에 넣으세요**

```py
@client.event
async def on_message(message):
    if message.content == '핑':
        await message.channel.send('퐁!')
```
이 코드는 사람이 `핑` 이라고 말하면 봇이 `퐁!` 이라고 말하는 코드입니다!

![vsc6](https://postfiles.pstatic.net/MjAyMDA1MDNfMjgy/MDAxNTg4NDg0OTczNzYw.dEMShPfPfxfLdEKW9zzNECb5euXn0EQuaJtTq2r0FcQg.NoDT2rmLQzqflEsBq-Fu9npr8jiNKlpF23R-x72U-h0g.PNG.samsunghappytree123/%EA%B0%95%EC%9D%986.PNG?type=w773)

참 작동 잘하군요! 다른 글을 써서 다른 명령어를 만드실 수도 있습니다!

전체코드는 [main.py](main.py) 파일을 확인해주세요.

------------

### 코드 해석

`import discord`
- discord 모듈을 불러옵니다.

`token = '님들의 토큰'`
- token이라는 변수를 생성한다.

`client = discord.Client()`
- client를 지정한다. (봇이라는것을 지정한다.)

`@client.event`
- 클라이언트 이벤트 (일이 일어나는 것)

`async def on_ready():`
- 봇이 준비가 되었을때 다음을 실행한다.

`print('로그인되었습니다!')`
- 큰솔 창에 글을 띄운다.

`client.user.name`
- 봇의 이름이다.

`client.user.id`
- 봇의 아이디이다.

`async def on_message(message):`
- 만일 메세지를 썼을때 다음과 같은 행동을 한다

`if message.content == "야":`
- 만일 사용자가 "야" 라고 입력했을때

`await message.channel.send("왜")`
- 메세지를 입력했던 채널에 '왜' 이라고 보낸다.

`client.run(token)`
- 봇을 실행한다. (여기서 token은 변수를 말한다.)

------------

강의를 봐 주셔서 감사해요! 3강에서 뵙겠습니다!
