from flask import Flask, render_template
import bot

app = Flask(__name__)

@app.route('/',methods=["POST"])
def home{}: 
        if request.method == "POST":
               message = request.form["message"]
               output = bot.send_message(message)
               return jsonify({"output": output})
       return render_template('home.html')

if __name__=='__main__':
        app.run

