import zlib


class UrlStore:
    def __init__(self):
        self.urls = {}

    def shrink_url(self, url: str) -> str:
        adler = zlib.adler32(url.encode('ascii'))
        adler_hash = str(hex(adler)).removeprefix('0x')
        self.store(adler_hash, url)
        return adler_hash

    def store(self, adler_hash, url):
        self.urls[adler_hash] = url

    def unshrink_url(self, adler_hash) -> str:
        return self.urls[adler_hash]
