from flask import Flask, render_template, jsonify, url_for, request

app = Flask('my server')


@app.route('/index/<title>')
@app.route('/<title>')
def index(title):
    return render_template('base.html', title=title)


@app.route('/training/<prof>')
def training(prof):
    params = {}
    params['prof'] = prof
    params['route_to_engineer'] = url_for('static', filename='img/starship_engineer_trainers.png')
    params['route_to_science'] = url_for('static', filename='img/starship_science_simulators.png')
    return render_template('training.html', **params)


@app.route('/list_prof/<list>')
def list_prof(list):
    if list not in ['ul', 'ol']:
        return jsonify({'error': 'Parameter list must be "ul" or "ol"'})
    params = {}
    params['list'] = list
    return render_template('list_prof.html', **params)


@app.route('/answer')
@app.route('/auto_answer')
def answer():
    params = request.json
    return render_template('auto_answer.html', **params)


@app.route('/distribution')
def distribution():
    params = {}
    params['colonists'] = request.json
    params['path_to_static'] = url_for('static')
    return render_template('distribution.html', **params)


if __name__ == '__main__':
    app.run('localhost', 8080)
