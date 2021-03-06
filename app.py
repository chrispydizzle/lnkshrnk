import flask
import hash_store

app = flask.Flask(__name__)
store = hash_store.UrlStore()


@app.route('/')
def index():  # put application's code here
    content: str = 'https://dogeplanet.com/asdjfaskbhjfkjhasdfhgkjasflasdjfjkdllbslabvalbhslbfalhbsfdk'
    short_url = store.shrink_url(content)
    long_url = store.unshrink_url(short_url)
    return flask.jsonify({'short_url': short_url, 'long_url': long_url})


@app.get('/go/<short_url>')
def go(short_url: str):
    long_url = store.unshrink_url(short_url)
    return flask.redirect(long_url)


@app.post('/shrink')
def shrink():  # put application's code here
    content = flask.request.json
    short_url = store.shrink_url(content['url'])
    baseurl = flask.request.host_url
    return flask.jsonify({"url": '{0}go/{1}'.format(baseurl, short_url)})


@app.post('/unshrink')
def unshrink():  # put application's code here
    content = flask.request.json
    full_url: str = content['url']
    baseurl = flask.request.host_url
    hashval = full_url.removeprefix('{0}go/'.format(baseurl))
    long_url = store.unshrink_url(hashval)
    return flask.jsonify({"url": long_url})


if __name__ == '__main__':
    app.run()
