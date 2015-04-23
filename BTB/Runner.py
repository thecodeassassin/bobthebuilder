__author__ = 'Stephen "TheCodeAssassin" Hoogendijk'

import os
import sys
import gnupg
from BTB import Validator as Validator

class Runner:

    quiet = False
    simulate = False
    config = None
    arguments = []
    validator = None
    operating_system = None
    git_url = None
    version = None
    gnupghome = None
    stable_channel_url = None

    def __init__(self, options, arguments):

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

        if options.os:
            self.operating_system = options.os

        self.version = options.version
        self.options = options

        self.arguments = arguments

    def start_validation(self):

        self.validator = Validator.Validator(self.version, self.operating_system, self)
        self.validator.validate()



    def run(self):

        # checkout the git repository of the given version
        print(self.version)

        # gpg = gnupg.GPG(gnupghome=self.gnupghome)

        print("\n=>")

        pass
