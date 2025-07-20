# Factorial Calculator API
- This is a factorial api that can calculate large Factorial number like 1200!
- This Api Orignally power by Replit, However, it has been moved to Render
----
## URL
The URL is: https://factorial-api.onrender.com/
## API URL
````https://factorial-api.onrender.com/calc?q={input} ````
### Example
https://factorial-api.onrender.com/calc?q=10 –—> ````{"error":false,"input":"10","result":"3628800"}````

## Sample Code
HTML
````
<input id="input" type="number" placeholder="Enter a number">
<div id="enter">Enter</div>
<br>
<textarea readonly id="display"></textarea>
````
Javascript
````
fetch("https://factorial-api.onrender.com/calc?q=" + document.getElementById("input").value)
        .then(function (response) {
           return responde.json
        })
        .then(function (data) {
            if (data.error) {
                throw new Error(data.error)
            } else {
                document.getElementById("display").value = data.result
            }
        })
        .catch(function (error) {
            console.error(error)
            alert(error);
        })
````
