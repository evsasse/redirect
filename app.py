import json
from urllib.parse import urljoin

from flask import Flask, request, abort, redirect


app = Flask(__name__)

with open('domains.json') as json_file:
    domains = json.load(json_file)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
@app.errorhandler(404)
def catch_all(path):
    host = request.host

    try:
        domain = domains[host]
    except KeyError:
        return { 'message': 'Not found', 'host': host }, 404

    incremental_path_options = request.full_path[1:] # removes first `/`
    url = urljoin(domain, incremental_path_options)

    return redirect(url, code=302)


if __name__ == '__main__':
    app.run()
