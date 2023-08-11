from flask import Flask, render_template, request, make_response, redirect, url_for, session

app = Flask(__name__)
app.secret_key = '123abc456'


@app.route('/')
def main():
    return redirect(url_for('signup'))


@app.route('/signup/', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        return redirect(url_for('welcome', name=name, email=email))
    return render_template('signup.html')


@app.route('/welcome/', methods=['GET', 'POST'])
def welcome():
    context = {
        'title': 'Добро пожаловать',
        'name': request.args.get('name'),
        'email': request.args.get('email')
    }
    if request.method == 'POST':
        response_1 = make_response(render_template('signup.html'))
        response_1.set_cookie(context['name'], context['email'], max_age=0)
        return response_1
    response_2 = make_response(render_template('welcome.html', **context))
    response_2.set_cookie(context['name'], context['email'])
    return response_2


if __name__ == '__main__':
    app.run(debug=True)
