<h1 align="center">Discord.py 10강에 오신것을 환영해요!</h1>

> [디스코드](https://discord.gg/7npaMJf), [사이트](https://happytree.cf/), [이메일](mailto:samsunghappytree123@naver.com)

## 강의 제작자
**Mail : [samsunghappytree123@naver.com](mailto:samsunghappytree123@naver.com)), Discord : [Happytree Samsung#7612](https://discord.com/users/726350177601978438)**
> **무단 도용 금지. 이 강의를 따라할때는 상관 없지만, 강의를 배껴가는것은 출처를 남겨주세요.**
> **저작권은 삼성해피트리에게 있습니다. 문의는 [samsunghappytree123@naver.com](mailto:samsunghappytree123@naver.com)으로 해주세요.**
------------

## 10강에는 **메세지 청소** 기능을 알려드립니다!
> [10강 바로가기](https://blog.naver.com/samsunghappytree123/222179498988)

> [유튜브 강의 바로가기](https://youtu.be/Aq3Cy1sNFiU)

------------

## 해당 강의는 다음과 같은 목차가 있습니다.
### 목차는 아래와 같아요!
순서대로 보시는것을 추천드립니다!
+ [메세지 청소하기](#메세지-청소하기)

------------

## Discord.py 봇 강의를 보기 전 참고해주세요!
+ 단순하게 따라하려고 하지 마시고, 원리를 파악해보세요.
+ 궁금한점은 구글링을 해보신 후, [봇 강의 서버](https://discord.gg/7npaMJf)에서 말씀해주세요.
+ 오타 또는 오류는 깃허브 이슈로 생성해주세요.

------------

### 메세지 청소하기
오늘 준비할 것은 메세지가 너무 더러워서 청소가 필요한 채널과 비쥬얼 스튜디오 코드, 그리고 자신의 멘탈이 필요합니다!

오늘도 어김없이 vsc를 켜주시고, 아래의 코드를 입력해봅시다!

```py
if message.content.startswith("!청소"):
```
![코드 1](https://postfiles.pstatic.net/MjAyMDEyMjBfMjcz/MDAxNjA4NDI2MjE5Njgx.hUP8MUPTwFWjX3C1sfvAlC5czRAwm-CNhRsmwzlgy6Eg._v5cRg4BSOwWWuvwC6orWhrX5RZ3fjl4GEpqHQlxgLog.PNG.samsunghappytree123/image.png?type=w773)

오늘은 message.content가 아닌, message.content.startswith를 사용합니다.

startswith는 `!청소 <1>` 명령어를 사용해도 알아듣지만 message.content를 사용할 시에는 알아듣지 못합니다.

그 아래줄에는 number 변수를 정하는데요!

![number 변수 정하기](https://postfiles.pstatic.net/MjAyMDEyMjBfMTYw/MDAxNjA4NDI2MzY5MTM5.TJweQ-yJxlMrPpLs7PwrNYArssFH83fy4S30AbkzoDQg.1RHM01IWqxBS0jvm9mcpsKRihxozjnWJlLMgSWJGu-sg.PNG.samsunghappytree123/image.png?type=w773)

Q. 저번 강의에서는 message.content[10:]이런식으로 하셨는데 왜 바꾸셨는지요?

A. message.content[10:] 같은것은 명령어가 바뀌면 숫자를 계속 바꾸어야 하는 데 반해서, message.content.split(" ")[1]은 항상 고정입니다.

![split 알기](https://cdn.discordapp.com/attachments/764768769205075968/790133218040217620/unknown.png)

!청소라는 말과 1234라는 말이 다르게 인식되어, 유용합니다.

여튼 다시 와서, 아래의 3개 문구를 적용해봅시다.

![구문 쓰기](https://postfiles.pstatic.net/MjAyMDEyMjBfMjY2/MDAxNjA4NDI2NzYxNzE5.lLC0K-qZ5OU4y90QPwVbbGhW0f6I32c85FoNnpPx-oIg.6ZNkemEX9txLCSBIbdznD1hGeOtufcriuhvnQlgUvEUg.PNG.samsunghappytree123/image.png?type=w773)

1. 메세지를 삭제하고
2. purge라는 것으로 대량 메세지를 삭제하고 (limit이 넘버 (삭제할 수)입니다.)
3. 메세지 채널에 삭제 완료라고 알려줍니다.
​

오늘은 아래의 유튜브 영상에 사용 장면 넣어놓겠습니다!

감사합니다.

------------

강의를 봐 주셔서 감사해요! 11강에서 뵙겠습니다!