from json import load

class Config:
    """Manages lookup and retrieval of configuration data."""
    
    DEFAULT_HOST = '127.0.0.1'
    DEFAULT_PORT = 9668
    
    def __init__(self):
        """Initialize the configuration."""
        self.reload()
    
    def _filename(self):
        """Return the filename of the configuration file."""
        return '/etc/pyoverseer/config.json'
    
    def reload(self):
        """Reload the configuration from disk."""
        with open(self._filename(), 'r') as f:
            self._config = load(f)
    
    def server(self):
        """Return the host and port of the server."""
        try:
            return (
                self._config['server']['host'],
                self._config['server']['port'],
            )
        except KeyError:
            return (DEFAULT_HOST, DEFAULT_PORT)
    
    def services(self):
        """Return a list of monitored services."""
        return self._config.get('services', {})
        
