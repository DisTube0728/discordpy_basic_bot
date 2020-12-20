<h1 align="center">Discord.py 8강에 오신것을 환영해요!</h1>

> [디스코드](https://discord.gg/7npaMJf), [사이트](https://happytree.cf/), [이메일](mailto:samsunghappytree123@naver.com)

## 강의 제작자
**Mail : [samsunghappytree123@naver.com](mailto:samsunghappytree123@naver.com)), Discord : [Happytree Samsung#7612](https://discord.com/users/726350177601978438)**
> **무단 도용 금지. 이 강의를 따라할때는 상관 없지만, 강의를 배껴가는것은 출처를 남겨주세요.**
> **저작권은 삼성해피트리에게 있습니다. 문의는 [samsunghappytree123@naver.com](mailto:samsunghappytree123@naver.com)으로 해주세요.**
------------

## 8강은 바로! 도큐먼트 (DOCS)를 알아봅니다!
> [8강 바로가기](https://blog.naver.com/samsunghappytree123/221991148333)

> [유튜브 강의 바로가기](https://youtu.be/aWlKX4ilGb8)

------------

## 도큐먼드 강의는 다음과 같은 목차가 있습니다.
### 목차는 아래와 같아요!
순서대로 보시는것을 추천드립니다!
+ [도큐먼트 알아보기](#도큐먼트-알아보기)
+ [도큐먼트로 예시코드 찾아보기](#도큐먼트로-예시코드-찾아보기)

------------

## Discord.py 봇 강의를 보기 전 참고해주세요!
+ 단순하게 따라하려고 하지 마시고, 원리를 파악해보세요.
+ 궁금한점은 구글링을 해보신 후, [봇 강의 서버](https://discord.gg/7npaMJf)에서 말씀해주세요.
+ 오타 또는 오류는 깃허브 이슈로 생성해주세요.

------------

### 도큐먼트 알아보기
일단 Discord.py DOCS를 들어가봅시다. [접속하기](https://discordpy.readthedocs.io/en/latest/)

Discord.js 쓰시는분은 Discord.js DOCS도 들어가보시길 [djs docs](https://discord.js.org/#/)

### 도큐먼트로 예시코드 찾아보기
![docs 메인페이지](https://blogfiles.pstatic.net/MjAyMDA2MDVfMzkg/MDAxNTkxMzQ0MTY3MTMy.-hHiJD1lWeDaX5Rs-BYn_h0_viFM7By-5j7Z909tzasg.IIBcOnbfBTiUWcEwuTjGifTc0KEOx8pWysuQJmmanYUg.PNG.samsunghappytree123/%EA%B0%95%EC%9D%981.png)

ㅗㅜㅑ 조금 어지럽죠?

하지만 DOCS로 독학도 나쁘진 않습니다^^

![docs 검색](https://postfiles.pstatic.net/MjAyMDA2MDVfOTQg/MDAxNTkxMzQ0MjM5MTQ4.i7djhCmCDhWFAdSwogxlEiAAFIUbhuy5az_6SmKR9mgg.e6_WY8x5xJab7huholWxfyex0v2Y3BtHbcWYiJ0m47Mg.PNG.samsunghappytree123/%EA%B0%95%EC%9D%982.png?type=w773)

왼쪽에 있는 Quick Search에서 검색을 하세요!

저는 서버 관련 구문을 검색해볼껍니다!

![docs 검색결과](https://postfiles.pstatic.net/MjAyMDA2MDVfMTc4/MDAxNTkxMzQ0MjkyMTU1.Z-LZDjoD_c_Byv301_m_0oH3obW_zUXdPSlAYeS__e4g.ubrxRJCAKN28YDHzfLS-ftfDu5JqJhejLStk2EiNSY4g.PNG.samsunghappytree123/%EA%B0%95%EC%9D%983.png?type=w773)

이렇게 마니 뜨네요! 여기서 저는 서버에 아이콘 url을 따볼껍니다.

discord.Guild.icon_url 보이시죠? discord.Guild.icon_url 쓰면 당연히 안됩니다!

그냥 discord.Guild.icon_url이라는 문구를 클릭해봅시다.

![docs 페이지](https://postfiles.pstatic.net/MjAyMDA2MDVfMjI1/MDAxNTkxMzQ0NDA3OTMw.jrKqOHnbUgIN1tFIhfnXc6EueQxVQh03NsKmLTFp-iUg.3KHB8dkfMfcmjcO8feMu8C4inm4CGLNsxpZJE9a6U38g.PNG.samsunghappytree123/%EA%B0%95%EC%9D%984.png?type=w773)

어딘가로 스폰했는데..?

iconurl이 나오네요!

대충 저렇게 나오면

```py
<변수>.icon_url
```

이런식으로 쓰시면 됩니다.

```py
if message.content == "서버아이콘":
    await message.channel.send(message.guild.icon_url)
```

이렇게 하면 됩니다.

![docs로 코드 만들기](https://postfiles.pstatic.net/MjAyMDA2MDVfODMg/MDAxNTkxMzQ0NTY4OTQ0.v64sVTf9W5mjsHI1FBXaD_IxJ4Ep6kPDXyCN3XobHIcg.wAtbPQwS4ixxFi7C_MFsZNRCD2WUDLP67I1WpmqS4Ogg.PNG.samsunghappytree123/%EA%B0%95%EC%9D%985.PNG?type=w773)

실행해본다면, 

![실행 결과](https://postfiles.pstatic.net/MjAyMDA2MDVfMjYy/MDAxNTkxMzQ0NzE0NjQ1.vZSZRnzPGZ6gd4O7uA6-UOqO7rXNkJf1RDNMK82i2i8g.7HpARycNbtzD3-XNBg4-YtQPiM3XgwaeNL2iclSKjR4g.PNG.samsunghappytree123/%EA%B0%95%EC%9D%986.PNG?type=w773)

서버아이콘이 제대로 나오군요!

이렇게 discord.py DOCS로 독학을 해봅시다!

밑에 이런 구문이 있었어요.

```py
icon_url_as(*, format=None, static_format='webp', size=1024)
```

이건 뭘까요? 저도 몰랐는데 한번 해보겠습니돠!

![docs icon_url_as 코드](https://postfiles.pstatic.net/MjAyMDA2MDVfMTg2/MDAxNTkxMzQ0OTAxMDcw.dxUL6NthXF0xeVopWOD0j28lJYltzFcA6N5AOA6O3n0g.9XN0q4X2J1Z50YWVlDvA7wXL7i1UwbdipLUEKN61clUg.PNG.samsunghappytree123/%EA%B0%95%EC%9D%987.PNG?type=w773)

한번 실행해보았는데...

![실행 결과](https://postfiles.pstatic.net/MjAyMDA2MDVfNTEg/MDAxNTkxMzQ0OTAxMDky.bjEsNuPNqK6V-XaZQ669jjkLZgRK7LplkhyLCK_E9Mcg.pgXf5coLZPz2MlUug2TNVlDi9Cs7TuVuf87H-w5Z4Vwg.PNG.samsunghappytree123/%EA%B0%95%EC%9D%988.PNG?type=w773)

이것도 아주 잘 된다는 것을 볼 수 있습니다!

------------

혹시나 무언가가 안된다면?! docs에서 검색을 한 번 해보는것도 좋을 것 같습니다 :)

강의를 봐 주셔서 감사해요! 9강에서 뵙겠습니다!