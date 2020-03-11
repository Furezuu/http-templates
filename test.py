from flask import Flask, render_template

app = Flask('my server')


@app.route('/index/<title>')
@app.route('/<title>')
def index(title):
    return render_template('base.html', title=title)


@app.route('/training/<prof>')
def training(prof):
    params = {}
    params['prof'] = prof
    params['img1']
    return render_template('training.html', **params)


if __name__ == '__main__':
    app.run('localhost', 8080)
