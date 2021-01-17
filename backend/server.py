from flask import Flask, render_template, request, url_for, redirect
import Requests
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html') #ADD HTML

@app.route("/about")
def about():
    return render_template('about.html') #ADD HTML

@app.route("/analysis", methods=["POST", "GET"])
def analysis():
    if request.method == "POST":
        print('1')
        stock_name = request.form['nm']



        ##INSERT ANALYSIS FUNCTIONS



        print(type(stock_name))
        print('1')
        return redirect(url_for('stonk', stocks=stock_name))
    else:
        return render_template('analysis.html')

@app.route("/analysis/<stocks>")
def stonk(stocks):
    return render_template('final.html')


if __name__ == "__main__":
    app.run(debug=True)