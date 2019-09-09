from flask import Flask
from flask import Response, abort, request
import requests

from config import DefaultConfig as Conf
from filters import HideDetail

app = Flask(__name__)

@app.route('/<key>/upstream.ics')
def upstream_ics(key):
    if hasattr(Conf, "direct_token") and Conf.direct_token:
        token = str(request.args.get('token'))
        if not token == Conf.direct_token:
            abort(403)
    
    upstream_url = Conf.upstreams.get(key)
    if upstream_url:
        r = requests.get(upstream_url)
        output = r.content
        if r.status_code == 200:
            return Response(output, mimetype='text/calendar')
        else:
            abort(r.status_code)
    else:
        abort(404)

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
