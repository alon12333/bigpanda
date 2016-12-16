#!/usr/bin/python
#
#  Counting Panda Script!
#  This script counts the get requests
#
#  Created by - Alon Almog

from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer

# Setting the web interface port number 
web_port_number = 8080
PandaCounter= 0 

class PandaHandler(BaseHTTPRequestHandler):
    
    #Handler for the GET request
    def do_GET(self):
        global PandaCounter 
        PandaCounter += 1
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        self.wfile.write(PandaCounter)
        return
try:
    
    server = HTTPServer(('', web_port_number), PandaHandler)
    print 'Started http server on port ' , web_port_number
    server.serve_forever()


except Exception as e:
    print "An exception was thrown!"
    print str(e)
