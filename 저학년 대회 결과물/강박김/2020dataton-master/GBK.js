const axios = require('axios');
const cheerio = require('cheerio');
var musicNum = new Array();
var musicName = new Array();

let $href = [];
let j = 0;

  axios.get(`https://www.melon.com/chart/index.htm`)
      .then(value => {
        for (var i = 1; i < 100; i++) {
          const selector = "#frm > div > table > tbody > tr:nth-child(" + i +") > td:nth-child(4) > div > div > div.ellipsis.rank01 > span > a";
          const s2 = "#frm > div > table > tbody > tr:nth-child(" + i + ") > td:nth-child(3) > div > a";
          const $ = cheerio.load(value.data);
          const tmp = $(selector).text();
          musicName[i] = tmp;
          $(s2).each((index, item)=>{$href.push(item.attribs.href)});
          var splitWord = $href[j++].split("\'");
          musicNum[i] = splitWord[1];
          console.log(tmp);
          console.log("https://www.melon.com/song/detail.htm?songId=" + splitWord[1]);
     }
});
