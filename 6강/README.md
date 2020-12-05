<h1 align="center">Discord.py 6강에 오신것을 환영해요!</h1>

> [디스코드](https://discord.gg/7npaMJf), [사이트](https://happytree.cf/), [이메일](mailto:samsunghappytree123@naver.com)

## 강의 제작자
**Mail : [samsunghappytree123@naver.com](mailto:samsunghappytree123@naver.com)), Discord : [Happytree Samsung#7612](https://discord.com/users/726350177601978438)**
> **무단 도용 금지. 이 강의를 따라할때는 상관 없지만, 강의를 배껴가는것은 출처를 남겨주세요.**
> **저작권은 삼성해피트리에게 있습니다. 문의는 [samsunghappytree123@naver.com](mailto:samsunghappytree123@naver.com)으로 해주세요.**
------------

## 6강에서는 f-string을 알아볼꺼에요!
> [5강 바로가기](https://blog.naver.com/samsunghappytree123/221976607052)

> [유튜브 강의 바로가기](https://youtu.be/QeqdBxp-dk4)

------------

## f-string에는 다양한 파일이 있어요!
### 파일 순차는 아래와 같아요!
순서대로 보시는것을 추천드립니다!
+ [f-string](#f-string)
    + [f-string이란?][#f-string이란]
    + [f-string을 사용하지 않을 때](#f-string을-사용하지-않을-때)
    + [f-string을 사용할 때](#f-string을-사용할-때)

------------

## Discord.py 봇 강의를 보기 전 참고해주세요!
+ 단순하게 따라하려고 하지 마시고, 원리를 파악해보세요.
+ 궁금한점은 구글링을 해보신 후, [봇 강의 서버](https://discord.gg/7npaMJf)에서 말씀해주세요.
+ 오타 또는 오류는 깃허브 이슈로 생성해주세요.

------------

### f-string

#### f-string이란?
f-string이란 뭘까요?

코드를 단축시켜주는 역할을 합니다.

#### f-string을 사용하지 않을 때
f-string을 사용하지 않으면 이렇게 코드를 짜야합니다.
```py
await message.channel.send(message.author + "님")
```

ㅗㅜㅑ 변수를 많이 써야 하는거라면 마니 힘들겠죠 ㅠㅠ

![img](https://postfiles.pstatic.net/MjAyMDA1MjRfMjgg/MDAxNTkwMjk1ODk5MzM3.fwt9C-neZHZA5uMwRTRwQs_TSrzFL4iEjYoVoXo7_xwg.GgYoqrVp3wUPCEkaivJxuSFM7WguIoIVvKdLe13TAA0g.PNG.samsunghappytree123/%EA%B0%95%EC%9D%981.PNG?type=w773)

저번에 했던 코드만 반복해도 이렇습니다.

`message.author + "님입니다. ID : " + user.id` 힘들죠....

일단 저 코드를 실행해보면... 저 코드는 잘 안됩니다....

하지만 f-string은 할 수 있습니다!

#### f-string을 사용할 때
```py
await message.channel.send(f"{message.author}님입니다.")
```
자유자재로 `{}` 안에 변수를 넣으면서 사용이 가능합니다.

![img](https://postfiles.pstatic.net/MjAyMDA1MjRfMjQ3/MDAxNTkwMjk2Mjc0NTE4.FGiDYDI5zwrfsoZEsWTAzv2F7RFYB0apQklQnU34H8Mg.zNCB4hTbadApQT6GV6Yy22tAUAyxnnc2YSz_XHTwsiAg.PNG.samsunghappytree123/%EA%B0%95%EC%9D%982.PNG?type=w773)

이렇게 써봤는데 실행해보면 아래와 같이 나오네요!

![img](https://postfiles.pstatic.net/MjAyMDA1MjRfMjg1/MDAxNTkwMjk2MjkyODYz.tbHXAoHkMcIEFYdKKXEaSfsfZGUhVoZ93btp97NxNq0g.-3Mg3QLaqSduTVmok6-KndFxxdYqPNVZlQtcrCRFP3wg.PNG.samsunghappytree123/%EA%B0%95%EC%9D%983.PNG?type=w773)

제 이름이 잘 나오군요!

그러면 우리 모두 f-string을 사용해봅시다!

도전과제는 f-string을 사용해서 자신의 이름을 출력하는것입니다.

모두 f-string을 사용해보세요!

------------

강의를 봐 주셔서 감사해요! 7강에서 뵙겠습니다!
