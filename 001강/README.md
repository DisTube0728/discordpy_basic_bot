<h1 align="center">Discord.py 1강에 오신것을 환영해요!</h1>

> [디스코드](https://discord.gg/7npaMJf), [사이트](https://happytree.cf/), [이메일](mailto:samsunghappytree123@naver.com)

## 강의 제작자
**Mail : [samsunghappytree123@naver.com](mailto:samsunghappytree123@naver.com)), Discord : [Happytree Samsung#7612](https://discord.com/users/726350177601978438)**
> **무단 도용 금지. 이 강의를 따라할때는 상관 없지만, 강의를 배껴가는것은 출처를 남겨주세요.**
> **저작권은 삼성해피트리에게 있습니다. 문의는 [samsunghappytree123@naver.com](mailto:samsunghappytree123@naver.com)으로 해주세요.**
------------

## 1강은 프로그램 설치와 관련된 강의입니다!
> [블로그 강의 바로가기](https://blog.naver.com/samsunghappytree123/221941697301)

> [유튜브 강의 바로가기](https://www.youtube.com/watch?v=cYlI5fdr-j4)

------------

## 프로그램 설치에는 다양한 파일이 있어요!
### 파일 순차는 아래와 같아요!
순서대로 보시는것을 추천드립니다!
+ [python 설치하기](#파이썬-설치하기)
+ [vsc 설치하기](#vsc-설치하기)
+ [봇 만들고 초대하기](#discord-bot-만들고-초대하기)
+ [모듈 설치하기](#모듈-설치하기)
+ [Mac PIP 설치방법](#mac-pip-설치-방법)

------------

## Discord.py 봇 강의를 보기 전 참고해주세요!
+ 단순하게 따라하려고 하지 마시고, 원리를 파악해보세요.
+ 궁금한점은 구글링을 해보신 후, [봇 강의 서버](https://discord.gg/7npaMJf)에서 말씀해주세요.
+ 오타 또는 오류는 깃허브 이슈로 생성해주세요.

------------

### 파이썬 설치하기

먼저 [파이썬 사이트](https://www.python.org/)에 접속합니다.

![python](https://postfiles.pstatic.net/MjAyMDA1MDJfOTUg/MDAxNTg4NDA3Mjk3NTE0.P7cKO5yEtgGghNiGZcUyNzvvIs5D4YRcwIt4mA1bkbMg.KtxdkW6z3c3uLyYNKG9Jct8upWWnBYmwkngKCmgmenQg.JPEG.samsunghappytree123/%EA%B0%95%EC%9D%981.jpg?type=w773)

여기서 최신 버전 설치를 권장합니다!

어떤 버전도 괜찮으니 설치해주세요!

+ 저기에서 Windows 개발환경이라면 바로 다운로드 버튼을 바로 누르시면 되구요,
+ macOS 이라면 파란색 사각형이 있는 곳으로 들어가서 다운로드 받아주시면 됩니다!

다운 받으신 파일을 열어봅시다!

![python download1](https://postfiles.pstatic.net/MjAyMDA1MDJfMTgw/MDAxNTg4NDA3NTUxMTcy.WDYllULqW8HMjywdW8PBG2txPY9gfQFHiuPKX0JboH0g.c6PffNuMs_DUt3zOsOe3Azx3GJGnCRLnlSegOUTwP3Yg.JPEG.samsunghappytree123/%EA%B0%95%EC%9D%982.jpg?type=w773)

저런 화면이 뜰텐데요, 먼저 `Add Python <버전 (3.8.2라면 3.8)> to PATH` 버튼을 꼭 눌러주신 후 `Install Now` 버튼을 눌러주세요!
+ **누르지 않았다면 제거 후 다시 설치해야합니다. [여기](https://blog.naver.com/samsunghappytree123/221984128090)에서 확인해주세요!**

![python download2](https://postfiles.pstatic.net/MjAyMDA1MDJfNDcg/MDAxNTg4NDA3NjU0NTM2.1MZIV_jgLnbS70fZp0zXacbGfLlP7T83scrUo7DQujog.P-ZxT86t80L73Z3HW36xp0vFOd0PEqxosRaFcjN4VJ0g.PNG.samsunghappytree123/%EA%B0%95%EC%9D%983.png?type=w773)

이런식으로 다운이 완료된다면 `Close`를 누르셔서 나가줍니다.

------------

### VSC 설치하기

VSC (Visual Studio Code의 약자)를 다운받아줍니다!

[다운받으러 가기](https://code.visualstudio.com/Download)

![vsc download1](https://postfiles.pstatic.net/MjAyMDA1MDJfMjAw/MDAxNTg4NDA4ODM2NDc4.JRXTR_pPfW2FsfrHAb0SIkGNPSLqZh_9nkx3ib5pdh0g.mj7NHini6kEC302ggQnW2ehyQhNw5vvUzb1zKz2Y9fAg.JPEG.samsunghappytree123/%EA%B0%95%EC%9D%986.jpg?type=w773)

Windows는 빨간색 동그라미, 리눅스는 파란색 동그라미, macOS는 초록색 동그라미가 있는 버튼을 클릭해서 다운받아줍니다!

그리고 실행해줍니다!

![vsc download2](https://postfiles.pstatic.net/MjAyMDA1MDJfMjU3/MDAxNTg4NDA5MDQzMDQ5.nIeDlwx0hS3cPXOzrAvMEweD3_9tO_lEh4IeE00Z6Ckg.6j8uADBJUitK5rSLsjOZ52VhRtVDcFr1f7bk6vaDTS8g.JPEG.samsunghappytree123/%EA%B0%95%EC%9D%987.jpg?type=w773)

여기서 동의를 클릭하신 후 다음을 눌러줍니다. 그러면 설치가 됩니다!

설치가 완료되면 실행해주세요!

그러면 VSC 설치가 완료된것입니다!

------------

### Discord Bot 만들고 초대하기

[여기](https://discord.com/developers/applications/)로 접속합니다!

![bot create](https://postfiles.pstatic.net/MjAyMDA1MDJfMTc1/MDAxNTg4NDA5MjYzMzY2.QoBPyrn79gPq_BlQMbFS7SH3PX6a38rmfQ3AbOc7ZV0g.CklqNW8tLwqbTM-TCYGAGGcLKOfGhDlaeLeCPJy-euwg.JPEG.samsunghappytree123/%EA%B0%95%EC%9D%988.jpg?type=w773)

여기서 우측 상단에 있는 `New Application` 버튼을 눌러줍시다!

![bot create](https://postfiles.pstatic.net/MjAyMDA1MDJfMjMw/MDAxNTg4NDA5NDMyNjUy.s_JIVSIyp8wdju79S3yzHKdQSKIuqyDLHzCp3zxTc-0g.dVEtdFP_3ZwoGlnzYd_OpaAu7-CLVjVtSKE2tUBg7KIg.JPEG.samsunghappytree123/%EA%B0%95%EC%9D%989.jpg?type=w773)

누르면 위와 같은 화면이 나오는데 빨간 사각형이 들어간 칸에 원하는 봇의 이름을 써줍니다!

그리고 Create 버튼을 눌러 생성을 해줍니다!

![bot create](https://postfiles.pstatic.net/MjAyMDA1MDJfMjQw/MDAxNTg4NDA5NTQ0OTAx.ebb1fH5PtR9jNi4-aNzr5hTe70NTkBfFEs9cX4JFr1Eg.l8_0h4OaT07ovhilC6NkSCW03MkqFj_IGc1M53XxxSwg.JPEG.samsunghappytree123/%EA%B0%95%EC%9D%9810.jpg?type=w773)

그러면 이런 화면이 뜨는데요, 하늘색 원에는 봇의 프로필 사진을, 빨간 사각형이 있는 칸에는 봇의 이름을, 초록 사각형이 있는 곳은 설명을 (설명은 안써도 됨) 써주시면 됩니다!

그리고 왼쪽편에 잘 보시면 Bot이라는 칸이 있는데 클릭해봅시다!

![bot create](https://postfiles.pstatic.net/MjAyMDA1MDJfNDcg/MDAxNTg4NDA5Njc4NjMz.3Xbgl3405CflVap_sslxSMuzoMA2dxWTIUENPTGu7hgg.S0USlBmSX9y4et4FU7RvYCAiaL4T4nRk36Yv8-j_MIMg.JPEG.samsunghappytree123/%EA%B0%95%EC%9D%9811.jpg?type=w773)

Add Bot 버튼을 눌러줍시다!

![bot create](https://postfiles.pstatic.net/MjAyMDA1MDJfMTQ1/MDAxNTg4NDA5Nzc0ODc0.UZ_6rpbF6NpalVzrOweSKosXOcZKADd_tM2C6ytwFj8g.ODKA0vifBifPT42WaEkmasUiC500IowyxeB3_6WZm7cg.JPEG.samsunghappytree123/%EA%B0%95%EC%9D%9812.jpg?type=w773)

그러면 이런 화면이 뜨는데 만일 안된다면 처음에 생성했던곳에서 이름을 다른 이름으로 바꿔줍시다!

노란색 동그라미는 봇 프사, 빨간색 사각형은 봇 이름, 파란색으로 감싸져있는 것은 봇의 토큰, 초록색 사각형은 공개 봇으로 할것인지 여부입니다!

일단 봇의 토큰이 있는 곳에 `Copy`를 누른 후 메모장에 붙여넣어봅시다!

![bot create](https://postfiles.pstatic.net/MjAyMDA1MDJfMTY0/MDAxNTg4NDEwMDU2NDAw.xKpcS_RGovBoBdii3GWdt1UFC1IxM34x4LI7SVgwEEAg.BYoZ7JRJ5lQgTZ3DCNzeDtX8EGifcsvB2TdBeIHhQQIg.PNG.samsunghappytree123/%EA%B0%95%EC%9D%9813.PNG?type=w773)

**중요**
+ **저는 강의이기 때문에 이렇게 공개하지만, 실제로는 다른 사람에게 노출하시면 안됩니다! 저 토큰이란것은 봇을 실행하려고 할때 봇의 비밀번호같은겁니다! 절대 다른분에게 노출하지 마세요!**

그리고 공개 여부는 `봇 초대 링크를 가져와서 다른 사람들이 봇을 초대할 수 있게 할것인가? 아닌가?` 입니다! 만일 봇을 초대할 수 있게 하려면 그냥 두시면 되고, 초대할 수 없게 하려면 저 설정을 끄면 됩니다!

그럼 이번에는 봇을 초대해볼까요?

왼쪽편에서 OAuth2를 찾아서 들어가봅시다!

![bot create](https://postfiles.pstatic.net/MjAyMDA1MDJfOTcg/MDAxNTg4NDEwMjMyOTQ1.S6XVykeIl4SAxPuHHGM3VDMHJlN08241XlJrYyr5nA8g.vYgBb6pUFTTzWSDvG_hGMWN9Su1-AcdqwCwSTssjIh8g.PNG.samsunghappytree123/%EA%B0%95%EC%9D%9814.png?type=w773)

그럼 이런 화면이 뜨는데 사각형에서 bot을 찾아 클릭해줍시다!

![bot create](https://postfiles.pstatic.net/MjAyMDA1MDJfNTcg/MDAxNTg4NDEwMzAzMDc4.QL23tiMneiRGxYgU9ox8sRZVrUPW9qBqRzO_WjQlKY4g.FNPiVVXnvx16WOZbtlLguQhEVsLhHho-Jra-oTXCroUg.PNG.samsunghappytree123/%EA%B0%95%EC%9D%9815.png?type=w773)

그러면 이런 화면이 뜨는데 중간에 있는 링크는 봇 초대 링크입니다!

권한은 아무것도 없는 상태가 됩니다!

아래쪽 표에 있는 권한을 선택해서 초대해보세요!

![bot permissions](https://cdn.discordapp.com/attachments/677024323780870174/719483259867627530/unknown.png)

![bot invite](https://postfiles.pstatic.net/MjAyMDA1MDJfMjU5/MDAxNTg4NDExNjA2NjYx.5HGk63pdSrB4YKlOLl59h9VZCZg9PC7a76pb5BbWqCUg.ZlFs5XP97R-8D4lXTdv9Vmkl7l2FErOYloQsertDF_og.JPEG.samsunghappytree123/%EA%B0%95%EC%9D%9816.jpg?type=w773)

빨간색 동그라미에 봇을 초대하고 싶은 서버를 확인하고 계속하기를 누르면 리캡챠를 해야 합니다!

![bot invite](https://postfiles.pstatic.net/MjAyMDA1MDJfMjc0/MDAxNTg4NDExNjcwNDc0.uSCIjRi8_Eq6pGeNhDzgiXj8BtUu-0HkTCAmtYwFDfog.ranDC-fmhISGbEs2ccu_OFudxpZF0z8J-nkEfVGqjcUg.PNG.samsunghappytree123/%EA%B0%95%EC%9D%9817.png?type=w773)

물론 이 화면이 뜬다면 승인 눌러주면 되구요, `로봇이 아닙니다` 라는 창이 뜨면 하라는 대로 하시면 초대가 완료되었습니다!

![bot invite](https://postfiles.pstatic.net/MjAyMDA1MDJfOTMg/MDAxNTg4NDExODg2ODI3.5To_EIyzdgdMSEFZhxWYvQsNQg2wiNkwb60NpAbWRNcg.bj41_SjaQ7khjUNiNeQ-bmP9rZ5dfiKrZ3xYCYwRr2kg.JPEG.samsunghappytree123/%EA%B0%95%EC%9D%9818.jpg?type=w773)

봇이 초대된 것을 볼 수 있습니다!

하지만 봇이 오프라인이네요 ㅠㅠ

다음 시간엔 기본적인 코딩을 배워보도록 하겠습니다!

------------

### 모듈 설치하기
윈도우 검색창에 cmd를 쳐서 열어줍시다!

![cmd](https://postfiles.pstatic.net/MjAyMDA1MDJfMjky/MDAxNTg4NDA3Nzk1MTI4.sgEAHWus_UujLpn56qD_7MadGZD6h9XExrj63yLMmx8g.jnlQbp7p_UsGjLHoYybqv2Elv5tgvSwt9mmFLTUOFgsg.PNG.samsunghappytree123/%EA%B0%95%EC%9D%984.PNG?type=w773)

요기서 `pip install discord`를 입력해줍니다!

![cmd install discord](https://postfiles.pstatic.net/MjAyMDA1MDJfMjE5/MDAxNTg4NDA3ODQ4NDAz.Ol1FPRADKkAovebaI_lamnufH85ppZwS9MSauDE0Vmog.U02TO3WkwbQmBQDAJfHhrJR93DC2hXhoR6We9r3ZgbEg.PNG.samsunghappytree123/%EA%B0%95%EC%9D%985.PNG?type=w773)

이런 식으로 하시면 됩니다. (꼭 저런 문구 안떠도 됨. 빨간 글자만 안나오면 됨.)

위와 같이 `pip install discord.py` / `pip install asyncio` 를 설치해줍니다!

------------

### Mac pip 설치 방법

Mac OS 에도 윈도우의 cmd와 같은 프로그램이 있습니다. 바로 '터미널'인데요. 터미널을 실행해주신 후 'python3 -m pip install -U discord.py' 를 입력해주시면 discord 모듈이 설치됩니다.

(LeeSeut - Official#9490님 제공)
------------

강의를 봐 주셔서 감사해요! 2강에서 뵙겠습니다!