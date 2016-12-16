#!/usr/bin/python
#
#  Static Panda Script!
#  This script serves images that include panda 
#  You should know the specific path in order to make the script work
#
#  Created by - Alon Almog


from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
from os import curdir, sep

# Setting the port number for the webservice
web_port_number = 8080

# Class for the HttpRequests
class PandaHandler(BaseHTTPRequestHandler):

    #Handler for the GET requests
    def do_GET(self):

        try:
            # By default - return nothing
            sendReply = False
            if self.path.endswith("small.jpg"):
                mimetype='resources/jpg'
                sendReply = True
            if self.path.endswith("big.jpg"):
                mimetype='resources/jpg'
                sendReply = True

            if sendReply == True:
                # Open the static file requested and send it
                f = open(curdir + sep  +"/resources/"+self.path)
                self.send_response(200)
                self.send_header('Content-type',mimetype)
                self.end_headers()
                self.wfile.write(f.read())
                f.close()
            return

        # Catch the error and send "No Found" message
        except IOError:
            self.send_error(404,'File Not Found: %s' % self.path)

try:

    server = HTTPServer(('', PORT_NUMBER), PandaHandler)
    print 'Started http server on port ' , PORT_NUMBER
    server.serve_forever()


except Exception as e:
    print "An exception was thrown!"
    print str(e)




