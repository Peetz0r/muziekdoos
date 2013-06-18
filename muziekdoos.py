#!/usr/bin/env python2.7

import time
import youtube
import BaseHTTPServer
import config

class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):
	def do_GET(s):
		s.send_response(200)
		s.send_header("Content-type", "text/html")
		s.end_headers()
		url = youtube.search("hotel california")
		if url == False:
			url = "foobar"
		s.wfile.write("%s\n" % url)

if __name__ == '__main__':
	server_class = BaseHTTPServer.HTTPServer
	httpd = server_class((config.HOST_NAME, config.PORT_NUMBER), MyHandler)
	print time.asctime(), "Server Starts - %s:%s" % (config.HOST_NAME, config.PORT_NUMBER)
	try:
		httpd.serve_forever()
	except KeyboardInterrupt:
		pass
	httpd.server_close()
	print time.asctime(), "Server Stops - %s:%s" % (config.HOST_NAME, config.PORT_NUMBER)
