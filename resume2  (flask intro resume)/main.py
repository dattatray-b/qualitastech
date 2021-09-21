from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/academics/<string:a>')
def academics(a):
    if( a == '10'):
        result = {
            "Examination": "X",
            "University" : "maharastra board of secondary and higher secondary education",
            "Institute"  : "adarsh shikshan mandir",
            "year"       : "2012",
            "Marks"      : "86.20%"
        }
    elif ( a == '12'):
        result = {
            "Examination": "XII",
            "University" : "maharastra board of secondary and higher secondary education",
            "Institute"  : "vidya mandir prashhala junior college",
            "year"       : "2014",
            "Marks"      : "65.69%"
        }
    else:
        result = {
            "Examination": "UG(B.Tech/B.E.)",
            "University" : "university of Mumbai",
            "Institute"  : "MGM's College of Engineering & Technology",
            "year"       : "2018",
            "Marks"      : "6.75/10"
        }
    return jsonify(result)



if __name__ == "__main__":
    app.run(debug=True)
    # this debug = true detects the change and it works on it sponteniously
