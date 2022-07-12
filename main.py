from flask import Flask, render_template,request
import pickle as pkl

app = Flask(__name__)
model = pkl.load(open('model.pkl','rb'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pred',methods = ["GET","POST"])
def pred():

    est_diameter_min = float(request.form.get('est_diameter_min'))
    est_diameter_max = float(request.form.get('est_diameter_max'))
    relative_velocity = int(request.form.get('relative_velocity'))
    miss_distance = float(request.form.get('miss_distance'))
    absolute_magnitude = int(request.form.get('absolute_magnitude'))

    result = model.predict([[est_diameter_min,est_diameter_max,relative_velocity,miss_distance,absolute_magnitude]])
    if result[0] == True:
        return "true"
    else:
        return "false"


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0', port=8080 )