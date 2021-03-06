#!/usr/bin/python3

__author__ = 'Stephen "TheCodeAssassin" Hoogendijk'

import gnupg
import os
import optparse
import sys
import re
import tempfile
from time import sleep
from urllib import request

# import optparse, re, os, time, urllib2, ConfigParser, subprocess
from BTB import Runner as Runner
from BTB.OutputControl import OutputControl

def run():

#    stable_channel_url = 'https://launchpad.net/~phalcon/+archive/ubuntu/stable/+packages?field.name_filter=&field.status_filter=&field.series_filter='

    print('=> Bob the Builder has been summoned to build the package')

    p = optparse.OptionParser()
    p.add_option('--simulate', '-s', action="store_true", help="Just run a simulation of a package upload")
    p.add_option('--quiet', '-q', action="store_true", help="Do a silent run")
    p.add_option('--config', '-c', default=None, help="Use an alternative configuration file")
    p.add_option('--version', '-v', help="Build specific version of Phalcon")
    p.add_option('--os', '-o', help="Build only the given operating system")
    p.add_option('--temp', '-t', default=None, help="Use a different temp folder for storing files")

    options, arguments = p.parse_args()

    version = options.version
    operating_system = options.os

    supported_operation_systems = ['trusty', 'precise', 'vivid', 'raring', 'utopic']

    if operating_system and operating_system not in supported_operation_systems:
        print('OS is not supported by BOB' % operating_system)
        sys.exit(1)

    if not options.temp:
        tmp_folder = tempfile.gettempdir()
    else:
        tmp_folder = options.temp

    print('=> Using temporary folder %s' % tmp_folder)

    if not os.access(tmp_folder, os.O_RDWR):
        OutputControl.fail('Error: Cannot read/write from temp folder! (folder used: %s)' % tmp_folder)
        sys.exit(1)

    if version is None:
        OutputControl.fail('Error: Please provide a version to build for (-v VERSION)')
        sys.exit(1)

    if not re.match('^\d{1,3}\.\d{1,3}(\.\d{1,3})?$', str(version)):
        OutputControl.fail('Error: Version %s does not appear to be a valid version number (x.x or x.x.x)' % version)
        sys.exit(1)

    print('=> Trying to build a package for Phalcon %s...' % version)
    sleep(1)

    # start validation of the phalcon version
    runner = Runner.Runner(options, arguments)
    runner.start_validation()
    runner.run()


if __name__ == '__main__':
    run()


