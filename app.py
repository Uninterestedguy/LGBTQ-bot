from flask import Flask, render_template, request, jsonify, url_for
import bot

app = Flask(__name__)

@app.route('/index',methods=["GET","POST"])
def home(): 
        if request.method == "POST":
                message = request.form["message"]
                output = bot.send_message(message)
                return jsonify({"output": output})
        return render_template('index.html')


if __name__=='__main__':
        app.run(debug=True)

