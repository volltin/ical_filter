from flask import Flask
from flask import Response, abort
import requests

from config import DefaultConfig as Conf
from filters import HideDetail

app = Flask(__name__)


@app.route('/<key>/filtered.ics')
def filtered_ics(key):
    upstream_url = Conf.upstreams.get(key)
    if upstream_url:
        r = requests.get(upstream_url)
        output = HideDetail(r.content).filtered()
        if r.status_code == 200:
            return Response(output, mimetype='text/calendar')
        else:
            abort(r.status_code)
    else:
        abort(404)


if __name__ == "__main__":
    app.run(debug=False, threaded=True)
