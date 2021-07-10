<h1 align="center">Discord.py 13강에 오신것을 환영해요!</h1>

> [디스코드](https://discord.gg/7npaMJf), [사이트](https://devht.xyz/), [이메일](mailto:samsunghappytree123@naver.com)

## 강의 제작자
**Mail : [samsunghappytree123@naver.com](mailto:samsunghappytree123@naver.com)), Discord : [Happytree Samsung#7612](https://discord.com/users/726350177601978438)**
> **무단 도용 금지. 이 강의를 따라할때는 상관 없지만, 강의를 배껴가는것은 출처를 남겨주세요.**
> **저작권은 삼성해피트리에게 있습니다. 문의는 [samsunghappytree123@naver.com](mailto:samsunghappytree123@naver.com)으로 해주세요.**
------------

## 13강에는 멤버를 추방 또는 차단하는 명령어를 제작합니다.
> [13강 바로가기](https://blog.naver.com/samsunghappytree123/222250426428)

> [유튜브 강의 바로가기](https://youtu.be/ZlhayiZz_OI)

------------

## 해당 강의는 다음과 같은 목차가 있습니다.
### 목차는 아래와 같아요!
순서대로 보시는것을 추천드립니다!
+ [.join이란?](#join이란)
+ [멤버 추방하기](#멤버-추방하기)
+ [멤버 차단하기](#멤버-차단하기)
+ [결과](#결과)

------------

## Discord.py 봇 강의를 보기 전 참고해주세요!
+ 단순하게 따라하려고 하지 마시고, 원리를 파악해보세요.
+ 궁금한점은 구글링을 해보신 후, [봇 강의 서버](https://discord.gg/7npaMJf)에서 말씀해주세요.
+ 오타 또는 오류는 깃허브 이슈로 생성해주세요.

------------

### .join이란?
+ [**자세한 내용은 여기를 참고해주세요!**](https://dojang.io/mod/page/view.php?id=2299)

### 멤버 추방하기
일단 VSC를 켜시고, 코드의 기본을 잡아줍니다.
```py
if message.content.startswith("!추방"):
```
``!추방 ~~~``를 하면 실행합니다.

```py
member = message.guild.get_member(int(message.content.split(" ")[1]))
```
member를 **해당 서버에 있는** ``메세지 내용의 띄어쓰기의 2번째 ID의 멤버로 지정``합니다.

> [**split는 아래의 강의에서 다시 확인해보실 수 있습니다.**](https://blog.naver.com/samsunghappytree123/222179498988)

그리고 이제 메인 코드! 추방을 하는 구문입니다.

```py
await message.guild.kick(member, reason=' '.join(message.content.split(" ")[2:]))
```
멤버를 member, 이유를 메세지 내용의 띄어쓰기 3번째부터로 지정하여 추방합니다.

### 멤버 차단하기
멤버 차단하기는 하나의 구문만 변경하면 가능해요!
```py
await message.guild.ban(member, reason=' '.join(message.content.split(" ")[2:]))
```
뭐가 달라졌을까요?

그렇습니다. kick이 ban으로 바뀐거에요!

### 결과
결과는 [유튜브 영상](https://youtu.be/ZlhayiZz_OI)으로 확인해주세요!

------------

강의를 봐 주셔서 감사해요! discord.ext 강의에서 다시 만나요!