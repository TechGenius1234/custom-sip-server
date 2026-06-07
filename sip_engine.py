import sys
from sippy.SipTransactionManager import SipTransactionManager
from sippy.SipUserAgent import SipUserAgent
from sippy.SipRequest import SipRequest
from sippy.SipResponse import SipResponse
from sippy.SipHeader import SipHeader
from sippy.SipConf import SipConf
from sippy.SipLogger import SipLogger

class SIPServer:
    def __init__(self, db):
        self.db = db
        self.config = SipConf()
        self.logger = SipLogger("SIPServer")
        # In sippy, we often subclass or use B2BUA logic
        # For a simple custom server, we'll use a Transaction Manager
        self.tm = SipTransactionManager(self.config, self.recv_request)
        self.registrations = {}

    def recv_request(self, request, t):
        method = request.getMethod()
        if method == "REGISTER":
            self.handle_register(request, t)
        elif method == "INVITE":
            self.handle_invite(request, t)
        elif method == "OPTIONS":
            t.sendResponse(request.genResponse(200, "OK"))
        else:
            t.sendResponse(request.genResponse(405, "Method Not Allowed"))

    def handle_register(self, request, t):
        to_addr = request.getHFBody("to").getUri()
        extension = to_addr.username
        
        user = self.db.get_user(extension)
        if user:
            # Check password (simplified)
            # contact = request.getHFBody("contact").getUri()
            self.registrations[extension] = True # Store registration
            response = request.genResponse(200, "OK")
            t.sendResponse(response)
            print(f"Registered extension: {extension}")
        else:
            t.sendResponse(request.genResponse(404, "User Not Found"))

    def handle_invite(self, request, t):
        to_addr = request.getHFBody("to").getUri()
        extension = to_addr.username
        print(f"Call to: {extension}")
        
        # IVR or routing logic
        if extension == "999": # IVR
            print("Routing to IVR")
            # IVR logic here
            t.sendResponse(request.genResponse(200, "OK"))
        elif extension in self.registrations:
            print(f"Routing to extension {extension}")
            t.sendResponse(request.genResponse(180, "Ringing"))
            # Routing logic
        else:
            t.sendResponse(request.genResponse(404, "Not Found"))

    def run(self):
        from twisted.internet import reactor
        print("SIP Server starting...")
        # reactor.run() # This will be called in main.py
