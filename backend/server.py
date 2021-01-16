from flask import Flask, render_template, request, url_for
app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template('base.html') #ADD HTML

@app.route("/about")
def about():
    return "<h1>About Page</h1>" #ADD HTML

@app.route("/analysis", methods=["POST", "GET"])
def analysis():
    if request.method == "POST":
        stonk = request.form['stock_name']
        return redirect(url_for('stock'), stocks=stonk)
    else:
        return render_template('base.html')

@app.route("/analysis/<stocks>")
def stonk(stocks):
    return f"{stocks}"


if __name__ == "__main__":
    app.run(debug=True)