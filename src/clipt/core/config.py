
import configparser
import os

class ConfigLoader:

    def __init__(self):
        self._parser = configparser.ConfigParser()
        self.home = os.path.expanduser('~/.clipt')
       
        # TODO try..except? what does read() do on error? 
        if os.path.exists(self.home + '/config'):
            self._parser.read(self.home + '/config')

        self._default_config = ({
            'main' : ({
                'storage' : 'local',
            }),
            'local' : ({
                'database' : self.home + '/data'
            })
        })

        self.resolveConfig()

    def resolveConfig(self):
        self.config = self._default_config

        if len(self._parser.sections()) > 0:
            for key in self.config:
                if key in self._parser.sections():
                    self.config[key] = dict(self._parser[key])
