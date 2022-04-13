from flask import Flask, render_template, url_for, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/user/<string:name>/<int:id>/')
def user(name, id):
    return 'Hello, ' + name + '. Your ID: ' + str(id)


@app.route('/game', methods=['GET'])
def game():
    if request.method == 'GET':
        name_param = request.args.get('name')

    if name_param is None:
        name_param = ""

    return render_template(
        'game.html',
        name=name_param,
        method=request.method
    )


@app.context_processor
def inject_globals():
    return {
        "greeting": [
            "Добрый день!",
            "Доброе утро!",
            "Добрый вечер!",
            "Здравствуйте!"
        ]
    }


if __name__ == "__main__":
    app.run(debug=True)
