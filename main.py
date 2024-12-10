from flask import Flask, make_response, jsonify, abort
from Controllers.App import App


flask = Flask(__name__)
app = App()


@flask.get('/')
def page_post_list():
	html = app.view.get_page_post_list()
	return make_response(html)


@flask.get('/js/<name>')
def get_js(name):
	js = app.view.load_js(name)
	if js is None:
		abort(404)
	res = make_response(js)
	res.headers['Content-Type'] = 'text/javascript'
	return res


@flask.post('/api/get_post_list')
def api_get_post_list():
	posts = app.api.get_post_list()
	return jsonify({'status': 'OK', 'data': posts})


if __name__ == '__main__':
	flask.run(host='127.0.0.1', port=8000)
