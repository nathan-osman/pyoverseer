from collections import Mapping
from json import load
from os import path

class Config:
    """Manages lookup and retrieval of configuration data."""

    class ConfigMissingError(Exception):
        """Configuration file was not found."""

    def __init__(self, filename, defaults={}):
        """Initialize the configuration."""
        self._config = defaults
        self._update(self._config, self._load(filename))

    def __contains__(self, key):
        """Indicate whether the specified key exists."""
        return key in self._config

    def __getitem__(self, key):
        """Return the value for the specified key."""
        return self._config[key]

    def _find_config(self, filename):
        """Attempt to find the configuration file."""
        for directory in ['/etc/pyoverseer', '.']:
            if path.isfile(path.join(directory, filename)):
                return path.join(directory, filename)
        raise ConfigMissingError('Configuration file %s does not exist.' % filename)

    def _load(self, filename):
        """Load the configuration from disk."""
        with open(self._find_config(filename), 'r') as f:
            return load(f)

    def _update(self, d, u):
        """Recursive update from http://stackoverflow.com/a/3233356/193619."""
        for k, v in u.iteritems():
            d[k] = self._update(d.get(k, {}), v) if isinstance(v, Mapping) else u[k]
        return d
