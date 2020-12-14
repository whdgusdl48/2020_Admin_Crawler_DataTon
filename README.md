# 2020_Admin_Crawler_DataTon
![2020_Crawler_DataTon_포스터](https://user-images.githubusercontent.com/52066712/101982317-64ee8600-3cb6-11eb-88ad-e2e8cdf96bc3.png)

## 대회 일정

o 대회 접수 : 12월 14일(월) ~ 12월 18일(금) <br />
o 대회 사전 교육 : 12월 21일(월) <br />
o 대회 개최 및 진행 : 12월 23일(수) 09:00 ~ 18:00 <br />

## 대회 목적

o 평소에 경험하기 어려운 빅데이터 분석의 실습 경험을 축적합니다. <br />
o 데이터 분석을 위한 데이터를 직접 수집하며 데이터의 중요성을 배웁니다. <br />
o Docker, python, node.js를 통하여 Backend의 개념을 넓히고 서버 쪽 부분에 지식을 쌓을 수 있습니다. <br />
o 팀원들과 대회 진행을 통하여 팀워크를 향상하고 발표 경험을 쌓을 수 있습니다. <br />

## 평가 방식 및 시상

본 대회의 평가 방식은 다음과 같습니다. <br />

대회 평가 방식은 팀원 평가 40% + 심사위원 평가 점수 60% 비율로 반영합니다.<br />
저학년 대회는 데이터의 창의성, 데이터의 실효성, 데이터의 정확성을 바탕으로 평가합니다.<br />
저학년 대회는 2팀, 고학년 대회는 3팀을 선정하여 시상합니다.
<p>
  <p>
    저학년 상금
  </p  
  <span style={color : blue}> 1등 팀 150,000원</span><br /> 
  <span style={color : blue}> 2등 팀 100,000원</span><br />
</p>

<p>
   <p>
    고학년 상금
   </p>  
   1등 팀 200,000원 <br /> 2등 팀 150,000원 <br /> 3등 팀 100,000원
</p>

## 제출방식
제출은 중간, 최종 2번에 걸쳐서 제출합니다. 이 점에 번거롭게 하여 죄송합니다. <br />
중간 제출은 현재 진행중인 각자 팀원의 화면 캡처를 기본으로 합니다.<br />
최종 제출은 저학년은 코드 및 보고서, 발표 유튜브 링크를 제출하시면됩니다. 고학년은 DockerFile, (compose로 실행하셨으면 그 파일도 다 제출하셔야합니다.), 코드, 발표 유튜브 링크입니다. 

## 수상자

12월 23일 18시에 공개됩니다.

## Docker

1. Docker 설치
```
https://ebbnflow.tistory.com/203 이 사이트를 참고하여 설치해주세요.
Docker ToolBox는 바탕화면에 진행해주시는게 좋습니다. 관리자 권한이 있는 C 드라이브의 경우에는 Vi editor가 잘 안될 수 있습니다.
```
2. 파이썬을 통한 대회 진행

```
docker pull jonghyeon9587/admin-crawler:1.0 명령어 입력

docker images 를 통해 pull한 이미지가 있는지 확인할 것.

docker run -it 8888:8888 -v /python jonghyeon9587/admin-crawler => 컨테이너 생성 및 실행 

컨테이너가 실행되었는지 확인하기위해 DockerTool Box 설치시 GUI 도구인 Kitematic 확인해주세요!

이미지 내 운영체제는 리눅스 기반이며 파이썬 코드를 작성하는 것보다 주피터로 이용해서 코딩을 진행하셔도 됩니다.

주피터 실행 명령어 : jupyter notebook --ip=0.0.0.0 --port=8888 --allow-root => 반드시 컨테이너에서 실행하셔야합니다.

추가 라이브러리를 설치하고 싶으시면 pip3 install ... 해주셔도 상관없습니다.

파이썬 버전 : 3.7.4

기존 설치 라이브러리 : numpy pandas matplotlib BeautifulSoap4 pip3

```
3. Node.js를 통한 대회 진행
```
위에 게시한 Deploy-Docker-Node.js 폴더를 다운받습니다.

다운받은 폴더를 Docker ToolBox 폴더에 넣어줍니다. 

docker-compose-up을 이용해 실행합니다

기본적으로 설치된 라이브러리는 Express, nodemon 이있습니다. 추가적으로 설치하실 라이브러리가 있으시면

Kitematic에 GUI에 들어가셔서 해당 실행하는 컨테이너를 클릭 후 exec를 누르시면 터미널이 나옵니다.

npm install body-parser와 같이 진행하시면 현재 진행하고있는 코드에 자동으로 package.json이 추가됩니다.
```
