module.exports = {
    html:function(tempcsv){
        var count = clone(tempcsv.count);
        var arr = [];
        var sorted_count = count.sort(function(a, b) {
            return b - a;
        });
        var top_count = sorted_count.slice(0, 5);
        for (var i = 0; i < 5; i++) {
            var target = top_count[i];
            var index = [];
            for (var j = 0; j < tempcsv.count.length; j++) {
                if (target == tempcsv.count[j]) {
                    index.push(j);
                }
            }
            Array.prototype.push.apply(arr, index);
        }
        var top_category = [];
        for (i = 0; i < arr.length; i++) {
            top_category.push(tempcsv.info[arr[i]][0].Category + '');
        }
        
      return`
      <div id="chartContainer2" style="height: 260px; width: 500px;">
      <canvas id="myChart2"></canvas>
      <h3><상위 5개 카테고리의 브금 개수></h3>
      </div>
      <script>
      var ctx = document.getElementById('myChart2').getContext('2d');
      ctx.canvas.width  = window.innerWidth;
      ctx.canvas.height = window.innerHeight;
      var myChart = new Chart(ctx, {
      type: 'bar',
      data: {
        labels: ['미분류', '신남', '평화', '합필갤', '유머'],
        datasets: [{
          label: 'Count',
          data: [${top_count}],
          backgroundColor: [
            'rgba(255, 99, 132, 0.2)',
            'rgba(54, 162, 235, 0.2)',
            'rgba(255, 206, 86, 0.2)',
            'rgba(75, 192, 192, 0.2)',
          ],
          borderColor: [
            'rgba(255, 99, 132, 1)',
            'rgba(54, 162, 235, 1)',
            'rgba(255, 206, 86, 1)',
            'rgba(75, 192, 192, 1)',
          ],
          borderWidth: 1,
          fill: false
        }]
      },
    });
    </script>`;
    }
  }

  function clone(obj) {
    if (obj === null || typeof(obj) !== 'object')
    return obj;
  
    var copy = obj.constructor();
  
    for (var attr in obj) {
      if (obj.hasOwnProperty(attr)) {
        copy[attr] = obj[attr];
      }
    }
  
    return copy;
  }
  