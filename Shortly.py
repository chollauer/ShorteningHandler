from aiohttp import web

HOST = "127.0.0.1"
PORT = 15001
SHORT_URL_DOMAIN = "http://short.est/"

class ShorteningHandler:
    def __init__(self):
        self.dict_short_to_long = {}
        self.dict_long_to_short = {}
        self.next_id = 1
        self.alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_"
        self.base = len(self.alphabet)

    async def encode_handler(self, request):
        original_url = request.match_info['original_url']
        return web.json_response({"shortened_url": self.encode(original_url)})

    async def decode_handler(self, request):
        short_url = request.match_info['short_url']
        return web.json_response({"original_url": self.decode(short_url)})

    def encode(self, long_url):
        # Check if long/original URL is already contained in storage
        if long_url in self.dict_long_to_short:
            return self.dict_long_to_short[long_url]
        else:
            short_string = self._encode_base_64()
            self.dict_long_to_short[long_url] = short_string
            self.dict_short_to_long[short_string] = long_url
            return short_string

    # Encode self.next_id into base-64 string
    def _encode_base_64(self):
        short_string = [SHORT_URL_DOMAIN]
        current_id = self.next_id
        self.next_id += 1
        while current_id > 0:
            short_string.append(self.alphabet[current_id % self.base])
            current_id = current_id // self.base
        return "".join(short_string)

    def decode(self, short_url):
        try:
            return self.dict_short_to_long[short_url]
        except KeyError:
            raise web.HTTPBadRequest(reason="Short URL not found!")

    def start_server(self):
        app = web.Application()
        app.add_routes([
            web.get('/encode/{original_url:.*}', self.encode_handler),
            web.get('/decode/{short_url:.*}', self.decode_handler)
        ])
        web.run_app(app, host=HOST, port=PORT)


if __name__ == '__main__':
    ShorteningHandler().start_server()
