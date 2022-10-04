from flask import Flask, redirect, url_for, render_template, request, jsonify
import telegram_script

app = Flask(__name__)

# def home():
#     return render_template("index.html")

@app.route("/", methods=["POST", "GET"])
def home_post():
    if request.method == "POST":
        textField = request.form['textbox']
        print(request.form.get('textbox'))
        telegram_script.send(str(textField), -605164661)
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
