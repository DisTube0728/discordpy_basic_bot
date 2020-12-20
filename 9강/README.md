<h1 align="center">Discord.py 9강에 오신것을 환영해요!</h1>

> [디스코드](https://discord.gg/7npaMJf), [사이트](https://happytree.cf/), [이메일](mailto:samsunghappytree123@naver.com)

## 강의 제작자
**Mail : [samsunghappytree123@naver.com](mailto:samsunghappytree123@naver.com)), Discord : [Happytree Samsung#7612](https://discord.com/users/726350177601978438)**
> **무단 도용 금지. 이 강의를 따라할때는 상관 없지만, 강의를 배껴가는것은 출처를 남겨주세요.**
> **저작권은 삼성해피트리에게 있습니다. 문의는 [samsunghappytree123@naver.com](mailto:samsunghappytree123@naver.com)으로 해주세요.**
------------

## 9강은 랜덤 및 타이머를 알려드립니다!
> [9강 바로가기](https://blog.naver.com/samsunghappytree123/222004944456)

> [유튜브 강의 바로가기](https://youtu.be/5ocui195iV4)

------------

## 해당 강의는 다음과 같은 목차가 있습니다.
### 목차는 아래와 같아요!
순서대로 보시는것을 추천드립니다!
+ [랜덤 기능](#랜덤-기능)
+ [타이머 기능](#타이머-기능)

------------

## Discord.py 봇 강의를 보기 전 참고해주세요!
+ 단순하게 따라하려고 하지 마시고, 원리를 파악해보세요.
+ 궁금한점은 구글링을 해보신 후, [봇 강의 서버](https://discord.gg/7npaMJf)에서 말씀해주세요.
+ 오타 또는 오류는 깃허브 이슈로 생성해주세요.

------------

### 랜덤 기능
먼저 cmd에서 "pip install asyncio", "pip install random"을 설치해줍니다.
[참고링크](https://github.com/samsunghappytree123/discordpy-bot/tree/master/1%EA%B0%95#%EB%AA%A8%EB%93%88-%EC%84%A4%EC%B9%98%ED%95%98%EA%B8%B0)

저번까지 사용했던 파일을 열어서 아래와 같은 구문을 입력해줍니다.
```py
import asyncio
import random
```

![구문 넣기](https://postfiles.pstatic.net/MjAyMDA2MThfODIg/MDAxNTkyNDY0MTIwNjU5.b5L85XG2loUOQhe_ZjQgLI7oCyKf1oGS-mtBooX0uTkg.DVOWwzpcKkOn-DLDzwUiv35j249XmpPiTOmQdd29cj0g.PNG.samsunghappytree123/%EA%B0%95%EC%9D%981.PNG?type=w773)

먼저 랜덤을 해보겠습니다!

1~10을 랜덤으로 선택해볼께요!

```py
if message.content == "선택":
    await message.channel.send(random.randint(1, 10))
```

이렇게 코드를 작성 후 실행해주시면...

![실행 결과](https://postfiles.pstatic.net/MjAyMDA2MThfMTgw/MDAxNTkyNDY0NjkwOTc5.EUrBUAQ4BaFp8VBqcirFp945HE4zgI_vN17fooUBvIgg.4FVn_6keKUBl-W8KSqy-TDUarkl74WxCDsDnhJiWNkEg.PNG.samsunghappytree123/%EA%B0%95%EC%9D%982.PNG?type=w773)

1~10까지 랜덤으로 골라드립니다! ~~복권~~

### 타이머 기능
asyncio를 사용할껀데요, time이라는 모듈을 쓸수 있습니다!

하지만 time을 쓰면 다른명령어는 못하기 때문에 asyncio를 쓰는게 좋아요!

이건 단순합니다.

```py
if message.content == "타이머":
    await asyncio.sleep(10)
    await message.channel.send(f"{message.author.mention}님 10초가 지났어요!")
```

![실행 결과](https://postfiles.pstatic.net/MjAyMDA2MThfMjc0/MDAxNTkyNDY0OTQxODM4.SRwq6ejCmqMbtThYKQvLK3MXASCd1s_t4ymHHmXcgwcg.Slwm-kt---0x-CQ-aIskPaZhMUVimJNfstuZrZFcz5wg.PNG.samsunghappytree123/%EA%B0%95%EC%9D%983.PNG?type=w773)

10초가 지나서 알려줍니다!

------------

강의를 봐 주셔서 감사해요! 10강에서 뵙겠습니다!