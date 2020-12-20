<h1 align="center">Discord.py 4강에 오신것을 환영해요!</h1>

> [디스코드](https://discord.gg/7npaMJf), [사이트](https://happytree.cf/), [이메일](mailto:samsunghappytree123@naver.com)

## 강의 제작자
**Mail : [samsunghappytree123@naver.com](mailto:samsunghappytree123@naver.com)), Discord : [Happytree Samsung#7612](https://discord.com/users/726350177601978438)**
> **무단 도용 금지. 이 강의를 따라할때는 상관 없지만, 강의를 배껴가는것은 출처를 남겨주세요.**
> **저작권은 삼성해피트리에게 있습니다. 문의는 [samsunghappytree123@naver.com](mailto:samsunghappytree123@naver.com)으로 해주세요.**
------------

## 4강은 임베드 심화와 관련된 강의입니다!
> [4강 바로가기](https://blog.naver.com/samsunghappytree123/221964001137)

> [유튜브 강의 바로가기](https://youtu.be/K9KMigy6d8o)

------------

## 임베드 심화에는 다양한 파일이 있어요!
### 파일 순차는 아래와 같아요!
순서대로 보시는것을 추천드립니다!
+ [임베드 심화](#임베드-심화)

------------

## Discord.py 봇 강의를 보기 전 참고해주세요!
+ 단순하게 따라하려고 하지 마시고, 원리를 파악해보세요.
+ 궁금한점은 구글링을 해보신 후, [봇 강의 서버](https://discord.gg/7npaMJf)에서 말씀해주세요.
+ 오타 또는 오류는 깃허브 이슈로 생성해주세요.

------------

### 임베드 심화
일단 파일을 열어줍시다.

![img](https://postfiles.pstatic.net/MjAyMDA1MTRfNzAg/MDAxNTg5NDI1NDY1MTI3.ZEEFfm7YnYkVa-NzAgnCchajtnkRbOtIdesade7yoyEg.vZ9Bsxbp5P4j9Ih9qh3Eidg3Yx4DTGfvtrhcfvb0DyQg.PNG.samsunghappytree123/%EA%B0%95%EC%9D%981.PNG?type=w773)

저희는 여기서 임베드 명령어만 수정할껍니다.

먼저 docs에 있는 embed를 읽고 와보시는건 어떨까요?

[확인하러 가기](https://discordpy.readthedocs.io/en/latest/api.html?highlight=embed#discord.Embed)

![img](https://postfiles.pstatic.net/MjAyMDA1MTVfNTcg/MDAxNTg5NTI0NzU1Nzcx.uK7HkqM-NEgBHLafECr0IfeftNM2RfmrkM-oq8q5KA0g.ZruZd3GTvpc2v-ei-PdJKxFleQMvLDUCNeoHSEGR8bMg.PNG.samsunghappytree123/%EA%B0%95%EC%9D%982.PNG?type=w773)

먼저 이렇게 바꿔보려면 아래의 코드를 입력해보세요!
```py
embed.set_image(url="https://cdn.discordapp.com/avatars/652509076055523338/149b30c01677f61d587e8d199256442d.png?size=1024")
```
+ 해석 : 이미지를 url값으로 정한다.

하지만 아래의 사진처럼 사진이 나오게 하고 싶은 분들이 있을껍니다

![img](https://postfiles.pstatic.net/MjAyMDA1MTVfMTk1/MDAxNTg5NTI0ODk5NTIw.OrjS7AJS01Vp4trfEMnWcLGA4YyYJc_6AzZl87uZ0-sg.Z4NB-R6G9fawIf4a01NZnYTEnNHLhfTS_keZ7dfiW4Ig.PNG.samsunghappytree123/%EA%B0%95%EC%9D%983.PNG?type=w773)

이렇게 나오게 하려면 아래의 코드를 따라해보세요!
```py
embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/652509076055523338/149b30c01677f61d587e8d199256442d.png?size=1024")
```
+ 해석 : 썸네일을 url 값으로 정한다.

위의 코드를 넣고 실행해보면 아래와 같이 나옵니다.

![img](https://postfiles.pstatic.net/MjAyMDA1MTVfMTc3/MDAxNTg5NTI1MjA5MDQ3.tHPSPoSPLuHe2MQdc5rfh7zpA9k8wkj0YeTYCfhBolog.EHnnJrBn2_Fc3j4QmWNVvgA4jiev8JC9kob11ozW2psg.PNG.samsunghappytree123/%EA%B0%95%EC%9D%984.PNG?type=w773)

뭐가 많이 달라졌죠?

그러면 이제 다른걸 배워볼까요?

![img](https://postfiles.pstatic.net/MjAyMDA1MTVfODkg/MDAxNTg5NTI1MzQ0MDEx.jAc-GJjuR0NzFfCf0cS98AiT6t5rIsHjvkFwQzWqxWIg.rCK8464y-O-ArwusOXxCKu4lqXZ5HvYaJ2x3TwtYeK4g.PNG.samsunghappytree123/%EA%B0%95%EC%9D%985.PNG?type=w773)

도움말 같은거를 배워보겠습니다!

```py
embed.add_field(name = '필드 이름', value = '필드 값')
```

+ 해석 : field를 정한다
    + 이름 : name 값
    + 내용 : value값

그러면 한번 실행해볼까요?

![img](https://postfiles.pstatic.net/MjAyMDA1MTVfNzEg/MDAxNTg5NTI1NDk3OTMx.BWpBKRC5KltJpMfPWZqHt2xsFouVVtAR5gAPYBrw8eMg.bUIdJYR8xuhWgcaqxLTVyzLBHFzpXsKLT1ocO6X2-3cg.PNG.samsunghappytree123/%EA%B0%95%EC%9D%986.PNG?type=w773)

필드 이름과 필드 값이 추가되었습니다!

![img](https://postfiles.pstatic.net/MjAyMDA1MTVfMTQ2/MDAxNTg5NTI1NTM5Nzkx.T_seS3Edr1LUWRmcXwp3r2dyb2795L4QAT-c5oeYmQEg.IRv45CehK4NfIfby1mjaQTDoZNwp2qhy8nl65IEzyL8g.PNG.samsunghappytree123/%EA%B0%95%EC%9D%987.PNG?type=w773)

이런식으로 정리하시면 되겠습니다!

------------

강의를 봐 주셔서 감사해요! 5강에서 뵙겠습니다!
