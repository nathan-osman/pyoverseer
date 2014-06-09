from twisted.internet.protocol import Factory

from ..jsonreceiver import JSONReceiver

class PYOP(JSONReceiver):
    """Client implementation of the PYOP protocol."""

class PYOPFactory(Factory):
    """Factory for PYOP sockets."""
    
    def buildProtocol(self, addr):
        """Create a new protocol instance."""
        return PYOP()
    
    def clientConnectionLost(self, connector, reason):
        """Automatically reconnect to server when connection is lost."""
        connector.connect()

