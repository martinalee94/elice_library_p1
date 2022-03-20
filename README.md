# 엘리스 도서관 대출 서비스
Flask, MySQL, Bootstrap을 이용해 도서관 책 대여 웹서비스를 구현했습니다.(개인프로젝트) <br>
서버사이드 렌더링 방식이며, Flask ORM을 이용하여 데이터베이스를 이용했습니다.



<br>
<br>


# 프로젝트 구조

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



<br>
<br>


# 개발 일일회고록 :pencil: 


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
