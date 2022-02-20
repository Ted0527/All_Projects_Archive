
# Introduction

- 기간 : 21.11.29 - 21.12.10
- 멤버 : Front-end 3명, Back-end 3명
- [프론트엔드 github](https://github.com/wecode-bootcamp-korea/27-1st-Brokurly-frontend)
- [Notion 프로젝트 소개 및 정리](https://pineapple-voyage-3ed.notion.site/Brokurly-d007312f7573445c860e268ebc60fbe7)

# Skills

- Python
- Django
- MySQL
- Git, Github

# ERD

<img width="" alt="스크린샷 2021-12-05 오후 6 16 02" src="https://user-images.githubusercontent.com/90754590/145568725-b50daf67-0506-4f15-9344-2381d83ee8b5.png">

# API 기능정의서

[API 기능정의서](https://docs.google.com/spreadsheets/d/1Pef-aPfqPTho8lBUXTizRTFqKoATX4ISbZswPHgFos8/edit#gid=0)

# 시연 영상 
[![Brokurly](https://media.vlpt.us/images/sae0428/post/f506ea79-a200-416c-bb47-b1138e53d240/1%EC%B0%A8%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8%20%EB%B8%8C%EB%A1%9C%EC%BB%AC%EB%A6%AC%20%EB%B2%A8%EB%A1%9C%EA%B7%B8%20%EC%8D%B8%EB%84%A4%EC%9D%BC.JPG)](https://youtu.be/RL1-vnUOx50)

# 앱 별 기능 구현 사항
- ★ 본인 구현 항목

### carts ★
- 장바구니 담기
- 장바구니 내역
- 수량 변경(get_or_create 메소드 활용)
- 아이템 삭제

### core(validator, login_decorator 모듈화) ★
- validator : 이메일, 패스워드, 유저네임 정규표현식에 따른 유효성 검사
- decorator : 발행한 JWT 와 패스워드 대조하여 인증/인가 여부 확인

### orders
- 주문 내역서 생성(생성이 완료되면 카트에서 해당 아이템들 삭제)
- 주문 내역 리스트
- 주문 상태 관리(결제완료, 입금대기, 주문취소 등)

### products ★
- 메인 페이지(상품 전체 or 카테고리별 리스트)
- 정렬(ordering) 및 필터링(filtering) 기능
- 제품 상세 페이지

### users
- 회원가입 및 로그인
- 중복 가입 유효성 검사
- bcrypt 라이브러리 활용하여 패스워드 암호화
- JWT 발급, 저장 및 제공
