"""
Flask App Init: https://www.youtube.com/watch?v=MwZwr5Tvyxo&list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH
"""

from flask import Flask, render_template, request, url_for, redirect
import Requests
app = Flask(__name__)
peers = [
  "AAPL",
  "EMC",
  "HPQ",
  "DELL",
  "WDC",
  "HPE",
  "NTAP",
  "CPQ",
  "SNDK",
  "SEG"
]

@app.route("/")
def home():
    return render_template('home.html',peers=peers, length=len(peers)) #ADD HTML

@app.route("/about")
def about():
    return "<h1>About Page</h1>" #ADD HTML

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
    return render_template('final.html', variable='12345', variable2='4523')


if __name__ == "__main__":
    app.run(debug=True)
