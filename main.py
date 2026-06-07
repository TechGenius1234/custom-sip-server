import threading
from database import Database
from sip_engine import SIPServer
from web_admin import run_web_admin
from twisted.internet import reactor
import sys

def start_sip_server(db):
    try:
        server = SIPServer(db)
        server.run()
        if not reactor.running:
            reactor.run(installSignalHandlers=False)
    except Exception as e:
        print(f"SIP Server Error: {e}")

if __name__ == "__main__":
    db = Database()
    
    # Start SIP Server in a separate thread
    sip_thread = threading.Thread(target=start_sip_server, args=(db,), daemon=True)
    sip_thread.start()
    
    print("Custom SIP Server is running...")
    print("Web Admin available at http://localhost:8080")
    
    # Run Web Admin in the main thread
    try:
        run_web_admin(db, port=8080)
    except KeyboardInterrupt:
        print("Shutting down...")
        sys.exit(0)
