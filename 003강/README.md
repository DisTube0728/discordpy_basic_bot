<h1 align="center">Discord.py 3강에 오신것을 환영해요!</h1>

> [디스코드](https://discord.gg/7npaMJf), [사이트](https://devht.xyz/), [이메일](mailto:samsunghappytree123@naver.com)

## 강의 제작자
**Mail : [samsunghappytree123@naver.com](mailto:samsunghappytree123@naver.com)), Discord : [Happytree Samsung#7612](https://discord.com/users/726350177601978438)**
> **무단 도용 금지. 이 강의를 따라할때는 상관 없지만, 강의를 배껴가는것은 출처를 남겨주세요.**
> **저작권은 삼성해피트리에게 있습니다. 문의는 [samsunghappytree123@naver.com](mailto:samsunghappytree123@naver.com)으로 해주세요.**
------------

## 2강은 기본 코딩 강의입니다!
> [블로그 강의 바로가기](https://blog.naver.com/samsunghappytree123/221943095076)

> [유튜브 강의 바로가기](https://youtu.be/H1PZrv8Kees)

------------

## 기본 코딩에는 다양한 파일이 있어요!
### 파일 순차는 아래와 같아요!
순서대로 보시는것을 추천드립니다!
+ [임베드](#임베드)

------------

## Discord.py 봇 강의를 보기 전 참고해주세요!
+ 단순하게 따라하려고 하지 마시고, 원리를 파악해보세요.
+ 궁금한점은 구글링을 해보신 후, [봇 강의 서버](https://discord.gg/7npaMJf)에서 말씀해주세요.
+ 오타 또는 오류는 깃허브 이슈로 생성해주세요.

------------

### 임베드

임베드는 무엇일까요?

바로 링크를 올릴 때 뜨는건데요, 한번 우리는 해보면 좋겠죠?

**전체코드는 [main.py](main.py) 파일을 확인해주세요.**

```py
embed = discord.Embed(timestamp=message.created_at, colour=discord.Colour.red(), title="제-목", description="설-명")
```
이렇게해서 보내면 아주 기본적이게 타이틀은 "제-목", 설명은 "설-명"이라고 보내지는 간단한 코드입니다.

```py
embed.set_thumbnail(url="https://prforest.ga/files/img/홍보숲.png")
```
이걸 붙이면 썸네일이 추가되겠죠?

```py
embed.set_image(url="https://postfiles.pstatic.net/MjAyMDA1MTVfNTcg/MDAxNTg5NTI0NzU1Nzcx.uK7HkqM-NEgBHLafECr0IfeftNM2RfmrkM-oq8q5KA0g.ZruZd3GTvpc2v-ei-PdJKxFleQMvLDUCNeoHSEGR8bMg.PNG.samsunghappytree123/%EA%B0%95%EC%9D%982.PNG?type=w773")
```
이거는 "사진을 추가" 해주는 것입니다.

사진을 추가하여 소개가 가능해요!

```py
embed.add_field(name="필트 제목", value="필드 설명", inline=False) #inline이 False라면 다음줄로 넘깁니다.
```
이 것은 "도움말" 처럼 불리는 것이랍니다!

필드라고도 하죠

```py
embed.set_footer(text=message.author, icon_url=message.author.avatar_url)
```
이건 푸터라고 해요!

------------

강의를 봐 주셔서 감사해요! 4강에서 뵙겠습니다!
