<h1 align="center">Discord.py 11강에 오신것을 환영해요!</h1>

> [디스코드](https://discord.gg/7npaMJf), [사이트](https://devht.xyz/), [이메일](mailto:samsunghappytree123@naver.com)

## 강의 제작자
**Mail : [samsunghappytree123@naver.com](mailto:samsunghappytree123@naver.com)), Discord : [Happytree Samsung#7612](https://discord.com/users/726350177601978438)**
> **무단 도용 금지. 이 강의를 따라할때는 상관 없지만, 강의를 배껴가는것은 출처를 남겨주세요.**
> **저작권은 삼성해피트리에게 있습니다. 문의는 [samsunghappytree123@naver.com](mailto:samsunghappytree123@naver.com)으로 해주세요.**
------------

## 11강에는 이슈가 되었던, **인텐트 켜기**를 알려드리겠습니다!
> [11강 바로가기](https://blog.naver.com/samsunghappytree123/222191516077)

> [유튜브 강의 바로가기](https://youtu.be/UsK7nuW3M5s)

------------

## 해당 강의는 다음과 같은 목차가 있습니다.
### 목차는 아래와 같아요!
순서대로 보시는것을 추천드립니다!
+ [인텐트 켜기](#인텐트-켜기)

------------

## Discord.py 봇 강의를 보기 전 참고해주세요!
+ 단순하게 따라하려고 하지 마시고, 원리를 파악해보세요.
+ 궁금한점은 구글링을 해보신 후, [봇 강의 서버](https://discord.gg/7npaMJf)에서 말씀해주세요.
+ 오타 또는 오류는 깃허브 이슈로 생성해주세요.

------------

### 인텐트 켜기
사실 인텐트를 켜는 법은 간단합니다.

먼저 [Discord Developer Portal](https://discord.com/developers)에 있는 자신의 봇 페이지에 들어가주세요.

![이미지](https://postfiles.pstatic.net/MjAyMDEyMzFfMTAg/MDAxNjA5MzkyOTE1NDMz.Dc3WOGwAWT7k-Vy6gR4qd8dwPWoc4946eva96pKkooEg.zyYlrWIn4gG0t4cUVSdAVF8VexX_9Otc2_wlCZBvlAMg.JPEG.samsunghappytree123/1.jpg?type=w773)
![이미지](https://postfiles.pstatic.net/MjAyMDEyMzFfMjk5/MDAxNjA5MzkyOTY4NzAy.IOgANzWn-Nx6HTwXifbbq8R5gNW5OjWkz_6uBacF804g.vu2Z-2mOsWxdZwxLzvCMHWu5U9hNwJ3SNrbx8m06ZsUg.JPEG.samsunghappytree123/2.jpg?type=w773)

그 다음으로 봇 설정을 하셔야 합니다!

![이미지](https://postfiles.pstatic.net/MjAyMDEyMzFfNTgg/MDAxNjA5MzkyOTY4ODQ2.iDfVK2jTi34oa5WFaURss-wscJgFVn0FlCrtbHU7gccg.rYX0D0762cXyXaKUCbiMn5PNWGRGQ7MzMnfHe9lwmZwg.JPEG.samsunghappytree123/3.jpg?type=w773)

원래 밑으로 내리면 이렇게 꺼져 있을 것인데요!

![이미지](https://postfiles.pstatic.net/MjAyMDEyMzFfMjg3/MDAxNjA5MzkyOTY4ODgw.HWd95FiHKce94o2HgSVIQ3YfamDyYzySMO8vof3eVXkg.s_m1tb22X-Uyf-vFOZO1_Q2k9I5MJyyhRfFHqXcSMrEg.JPEG.samsunghappytree123/4.jpg?type=w773)

여기 있는 것(Privileged Gateway Intents)를 다 켜주세요!

|인텐트 이름|인텐트 주요 기능|
|:---:|:---:|
|PRESENCE INTENT|유저의 상태 불러오기|
|SERVER MEMBERS INTENT|서버의 멤버 불러오기|

이제 아래의 **Save Changes를 눌러 저장해주세요.** (저장 안하시는 분들이 간혹 있으시더라고요.)

다음으로 VSC로 들어가셔서 구문을 수정해줍니다.

```py
import discord, asyncio
client = discord.Client()
```

이런 식으로 되어 있으실 건데요 (import는 무슨 모듈을 임포트하든 관계없습니다.)

이 구문을 아래와 같이 바꿔줍니다.

```py
import discord, asyncio
intents = discord.Intents.all()
client = discord.Client(intents=intents)
```

모든 인텐트를 켜 주라고 Client에 명령하는(?) 그런 구문입니다.

그리고 저장 후 실행하시면 정상적으로 완료가 된 것입니다!

------------

강의를 봐 주셔서 감사해요! 12강에서 뵙겠습니다!