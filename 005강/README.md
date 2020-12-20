<h1 align="center">Discord.py 5강에 오신것을 환영해요!</h1>

> [디스코드](https://discord.gg/7npaMJf), [사이트](https://happytree.cf/), [이메일](mailto:samsunghappytree123@naver.com)

## 강의 제작자
**Mail : [samsunghappytree123@naver.com](mailto:samsunghappytree123@naver.com)), Discord : [Happytree Samsung#7612](https://discord.com/users/726350177601978438)**
> **무단 도용 금지. 이 강의를 따라할때는 상관 없지만, 강의를 배껴가는것은 출처를 남겨주세요.**
> **저작권은 삼성해피트리에게 있습니다. 문의는 [samsunghappytree123@naver.com](mailto:samsunghappytree123@naver.com)으로 해주세요.**
------------

## 5강은 유저정보를 조회해보는 강의입니다!
> [5강 바로가기](https://blog.naver.com/samsunghappytree123/221975621791)

> [유튜브 강의 바로가기](https://youtu.be/nojv_BYKYE8)

------------

## 임베드 심화에는 다양한 파일이 있어요!
### 파일 순차는 아래와 같아요!
순서대로 보시는것을 추천드립니다!
+ [유저정보](#유저정보)

------------

## Discord.py 봇 강의를 보기 전 참고해주세요!
+ 단순하게 따라하려고 하지 마시고, 원리를 파악해보세요.
+ 궁금한점은 구글링을 해보신 후, [봇 강의 서버](https://discord.gg/7npaMJf)에서 말씀해주세요.
+ 오타 또는 오류는 깃허브 이슈로 생성해주세요.

------------

### 유저정보
일단 파일을 열어줍시다.

![img](https://postfiles.pstatic.net/MjAyMDA1MjNfMjk5/MDAxNTkwMjE1MzQ3Njgy.TvYEcrECWXK0h8sIZfa5pB11u65I0Hh4uiVR12CAv-wg.zLjjqPidjYsocqwvc-LZWTlgpmcE1XRoazazTMWX81Mg.PNG.samsunghappytree123/%EA%B0%95%EC%9D%981.PNG?type=w773)

⚠ 또한 오늘은 새로운 모듈인, **__datetime__** 모듈이 필요합니다.
> 모듈을 설치하기 위해서, [1강의 모듈 설치 강의](https://github.com/DisTube-Official/python-discord-bot/tree/master/1%EA%B0%95#%EB%AA%A8%EB%93%88-%EC%84%A4%EC%B9%98%ED%95%98%EA%B8%B0)부분을 다시 확인해주세요.
명령어는 `pip install datetime` 입니다.

원래 쓰던데로 

```py
if message.content == '내정보':
```
를 써줍시다.

변수를 지정해봅시다!

```py
user = message.author
```
user 변수를 메세지를 입력한 사람으로 정합니다.

```py
date = datetime.datetime.utcfromtimestamp(((int(user.id) >> 22) + 1420070400000) / 1000)
```
date 변수를 user의 가입일로 정합니다.

​

그럼 이제 전에 했던 임베드를 응용해서 만드시면 되겠습니다 (??)

아래는 유저정보 관련 변수입니다.

| 변수              | 해석                            | 예시              |
| ----------------- | ------------------------------ | ----------------- |
| user              | 메세지를 보낸 유저의 태그        | 삼성해피트리#0957  |
| user.name         | 메세지를 보낸 유저의 이름        | 삼성해피트리       |
| user.avatar_url   | 메세지를 보낸 유저의 아바타 url  | [여기](https://cdn.discordapp.com/avatars/726350177601978438/5396b475708759a552d0fd79f92211e1.webp?size=1024)를 확인하세요.|
| user.display_name | 메세지를 보낸 유저의 닉네임      | STAFF 삼성해피트리 |
| str(date.year)    | 메세지를 보낸 유저의 가입연도    | 2019              |
| str(date.month)   | 메세지를 보낸 유저의 가입한 달   | 12                |
| str(date.day)     | 메세지를 보낸 유저의 가입일      | 8                 |

------------

강의를 봐 주셔서 감사해요! 6강에서 뵙겠습니다!
