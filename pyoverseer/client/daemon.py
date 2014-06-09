from twisted.internet import ssl, reactor

from ..config import Config
from .factory import PYOPFactory

class ClientDaemon:
    """Monitors running services."""
    
    _DEFAULTS = {
        'server': {
            'host': '127.0.0.1',
            'port': '9886',
        },
        'ssl': {
            'key_file': 'client.key',
            'crt_file': 'client.crt',
        },
    }
    
    def __init__(self):
        """Initializes the client daemon."""
        self._config = Config('client.json', self._DEFAULTS)
        reactor.connectSSL(self._config.get('server/port'),
                           PYOPFactory(),
                           ssl.DefaultOpenSSLContextFactory(
                               self._config.get('ssl/key_file'),
                               self._config.get('ssl/crt_file'),
                           ))
    
    def run(self):
        """Enters the event loop of the client."""
        reactor.run()

