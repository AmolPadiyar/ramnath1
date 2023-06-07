from flask import Flask,jsonify,render_template,request

from packages.utils import MedicalInshorance


app = Flask(__name__)

@app.route("/")
def home():
    print('welcome********')
    return render_template("show.html")

@app.route("/show_html_page" , methods=['POST','GET'])
def form_show():
    if request.method == "GET":
        print("Test--we are in get method")
    
        age = int(request.args.get("age"))
        sex = (request.args.get("sex"))
        bmi = float(request.args.get("bmi"))
        children = int(request.args.get("children"))
        smoker = request.args.get("smoker")
        region = request.args.get("region")

        med_ins = MedicalInshorance(age, sex, bmi, children, smoker, region)
        charges = med_ins.predict_output()
    
        return render_template("show.html", prediction = charges)
    
    
    
app.run(host="0.0.0.0",port=5005,debug=False)