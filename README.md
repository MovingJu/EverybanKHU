# EverybanKHU
 
대학생을 위한 금융자신관리 프로그램입니다.

기존의 관리 프로그램보다 훨씬 다양한 통계수치를 제공하며 오픈소스라는 점이 차별점입니다.

**Pull Request** is always open to me

# Folder 구성

  - **Initial_screes/** : data.csv 속 아무 내용이 없는 초기 상태일때 나오는 스크린 전반을 관리
  - **data_csv**/ : 유저의 금융내역을 기록하고 다양한 csv함수들을 정의
  - **main_screen**/ : 앱이 실행되는 메인 화면의 요소들을 정의
  - **visualizer**/ : data.csv만을 이용해 통계 자료들을 시각화하는 다양한 함수들을 정의 및 생성한 통계 자료를 저장
  - **widgets**/ : main_screen속 widgets창의 다양한 위젯들을 정의

# Critically Requiring Packages

- kivy -> for running app
 
- buildozer -> for debugging

- pandas
- numpy -> above this is for transaction list

- matplotlib -> above this is for visualize

> check requirements.txt for running app without any bugs.

# python version: above 3.11

> 주의사항: class를 배우며 만들어서 코드가 상당히 더러움
