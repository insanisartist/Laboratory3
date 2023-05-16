from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/', methods=['post', 'get'])
def form():
    if request.method == 'POST':
        p = float(request.form.get("num_1"))
        r = float(request.form.get("num_2"))
        n = float(request.form.get("num_3"))
        t = float(request.form.get("num_4"))
    return render_template('index.html',ans=int(p*(1+(r/n))**(n*t)))

if __name__ == "__main__":
    app.run(debug=True)