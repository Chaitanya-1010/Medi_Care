from flask import request, jsonify, Flask, send_file, render_template

app = Flask(__name__, static_folder='Backend/static', template_folder="Backend/templates")

@app.route('/')
def index():
    # Implement login logic here
    return render_template("index.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0')
