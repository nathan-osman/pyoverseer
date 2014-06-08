from json import dumps, loads

from twisted.protocols.basic import LineReceiver

class JSONReceiver(LineReceiver):
    """Protocol for exchanging JSON messages."""
    
    def lineReceived(self, line):
        """Process JSON received."""
        JSONReceived(loads(line))
    
    def sendJSON(self, line):
        """Send JSON."""
        sendLine(dumps(line))
        
