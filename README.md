# PythonHL7ToJson

This is a code that creates a REST service to parse HL7 to Json.

Based on this code <a href="https://gist.github.com/prschmid/801e86891026a39b1fb4df7178828321#file-hl7_to_dict-py">here</a> from <a href="https://gist.github.com/prschmid">@prschmid</a>

The REST interface is made through Flask.

<b><h2>How to invoke:</h2></b>

With the coding running, send a POST request to the URL:

http://localhost:5000/conversao/hl72json

The HL7 goes into the body, with content-type: application/x-www-form-urlencoded, into the parameter dados.

<a href="https://github.com/ChristoPedro/PythonHL7ToJson/blob/master/HL7%20to%20Json.postman_collection.json">Here</a> you can see the postman request example.
