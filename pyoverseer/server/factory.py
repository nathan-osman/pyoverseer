from twisted.internet.protocol import Factory

from ..jsonreceiver import JSONReceiver

class PYOP(JSONReceiver):
    """Server implementation of the PYOP protocol."""
    
    def JSONReceived(self, data):
        """Process data received from the client."""
        if not hasattr(self, '_info'):
            self._info = data
        else:
            pass # do something with performance data

class PYOPFactory(Factory):
    """Factory for PYOP sockets."""
    
    def buildProtocol(self, addr):
        """Create a new protocol instance."""
        return PYOP()

