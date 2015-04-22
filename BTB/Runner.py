__author__ = 'Stephen "TheCodeAssassin" Hoogendijk'

import configparser
import os
import sys
from BTB import Validator as Validator

class Runner:

    quiet = False
    simulate = False
    config = None
    arguments = []
    validator = None
    phalcon_git_url = None
    operating_system = None
    version = None

    def __init__(self, options, arguments, phalcon_git_url):

        """

        :param options:
        :param arguments:
        """
        if options.quiet:
            self.quiet = True

        if options.simulate:
            self.simulate = True

        if options.simulate:
            self.simulate = True

        if options.operating_system:
            self.operating_system = options.operating_system

        self.version = options.version

        # set the config file if passed as an option
        if options.config is not None:
            configfile = options.config
        else:
            configfile = os.path.abspath('config.ini')

        print('=> Using config file %s' % configfile)

        if not os.path.exists(configfile):
            print('Given config file was not found in the given path')
            exit(1)

        print('=> Config file found, verifying...')

        # set the config file
        cfg = self.validate_config(configfile)
        self.config = cfg

        self.arguments = arguments
        self.phalcon_git_url = phalcon_git_url

    def validate_config(self, configfile):
        """

        :param configfile:
        """
        cfg = configparser.ConfigParser()
        try:
            cfg.read(configfile)
        except configparser.ParsingError as exc:
            print('Could not read configuration: %s' % exc)
            sys.exit(1)

        if not cfg.has_section('endpoints'):
            print('No endpoints section found in config')
            sys.exit(1)

        if not cfg.has_section('main'):
            print('No main section found in config')
            sys.exit(1)

        if not cfg.has_option('main', 'gnpughome'):
            gnupghome = os.path.join(os.path.expanduser('~'), '.gnupg')
        else:
            gnupghome = cfg.get('main', 'gnupghome')


        if not os.path.exists(gnupghome):
            print('gnupg home %s does not exist! Please configure your gnupg' % gnupghome)
            sys.exit(1)

        print('=> Configuration passed initial test')

        return cfg

    def start_validation(self, version, operating_system):
        self.validator = Validator.Validator(version, operating_system, self)

        self.validator.validate()

    def run(self):

        # checkout the git repository of the given version
        print(self.version)

        pass
