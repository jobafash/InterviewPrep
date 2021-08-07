const https = require('https');

https.get('https://coderbyte.com/api/challenges/json/rest-get-simple', (resp) => {
  
  let data = '';

  // parse json data here...
  resp.on('data', (d) => {
    data += [d]
  })

  resp.on('end', () => {
    res = JSON.parse(data)
    console.log(res.hobbies)
  })
  

});