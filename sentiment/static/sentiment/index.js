document.addEventListener("DOMContentLoaded", function () {
  
    const Rdates=JSON.parse(document.getElementById('hello-data-1').textContent)
    const ratingCnt=JSON.parse(document.getElementById('hello-data-2').textContent)
    const r_month_count=JSON.parse(document.getElementById('r_c_count').textContent)
    var g_data=JSON.parse(document.getElementById('g_data').textContent)
    var r_data=JSON.parse(document.getElementById('r_data').textContent)
    var k_data=JSON.parse(document.getElementById('k_data').textContent)
    var s_data=JSON.parse(document.getElementById('s_data').textContent)

    

    let dates = []
    let count = []

    let ratingNo = []
    let ratingCount = []

    for(let i in Rdates)
    {
      dates.push(i)
      count.push(Rdates[i])
    }

    for(let j in ratingCnt)
    {
      ratingNo.push(j)
      ratingCount.push(ratingCnt[j])
    }


  //rating 

    const dataRat = {
    labels: ratingNo,
      datasets: [{
          label: '# of Ratings',
          data: ratingCount,
          backgroundColor: [
              'rgba(255, 99, 132, 0.2)',
              'rgba(54, 162, 235, 0.2)',
              'rgba(255, 206, 86, 0.2)',
             
          ],
          borderColor: [
              'rgba(255, 99, 132, 1)',
              'rgba(54, 162, 235, 1)',
              'rgba(255, 206, 86, 1)',
              
          ],
          borderWidth: 1
      }]
    }

  
    const configRating = {
        type: 'line',
        data: dataRat, 
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    }

    const ratingChart = new Chart(
        document.getElementById('ratingChart'),
        configRating
    )



    // Line Chart

    const dataLine = {
      labels: dates,
        datasets: [{
            label: '# of Reviews',
            data: count,
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                
            ],
            borderWidth: 1
        }]
    }

    
    const configLine = {
        type: 'line',
        data: dataLine, 
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    }

    const lineChart = new Chart(
        document.getElementById('lineChart'),
        configLine
    )


    const barchart1 = {
        labels: ['Negative', 'Neutral', 'Positive'],
          datasets: [{
              label: 'Random Forset',
              data: g_data,
              backgroundColor: [
                  'rgba(255, 99, 132, 0.2)',
                  'rgba(75, 192, 192, 0.2)',
                  'rgba(33, 255, 81, 0.2)',
                  
              ],
              borderColor: [
                  'rgba(255, 99, 132, 1)',
                  'rgba(75, 192, 192, 1)',
                  'rgba(33, 255, 81, 1)',
                  
              ],
              borderWidth: 1
          }]
      }
      
      
      const configBar1 = {
          type: 'bar',
          data: barchart1, 
          options: {
              scales: {
                  y: {
                      beginAtZero: true
                  }
              }
          }
      }
      
      const barChart1 = new Chart(
          document.getElementById('barChart1'),
          configBar1
      )
      
      
      
      // BarChart - 2
      
      const barchart2 = {
        labels: ['Negative', 'Neutral', 'Positive'],
          datasets: [{
              label: 'RidgeClassifier',
              data: r_data,
              backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(33, 255, 81, 0.2)',
                
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(33, 255, 81, 1)',
                
            ],
              borderWidth: 1
          }]
      }
      
      
      const configBar2 = {
          type: 'bar',
          data: barchart2, 
          options: {
              scales: {
                  y: {
                      beginAtZero: true
                  }
              }
          }
      }
      
      const barChart2 = new Chart(
          document.getElementById('barChart2'),
          configBar2
      )
      
      
      // BarChart - 3
      
      const barchart3 = {
        labels: ['Negative', 'Neutral', 'Positive'],
          datasets: [{
              label: 'Kneighbor',
              data: k_data,
              backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(33, 255, 81, 0.2)',
                
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(33, 255, 81, 1)',
                
            ],
              borderWidth: 1
          }]
      }
      
      
      const configBar3 = {
          type: 'bar',
          data: barchart3, 
          options: {
              scales: {
                  y: {
                      beginAtZero: true
                  }
              }
          }
      }
      
      const barChart3 = new Chart(
          document.getElementById('barChart3'),
          configBar3
      )
      
      
      
      // BarChart - 4
      
      const barchart4 = {
        labels: ['Negative', 'Neutral', 'Positive'],
          datasets: [{
              label: 'SVM',
              data: s_data,
              backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(33, 255, 81, 0.2)',
                
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(33, 255, 81, 1)',
                
            ],
              borderWidth: 1
          }]
      }
      
      
      const configBar4 = {
          type: 'bar',
          data: barchart4, 
          options: {
              scales: {
                  y: {
                      beginAtZero: true
                  }
              }
          }
      }
      
      const barChart4 = new Chart(
          document.getElementById('barChart4'),
          configBar4
      )

         
    // Review Month wise Count


    let month_year = []
    let rating_month = []

    for(let i in r_month_count)
    {
        month_year.push(i)
        rating_month.push(r_month_count[i])
    }

    const data = {
        labels: ratingNo,
        datasets: [{
            label: 'Rating Count Month ',
            data: rating_month[0],
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(33, 255, 81, 0.2)',
                
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(33, 255, 81, 1)',
                
            ],
            borderWidth: 1
        }]
    };
  

  
    const config = {
        type: 'bar',
        data, 
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    }
  
    const reviewMCount = new Chart(
        document.getElementById('reviewMCount'),
        config
    )

    const month_s = document.querySelector('.month')

    month_s.addEventListener('change', (event) => {
        
        const month_value = document.querySelector('.month').value;
        data.datasets[0].data = rating_month[month_value]
        reviewMCount.update()
    });


});
