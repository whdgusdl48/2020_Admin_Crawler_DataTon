const csv = require('csv-parser');
const fs = require('fs');

var bgms = {
  count:[],
  info:[],
}

var file_list = ['감동','개드립','격렬','경쾌','고요','고전','공포','귀여움','긴박','긴장','달달','당당','동심','따뜻','몽환','미분류','발랄','비장','비트','순수','슬픔','신남','신비','심각','쓸쓸','아련','애잔','애절','여유','엽기','우울','웅장','유머','일상','잔잔','장엄','좌절','즐거움','진지','초조','추억','클럽','평화','한심','합필갤','행복','활기','훈훈','흥겨움','흥함','희망']; // size = 51

for(var i = 0; i < file_list.length; i++){
  file_path = './data/'+file_list[i]+'.csv';
  read_csv(file_path);
}


function read_csv(file_path){
  var result = [];
  var count = 0;
  fs.createReadStream(file_path)
    .pipe(csv())
    .on('data', (row) => {
      count += 1;
      result.push(row)
    })
    .on('end', () => {
      bgms.count.push(count);
      bgms.info.push(result);
    })
}

module.exports = bgms;
