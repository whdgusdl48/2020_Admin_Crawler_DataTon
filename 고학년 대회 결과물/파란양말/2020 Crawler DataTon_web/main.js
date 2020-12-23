const express = require('express');
const app = express();
const port = 3000;
var fs = require('fs');
var path = require('path');
// var sanitizeHtml = require('sanitize-html');
var qs = require('querystring');
var bodyParser = require('body-parser');
var compression = require('compression');
var template = require('./lib/template.js');
var tempcsv = require('./readdata.js');
var graph = require('./graph/main_garph.js');

app.use(express.static('public'));
app.use(bodyParser.urlencoded({ extended: false }));
app.use(compression());
app.get('*', function(request, response, next){
  fs.readdir('./data', function(error, filelist){
    request.list = filelist;
    next();
  });
});

app.get('/', (request, response) => {
  var title = '안녕하세요';
  var description = `<p>BGMSTORE(https://bgmstore.net/)에서 브금을 크롤링 하였습니다.</p>
    <p>이 사이트 에서는 총 51개의 카테고리와 카테고리별 순위로 분류한 브금을 볼 수 있습니다.</p>`;
  var list = template.list(request.list);
  var gh = graph.html(tempcsv);
  var home_table = template.home_table(tempcsv);
  var html = template.HTML(title, list,
    `<h2>${title}</h2><p>${description}</p>
    <p>${home_table}</p>
    <p>${gh}</p>`,
    '<link rel="stylesheet" href="css/style.css">'
  );
  response.send(html);
});

app.get('/page/:pageId', function(request, response, next){
  var filteredId = path.parse(request.params.pageId).base;
  fs.readFile(`data/${filteredId}`, 'utf8', function(err, description){
    if(err){
      next(err);
    } else{
      var title = request.params.pageId;
      title = title.split('.')[0];
      var table = template.page_table(title, tempcsv);
      var list = template.list(request.list);
      var html = template.HTML(title, list,
        `<h2>${title}</h2>${table}`,''
      );
      response.send(html);
    }
  });
});

app.use(function(request, response, next) {
  response.status(404).send('Sorry cant find that!');
});

app.use(function(err, req, res, next) {
  console.error(err.stack);
  res.status(500).send('Something broke!');
});

app.listen(port, () => {
  console.log(`Example app listening at http://localhost:${port}`)
});
