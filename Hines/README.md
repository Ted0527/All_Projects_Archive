# Hines
> [오늘의집](https://ohou.se/store?utm_source=brand_google&utm_medium=cpc&utm_campaign=commerce&utm_content=e&utm_term=%EC%98%A4%EB%8A%98%EC%9D%98%EC%A7%91&source=14&affect_type=UtmUrl&gclid=Cj0KCQiA2ZCOBhDiARIsAMRfv9KqcY4mcWWZikC6z5zRQa7ZkFj4jcVxD_ZFBb1CgGwjTPNQPmBfBhQaAi7yEALw_wcB)
> 사이트의 다양한 기능 중 커머스 기능을 중심으로, '몇 십년 뒤의 집'이라는 컨셉 하에 우주 속 다른 행성들의 땅을 소개하고 필요한 물품 판매를 목적으로 하는 사이트.

# 프로젝트 개요
## 기간
- 2021.12.13 ~ 2021.12.24

## 멤버
- Backend : 이유진, 장도원, 제갈창민
- Frontend : 이지현, 홍정빈, 황주영</br>
[Frontend github](https://github.com/wecode-bootcamp-korea/27-2nd-Hines-frontend)


<br>

## 목표
- 다양한 툴(Trello, Notion, Slack, Github)을 사용함으로써 의사소통 능력 증대
- 초기 세팅부터 전부 실제 사용할 수 있는 서비스 수준으로 기획 및 배포까지 구현
- 화려하고, 고난이도의 로직을 구현하기보다는 그동안 학습했던 지식들을 2주 간의 팀 프로젝트에 복습 및 다진다는 것이 궁극적 목표

<br>

## 모델링
<img width="auto" src="https://raw.githubusercontent.com/Ted0527/wecode_projects_achive/main/Hines/images/%ED%95%98%EC%9D%B8%EC%A6%88_%EB%AA%A8%EB%8D%B8%EB%A7%81.png">
<br>

## SKillS
- Python
- Django
- Mysql
- AWS

<br>

## Communication Tools
- Slack
- Github
- Trello
- Notion

<br>

## 구현기능
- 소셜로그인
- 메인페이지
- 상세페이지
- 제품 리뷰 포스팅
- 장바구니
- 주문 확인 페이지
- CSV 데이터 작성 및 데이터 입력

## 세부 구현 사항
1. 카카오 소셜 로그인 구현
  - 카카오에서 제공하는 REST API를 이용해 프론트에서 받아온 카카오 token 으로 사용자의 정보를 요청
  - 받아온 정보 중 필요한 정보를 저장(nickname, email)
  - DB에 생성된 id로 JWT를 활용해 '우리의 token'으로 재가공하여 프론트로 응답.

2. 주문 확인 페이지 구현
  - 유저의 정보를 참조하는 Orders 와 상품을 정보를 참조하는 OrderItems 테이블로 구성되어 있다.
  - 주문 번호(order number)와 배송 번호(tracking number)를 uuid 모듈을 이용하여 랜덤하게 부여.
  - OrderStatus 테이블을 따로 두어 '배송중, 결제완료, 주문취소' 와 같은 상태 정보를 참조함. Enum 함수 사용.
  - patch 함수로 주문취소 상황을 따로 컨트롤 할 수 있도록 구현

3. Unit Test 적용
  - 소셜로그인와 주문 확인 페이지에 각각 UnitTest 를 적용하여 에러 및 잘못된 코드에 대한 문제점을 빠르고 확실하게 파악하여 수정하였음.
  - 불필요한 exception 최소화

<br>

## 시연 영상</br>
[시연 영상 YouTube](https://www.youtube.com/watch?v=Z4Hw1AQc_og)

<br>

## Reference
- 이 프로젝트는 [오늘의집](https://www.google.com/search?gs_ssp=eJzj4tVP1zc0zCopKc8tMchRYDRgdGDw4nkzY8nrrhlv5s54s3wiAL8EDec&q=%EC%98%A4%EB%8A%98%EC%9D%98%EC%A7%91&rlz=1C5CHFA_enKR980KR980&oq=%EC%98%A4%EB%8A%98%EC%9D%9C&aqs=chrome.3.69i57j0i512l2j46i10i199i465i512j46i175i199i512j0i512l3j0i10i512j0i512.2653j0j15&sourceid=chrome&ie=UTF-8) 사이트를 참조하여 학습목적으로 만들었습니다.
- 실무 수준의 프로젝트이지만 학습용으로 만들었기 때문에 이 코드를 활용하여 이득을 취하거나 무단 배포할 경우 법적으로 문제가 될 수 있습니다.
- 이 프로젝트에서 사용하고 있는 사진 대부분은 위코드에서 구매한 것이므로 해당 프로젝트 외부인이 사용할 수 없습니다.
