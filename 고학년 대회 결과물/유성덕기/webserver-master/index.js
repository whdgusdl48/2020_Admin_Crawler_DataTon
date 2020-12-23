// 모듈 호출 및 객체 생성
const bodyParser = require('body-parser');
const express = require('express');
const app = express();
const port = 3000;
const methodOverride = require('method-override');
const router = require('./routes/home') (app);
const mongoose = require('mongoose');

// https://eu-ne.tistory.com/entry/Mongodb-%EC%82%AC%EC%9A%A9%ED%95%98%EA%B8%B0

// mongoDB 연결
// let url = "mongodb+srv://아이디:"+encodeURIComponent("비밀번호")+"@주소/test"
// mongoose.connect(url, {useNewUrlParser:true,useUnifiedTopology:true,dbName:'test'},function(err){
//     console.log('err::'+err)
// });

// var Schema = mongoose.Schema;

// 데이터 형태에 따라 스키마 구성
// var music_schema = new Schema(
//     {title: String, shout_out: Number, popular_rank: Number, tag: String}
// )

// 모델을 위한 변수
// var data = mongoose.model('music', music_schema, '콜렉션 이름');

// 데이터 확인 - 항목별 표시
// DataCue.find(function(err, music){
//     if(error){
//         console.log("error::"+error);
//     } else {
//         music.array.forEach(function(row){
//             console.log("data::"+row.title);
//         });
//     }
// })

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({extended:true}));

// views/home으로 ejs 파일의 위치 지정
app.set('views', __dirname + '/views/home');

// 서버가 HTML 랜더링을 할 때 EJS 엔진을 사용하도록 설정
app.set('view engine', 'ejs');
app.engine('html', require('ejs').renderFile);

// 정적 파일을 다루기 위한 코드 (css파일)
app.use(express.static(__dirname+'/public'));

// PUT, DELETE method 허옹
app.use(methodOverride('_method'));

// 서버를 연결하고 function() 이용
const server = app.listen(port, function() {
    console.log(`Example app listening at http://localhost:${port}`);
});


