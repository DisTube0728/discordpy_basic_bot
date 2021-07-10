<h1 align="center">Discord.py 7강에 오신것을 환영해요!</h1>

> [디스코드](https://discord.gg/7npaMJf), [사이트](https://devht.xyz/), [이메일](mailto:samsunghappytree123@naver.com)

## 강의 제작자
**Mail : [samsunghappytree123@naver.com](mailto:samsunghappytree123@naver.com)), Discord : [Happytree Samsung#7612](https://discord.com/users/726350177601978438)**
> **무단 도용 금지. 이 강의를 따라할때는 상관 없지만, 강의를 배껴가는것은 출처를 남겨주세요.**
> **저작권은 삼성해피트리에게 있습니다. 문의는 [samsunghappytree123@naver.com](mailto:samsunghappytree123@naver.com)으로 해주세요.**
------------

## 7강은 "업타임"에 대해 알아볼 예정입니다~
> [7강 바로가기](https://blog.naver.com/samsunghappytree123/221981917651)

> [유튜브 강의 바로가기](https://youtu.be/8KEn_yTHwIs)

------------

## 업타임은 다음과 같은 목차가 있습니다.
### 목차는 아래와 같아요!
순서대로 보시는것을 추천드립니다!
+ [업타임 모듈 설치](#업타임-모듈-설치)
+ [업타임 코드 만들기](#업타임-코드-만들기)

------------

## Discord.py 봇 강의를 보기 전 참고해주세요!
+ 단순하게 따라하려고 하지 마시고, 원리를 파악해보세요.
+ 궁금한점은 구글링을 해보신 후, [봇 강의 서버](https://discord.gg/7npaMJf)에서 말씀해주세요.
+ 오타 또는 오류는 깃허브 이슈로 생성해주세요.

------------

### 업타임 모듈 설치
이 강의를 시작하기 전, 모듈을 설치하여야합니다. cmd에서 `pip install Dtime`을 입력해줍니다.

![업타임 모듈 설치](https://postfiles.pstatic.net/MjAyMDA1MjhfOTkg/MDAxNTkwNjQ4NDE0NjAy.ZFXJIxUBzh46Stkl6a9rbUlipbhpoyrNLoGQXGt6NdYg.TwMNpMBI6b1H_XdrwsQ7JIDvWXXKmgwnXCG6m0mgbu4g.PNG.samsunghappytree123/%EA%B0%95%EC%9D%982.PNG?type=w773)

### 업타임 코드 만들기
![vsc 코드](https://postfiles.pstatic.net/MjAyMDA1MjhfNTUg/MDAxNTkwNjQ4NjcyMTgy.xTQ8wFP0LNbeJZmCoWgzyqPmWct6OQR2iivOZWN6AH8g.E0rpYCPuNiolAZMu0JtEahHGKlUIq5CWfL_4G9aVDGwg.PNG.samsunghappytree123/%EA%B0%95%EC%9D%983.PNG?type=w773)

봇 파일을 실행하면 다음과 같이 나오게 됩니다.

그리고 Dtime 모듈을 임포트해봅시다!

import asyncio 아래쪽에 임포트해줍시다.

```py
from Dtime import Uptime
```

그런 후 'client = discord.Client()' 아랫줄에 다음과 같은 코드를 추가해줍니다.

```py
Uptime.uptimeset()
```

![위의 실행 코드](https://postfiles.pstatic.net/MjAyMDA1MjhfMTAw/MDAxNTkwNjQ5Mjg1MjAx.t7cy0dL4nbHbJERFqBuGDQFIO21Ox8TtglH8LBJ2lTkg.yLWu9FqOmG1Jrn1vJpKhgzgCvZnCZdL47A7ucDFHnOUg.PNG.samsunghappytree123/%EA%B0%95%EC%9D%984.PNG?type=w773)

모듈을 임포트했고, Uptime을 지정했습니다.

이게 끝이에요! 진짜입니다! 이제 코드만 짜주면 되요!

코드를 짜볼까요?

```py
if message.content == '!업타임': # 사용자가 '!업타임' 이라고 입력하면
    uptime = str(Uptime.uptime()).split(":") # uptime을 나눈다. (':' 기준)
    hours = uptime[0] # hours를 uptime에서 나눈 것 중 0번째 (':' 기준)로 정한다.
    minitues = uptime[1] # minitues를 uptime에서 나눈 것 중 1번째 (':' 기준)로 정한다.
    seconds = uptime[2].split(".")[0] # seconds를 uptime에서 나눈 것 중 2번째 (':' 기준), 56.에서 .을 뺀 나머지 수로 정한다.
    await message.channel.send(f"{hours}시간 {minitues}분 {seconds}초") # 메세지를 보냈던 채널에 "{hours}시간 {minitues}분 {seconds}초"라고 보낸다.
```

처음 보는 용어인 split도 있네요!

실행해보면 아주 잘 된다는 것을 볼 수 있습니다!

![실행 장면](https://postfiles.pstatic.net/MjAyMDA1MjhfNTIg/MDAxNTkwNjUxNTcxMDY2.dvAUPr_q599adxFlEUhoPDvDN68IwpeCVdwdzDYXuQEg.-r6zUl31sXcqPyFLy4zbUfPzaw5t9qiJhMQw22syNncg.PNG.samsunghappytree123/%EA%B0%95%EC%9D%985.PNG?type=w773)

------------

강의를 봐 주셔서 감사해요! 8강에서 뵙겠습니다!