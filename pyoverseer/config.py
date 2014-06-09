from json import load
from os import path

class Config:
    """Manages lookup and retrieval of configuration data."""
    
    class ConfigMissingError(Exception):
        """Configuration file was not found."""
    
    def __init__(self, filename, defaults={}):
        """Initialize the configuration."""
        self._filename = filename
        self._defaults = defaults
        self.reload()
    
    def _find_config(self, filename):
        """Attempt to find the configuration file."""
        for directory in ['/etc/pyoverseer', '.']:
            if path.isfile(path.join(directory, filename)):
                return path.join(directory, filename)
        raise ConfigMissingError('Configuration file %s does not exist.' % filename)
    
    def _lookup(self, _dict, key):
        """Lookup a value in a dict by path."""
        for component in key.split('/'):
            _dict = _dict[component]
        return _dict
    
    def reload(self):
        """Reload the configuration from disk."""
        with open(self._find_config(self._filename), 'r') as f:
            self._config = load(f)
    
    def get(self, key):
        """Retrieve the value for the specified key."""
        try:
            return self._lookup(self._config, key)
        except KeyError:
            return self._lookup(self._defaults, key)

