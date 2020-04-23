from flask import Flask
from flask import request
from hl7apy.parser import parse_message

app = Flask(__name__)

def hl7_str_to_dict(s, use_long_name=True):

    """Convert an HL7 string to a dictionary
    :param s: The input HL7 string
    :param use_long_name: Whether or not to user the long names (e.g. "patient_name" instead of "pid_5")
    :returns: A dictionary representation of the HL7 message
    """

    s = s.replace("\n", "\r")
    m = parse_message(s)
    return hl7_message_to_dict(m, use_long_name=use_long_name)


def hl7_message_to_dict(m, use_long_name=True):

    """Convert an HL7 message to a dictionary
    :param m: The HL7 message as returned by :func:`hl7apy.parser.parse_message`
    :param use_long_name: Whether or not to user the long names (e.g. "patient_name" instead of "pid_5")
    :returns: A dictionary representation of the HL7 message
    """

    if m.children:
        d = {}
        for c in m.children:
            name = str(c.name).lower()
            if use_long_name:
                name = str(c.long_name).lower() if c.long_name else name
            dictified = hl7_message_to_dict(c, use_long_name=use_long_name)
            if name in d:
                if not isinstance(d[name], list):
                    d[name] = [d[name]]
                d[name].append(dictified)
            else:
                d[name] = dictified
        return d
    else:
        return m.to_er7()


@app.route("/hl72json", methods=["POST"])
def response():

    """Get HL7 data x-www-form-urlencoded body from the Post request
    and return HL7 as Json.
    The Body request format:
    {
        data:"HL7 Data"
    }
    """

    req = request.form
    return hl7_str_to_dict(req['data'])

if __name__ == '__main__':
    
    app.run(debug=True, host='0.0.0.0')