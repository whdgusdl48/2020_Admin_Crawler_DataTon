module.exports = {
  HTML:function(title, list, body, css){
    return `
    <!doctype html>
    <html>
    <head>
      <title>${title}</title>
      <meta charset="utf-8">
      <!-- favicon.ico 404 (Not Found) -->
      <link rel="icon" href="data:;base64,iVBORw0KGgo=">
      <script src="https://cdn.jsdelivr.net/npm/chart.js@2.9.3/dist/Chart.min.js"></script>
      ${css}
    </head>
    <body>
      <h1><a href="/">2020 Crawler DataTon_파란양말팀</a></h1>
      ${list}
      ${body}
    </body>
    </html>
    `;
  },
  list:function(filelist){
    list = '';
    for(var i = 0; i < 51; i++){
      list += `<button type="button" onclick="location.href='/page/${filelist[i]}'">${filelist[i].split('.')[0]}</button>`
    }
    return list;
  },
  page_table:function(filename, tempcsv){
    var info = tempcsv.info;
    var count = tempcsv.count;
    var file_list = [];
    for (var i = 0; i < count.length; i++) {
      file_list.push(info[i][0].Category);
    }
    var i = file_list.indexOf(filename.split('.')[0]);
    var size = count[i];
    var table = `(total bgms: ${size})
     <table border="1">`;
    table += `<tr>
    <th>카테고리</th>
    <th>이름</th>
    <th>추천수</th>
    <th>링크</th>
    </tr>`
    for (var j = 0; j < size; j++) {
      table += `<tr>
        <td>${info[i][j].Category}</td>
        <td>${info[i][j].Name}</td>
        <td>${info[i][j].Rated}</td>
        <td><a href="${info[i][j].URL}">${info[i][j].URL}</a></td>
        </tr>`
    }
    table += '</table>';
    return table;
  },
  home_table:function(tempcsv){
    var total_size = 0;
    var sizes = (tempcsv.count + '').split(',');
    for (var i = 0; i < sizes.length; i++) {
      total_size += parseInt(sizes[i]);
    }
    var table = `(total bgm: ${total_size})
     <table border="1">`;
    var i = 0;
    table += `
    <tr>
    <th>수집한 사이트</th>
    <th>전체 브금 개수</th>
    </tr>`;
    table += `
    <tr>
      <td>bgmstore</td>
      <td>${total_size}</td>
    </tr>`;
    table += '</table>';
    return table;
  }
}

// module.exports = template;
