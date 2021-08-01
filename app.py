import flask
import smaz
import base64


app = flask.Flask(__name__)


@app.route('/')
def index():  # put application's code here
    content = 'https://dogeplanet.com'
    compressed: bytes = smaz.compress(content)
    b64_bytes: bytes = base64.b64encode(compressed)
    short_url: str = b64_bytes.decode('ascii')
    print(short_url)
    b64_bytes_enc = short_url.encode('ascii')
    b64decoded_compressed: bytes = base64.b64decode(b64_bytes_enc)
    long_url: str = smaz.decompress(b64decoded_compressed)
    origin_url: str = smaz.decompress(compressed)
    print(long_url)
    print(origin_url)


@app.post('/shrink')
def shrink():  # put application's code here
    content = flask.request.json
    compressed: bytes = smaz.compress(content['url'])
    b64_bytes: bytes = base64.b64encode(compressed)
    short_url: str = b64_bytes.decode('ascii')
    print(short_url)
    return flask.jsonify({"url": short_url})


@app.post('/unshrink')
def unshrink():  # put application's code here
    content = flask.request.json
    b64_bytes_enc = content['url'].encode('ascii')
    b64decoded_compressed: bytes = base64.b64decode(b64_bytes_enc)
    long_url: str = smaz.decompress(b64decoded_compressed)
    return flask.jsonify({"url": long_url})


if __name__ == '__main__':
    app.run()
