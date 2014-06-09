from twisted.internet import ssl, reactor

from ..config import Config
from .factory import PYOPFactory

class ServerDaemon:
    """Monitors client services."""
    
    _DEFAULTS = {
        'server': {
            'host': '127.0.0.1',
            'port': '9886',
        },
        'ssl': {
            'key_file': 'server.key',
            'crt_file': 'server.crt',
        },
    }
    
    def __init__(self):
        """Initializes the server daemon."""
        self._config = Config('server.json', self._DEFAULTS)
        reactor.listenSSL(self._config.get('server/port'),
                          PYOPFactory(),
                          ssl.DefaultOpenSSLContextFactory(
                              self._config.get('ssl/key_file'),
                              self._config.get('ssl/crt_file'),
                          ))
    
    def run(self):
        """Enters the event loop of the server."""
        reactor.run()

