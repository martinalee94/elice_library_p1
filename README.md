# elice_library_p1

# - 엘리스 도서관 대출 서비스 개발 마일스톤 일정 :thinking:

  - DB설계 및 페이지 별 DRAFT 구성(~11/18 목) :ballot_box_with_check: 
  - 로그인/로그아웃/회원가입 기능 개발(11/19 금) :ballot_box_with_check: 
  - 대여하기/반납하기/ 대여기록 기능 개발(~11/21 일) :ballot_box_with_check: 
  - 책소개(11/22 월) :ballot_box_with_check: 
  - VM 안내사항 확인 및 기 개발 기능 테스트(11/23 화) :ballot_box_with_check: 
  - 화면 UI 구성 및 발표자료 작성(~11/25 목) :ballot_box_with_check: 
  - VM테스트(11/26 금) :ballot_box_with_check: 
  - 발표자료 정리 및 예행연습(11/27 토) :ballot_box_with_check: 
  - 발표(11/28 일)

<br>
<br>

<details><summary>프로젝트 구조 한눈에 살펴보기</summary>

```
├── app/
│      ├─ __init__.py
│      ├─ models.py
│      ├─ main.py
│      ├─ dashboard.py
│      ├─ detail.py
│      ├─ auth.py
│      ├─ migrations/
│      ├─ static/
│      │   ├─ books.json
│      │   ├─ css/
│      │   ├─ js/
│      │   └─ img/
│      ├─ tests/
│      │   └─ error_handler.py
│      └─ templates/
│            ├─ base.html
│            ├─ home.html
│            ├─ dashboard.html
│            ├─ detail.html
│            ├─ login.html
│            ├─ signup.html
│            └─ error.html
├── .env
├── .gitignore
├── config.py
├── loaddata.py
├── requirements.txt
└── README.md
```

</details> 

<details><summary>실제 개발 현황 펼쳐보기 :100:</summary>

  - 2021/11/16 화
    - DB설계 및 프로젝트 요구 기능 파악
    - 로그인 페이지 및 메인 페이지 구현 
    <br>
  - 2021/11/18 목
    - <span style="color:red"> **DB(users, books)설계 및 프로젝트 재구성** </span> 
    - DB 데이터 입력
    - 로그인/로그아웃/회원가입 기능 개발, 책소개 페이지 구현
    <br>
  - 2021/11/19 금
    - 대여 기록 DB 설계
    - 대여하기 기능 개발 완료
    <br>
  - 2021/11/20 토
    - 반납하기/ 대여기록 기능 개발 완료
    - 메인 페이지 UI 개편
    - 회원가입 및 로그인 UI 개발 완료
    - 회원가입 시 USERNAME이 undefined로 입력되는 오류 수정
    <br>
  - 2021/11/21 일
    - 평점(rating) 테이블 설계 및 구현, 평점 기능 추가
    - 책 소개 페이지 UI 개발
    - Dashboard 페이지 책 리스트가 출력되지 않는 이슈 해결
    <br>
  - 2021/11/22 월
    - 메인페이지 페이지네이션 기능 개발 완료
    - Dashboard 현재 대여 중인 책 count 오류 이슈 해결
    <br>
  - 2021/11/23 화
    - 책 소개 페이지(리뷰 부분) 렌더링 방식 개편
    - 렌더링 방식 개편에 따른 책 소개 페이지 books & users 테이블 join방식 변경
    - 책 리뷰 삭제 기능 개발 완료
    <br>
  - 2021/11/24 수
    - Dashboard UI 개편
    - 회원가입 이름, 이메일, 비밀번호 가입 조건 설정 완료
    <br>
  - 2021/11/25 목
    - app_errorhandler 추가
    <br>
  - 2021/11/26 금
    - VM 배포 및 트러블슈팅
    - 발표 자료 작성
    <br>

</details>    



<br>
<br>


- # 개발 일일회고록 :pencil: 


| 날짜     | 주요 이슈 |
| :------: | :------ | 
| [21.11.16(화)](https://kdt-gitlab.elice.io/003-part2-project-library/team1/youngsuk/-/wikis/21.11.16(%ED%99%94)-%EC%9D%BC%EC%9D%BC%ED%9A%8C%EA%B3%A0) | 개발환경셋팅 |
| [21.11.17(수)](https://kdt-gitlab.elice.io/003-part2-project-library/team1/youngsuk/-/wikis/21.11.17(%EC%88%98)-%EC%9D%BC%EC%9D%BC%ED%9A%8C%EA%B3%A0) | DB(users, books)설계 및 이미지 처리 방식 구상 |
| [21.11.18(목)](https://kdt-gitlab.elice.io/003-part2-project-library/team1/youngsuk/-/wikis/21.11.18(%EB%AA%A9)-%EC%9D%BC%EC%9D%BC%ED%9A%8C%EA%B3%A0)| 프로젝트 재설계 <br> 로그인/회원가입 기능 개발 <br> 책 소개 페이지 구현 <br> |
| [21.11.19(금)](https://kdt-gitlab.elice.io/003-part2-project-library/team1/youngsuk/-/wikis/21.11.19(%EA%B8%88)-%EC%9D%BC%EC%9D%BC%ED%9A%8C%EA%B3%A0) | DB(rent) 설계 <br> 대여하기 기능 개발 <br> 사용자별 Dashboard 구현 <br>  |
| [21.11.20(토)](https://kdt-gitlab.elice.io/003-part2-project-library/team1/youngsuk/-/wikis/21.11.20(%ED%86%A0)-%EC%9D%BC%EC%9D%BC%ED%9A%8C%EA%B3%A0) | 반납하기 기능 개발 <br> 로그인/회원가입 버그 수정 및 UI 개편 <br> 메인페이지 UI 개편 <br> |
| [21.11.21(일)](https://kdt-gitlab.elice.io/003-part2-project-library/team1/youngsuk/-/wikis/21.11.21(%EC%9D%BC)-%EC%9D%BC%EC%9D%BC%ED%9A%8C%EA%B3%A0) | 평점(Rating)테이블 설계 <br> 책 평점 보여주기 기능 추가 <br> 책 소개 페이지 UI 개발 |
| [21.11.23(화)](https://kdt-gitlab.elice.io/003-part2-project-library/team1/youngsuk/-/wikis/21.11.23(%ED%99%94)-%EC%9D%BC%EC%9D%BC%ED%9A%8C%EA%B3%A0) | 책 소개 페이지(리뷰 부분) 바닐라 자바스트립트 방식 도입 <br> 책 리뷰 삭제 기능 개발 |
| [21.11.24(수)](https://kdt-gitlab.elice.io/003-part2-project-library/team1/youngsuk/-/wikis/21.11.24(%EC%88%98)-%EC%9D%BC%EC%9D%BC%ED%9A%8C%EA%B3%A0) | Dashboard UI 개편 <br> 회원가입 폼 조건(regex사용) 설정 완료 |
| [21.11.25(목)](https://kdt-gitlab.elice.io/003-part2-project-library/team1/youngsuk/-/wikis/21.11.25(%EB%AA%A9)-%EC%9D%BC%EC%9D%BC%ED%9A%8C%EA%B3%A0) | error_handler.py 추가 <br> error.html 생성 |
| [21.11.26(금)](https://kdt-gitlab.elice.io/003-part2-project-library/team1/youngsuk/-/wikis/21.11.26(%EA%B8%88)-%EC%9D%BC%EC%9D%BC%ED%9A%8C%EA%B3%A0) | VM배포 <br> 이슈 트러블 슈팅  <br> 발표자료 작성  |