"""
Flask App Init: https://www.youtube.com/watch?v=MwZwr5Tvyxo&list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH
"""

from flask import Flask, render_template, request, url_for, redirect
import Requests
import ml
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
    return render_template('about.html')

@app.route("/analysis", methods=["POST", "GET"])
def analysis():
    if request.method == "POST":
        stock_name = request.form['nm']
        ##INSERT ANALYSIS FUNCTIONS
        return redirect(url_for('stonk', stocks=stock_name))
    else:
        return render_template('analysis.html')

@app.route("/analysis/<stocks>")
def stonk(stocks):
    a = ml.Analysis(stocks)
    a.findFlairs()
    score = round(a.return_prediction(),3)

    if score >= -1 and score <=1:
        assess ='Hold'
    elif score > 1:
        assess ='Buy'
        if score > 2:
            assess= 'Strong Buy'
    elif score < -1:
        assess = "Sell"
        if score < -2:
            assess = 'Strong Sell'
    
        
    return render_template('final.html', assess=assess, stocks=stocks, score=score)


if __name__ == "__main__":
    app.run(debug=True)
