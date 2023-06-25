const express = require('express');
const request = require('request');
const bodyparser = require('body-parser');
const https = require('https');

const app = express();

app.use(express.static("public"));
app.use(bodyparser.urlencoded({ extended: true }));

app.get("/", function(req, res) {
  res.sendFile(__dirname + "/signup.html");
});

app.post("/", function(req, res) {
  const fname = req.body.fname;
  const lname = req.body.lname;
  const email = req.body.email;
  const data = {
    members: [
      {
        email_address: email,
        status: "subscribed",
        merge_fields: {
          FNAME: fname,
          LNAME: lname
        }
      }
    ]
  };
  const jsonData = JSON.stringify(data);

  const url = "USE YOUR OWN URL";
  const options = {
    method: "Post",
    auth: "nova:USE YOUR OWN API KEY"
  };

  const request = https.request(url, options, function(response) {

    if (response === 200){
        res.sendFile(__dirname+"/Success.html");
    }else{
        res.sendFile(__dirname+"/Failure.html");
    }


    let responseData = '';

    response.on("data", function(chunk) {
      responseData += chunk;
    });

    response.on("end", function() {
      console.log(JSON.parse(responseData));
    });
  });

  request.write(jsonData);
  request.end();
});

app.listen(3000, function() {
  console.log("server started at port 3000");
});
