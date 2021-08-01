import flask
import hashlib
import hash_store

app = flask.Flask(__name__)

store = hash_store.UrlStore()


@app.route('/')
def index():  # put application's code here
    content: str = 'https://dogeplanet.com/asdjfaskbhjfkjhasdfhgkjasflasdjfjkdllbslabvalbhslbfalhbsfdk'
    short_url = store.shrink_url(content)
    long_url = store.unshrink_url(short_url)
    return flask.jsonify({'short_url': short_url, 'long_url': long_url})


@app.post('/shrink')
def shrink():  # put application's code here
    content = flask.request.json
    short_url = store.shrink_url(content['url'])
    print(flask.request.host)
    return flask.jsonify({"url": short_url})


@app.post('/unshrink')
def unshrink():  # put application's code here
    content = flask.request.json
    long_url = store.unshrink_url(content['url'])
    print(flask.request.host)
    return flask.jsonify({"url": long_url})


if __name__ == '__main__':
    app.run()
