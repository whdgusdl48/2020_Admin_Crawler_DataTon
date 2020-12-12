# 2020_Admin_Crawler_DataTon
![2020_Crawler_DataTon_포스터](https://user-images.githubusercontent.com/52066712/101982317-64ee8600-3cb6-11eb-88ad-e2e8cdf96bc3.png)

## 대회 목적

o 평소에 경험하기 어려운 빅데이터 분석의 실습 경험을 축적합니다.
o 데이터 분석을 위한 데이터를 직접 수집하며 데이터의 중요성을 배웁니다.
o Docker, python, node.js를 통하여 Backend의 개념을 넓히고 서버 쪽 부분에 지식을 쌓을 수 있습니다.
o 팀원들과 대회 진행을 통하여 팀워크를 향상하고 발표 경험을 쌓을 수 있습니다.

## DockerFile Node.js 사용법

1. Docker 설치
```
https://ebbnflow.tistory.com/203 이 사이트를 참고하여 설치해주세요.
```
2. 파이썬을 통한 대회 진행

```
docker pull jonghyeon9587/admin-crawler:1.0 명령어 입력
docker images 를 통해 pull한 이미지가 있는지 확인할 것.
docker run -it 8888:8888 -v /python jonghyeon9587/admin-crawler => 컨테이너 생성 및 실행 
컨테이너가 실행되었는지 확인하기위해 DockerTool Box 설치시 GUI 도구인 Kitematic 확인해주세요!
이미지 내 운영체제는 리눅스 기반이며 파이썬 코드를 작성하는 것보다 주피터로 이용해서 코딩을 진행하셔도 됩니다.
추가 라이브러리를 설치하고 싶으시면 pip3 install ... 해주셔도 상관없습니다.
파이썬 버전 : 3.7.4
기존 설치 라이브러리 : numpy pandas matplotlib BeautifulSoap4 pip3
```
