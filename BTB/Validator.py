__author__ = 'Stephen "TheCodeAssassin" Hoogendijk'

import os
import re
import subprocess
import sys
from urllib import request

class Validator:

    version = None
    release = None
    release_path = None
    runner = None

    def __init__(self, version, release, runner):
        """

        :param version:
        :param release:
        """
        self.version = version
        self.release = release
        self.runner = runner

    def validate(self):

        # validate the changelog file
        self.check_changelog()

        # validate the release that needs to be tagged
        self.check_version()


    def check_changelog(self):


        changelog_path = os.path.join(self.release_path, 'changelog.json')
        print('=> Checking changelog file %s' % changelog_path)
        if not os.path.exists(changelog_path):
            print('Error: Could not find a changelog.json file in the release folder')
            sys.exit(1)

        changelog = open(changelog_path)

        # changelog_lines = changelog.readlines()
        # num = 0
        #
        # # regex for change lines
        # changeline_regex = '^\s\s\*\s.*|\s\s\s\s.*$'
        #
        # # a valid count of 2 is required before a changelog can be considered valid
        # valid_count = 0
        # valid_blocks = 0


        # try:
        #
        #     for line in changelog_lines:
        #
        #         if self.version + '-ppa' in line:
        #             raise ValueError('Version %s has been found in the changelog, you cannot use this script to reupload packages!' % self.version)
        #
        #         # only validate full blocks
        #         try:
        #             next_line = changelog_lines[num + 1]
        #             next_next_line = changelog_lines[num + 2]
        #         except IndexError:
        #             break
        #
        #         # start with validating the first line
        #         if re.match('^.*(\d{1,3}\.\d{1,3}(\.\d{1,3})?).*?'+self.release+';\surgency=(low|medium|high|emergency|critical)$', line):
        #             # one changelog line is minimum
        #             if not re.match(changeline_regex, next_line) and not re.match(changeline_regex, next_next_line):
        #                 raise ValueError('Line after release line not a change, one change line is required (line %d)' % (num + 1))
        #             else:
        #                 valid_count += 1
        #
        #         # if a line matches a change line, next should be the author line
        #         if re.match(changeline_regex, line):
        #             if not re.match(changeline_regex, next_line):
        #                 if not re.match('^\s--\s.*?<.*?>\s\s.*$', next_next_line):
        #                     raise ValueError('Change block should end with a valid author line (line %d)' % (num + 1))
        #                 else:
        #                     valid_count += 1
        #
        #         # every two valid counts equals a valid block
        #         if valid_count is 2:
        #             valid_count = 0
        #             valid_blocks += 1
        #
        #         # increate the iterator count
        #         num += 1
        #
        #     if valid_blocks is 0 or valid_count is not 0:
        #         raise ValueError('file does not contain a fully valid block or at least one invalid block!')
        #
        #
        # except ValueError as ex:
        #     print('Error: changelog is not valid! Reason: %s' % ex)
        #     sys.exit(1)


        print('=> Changelog file appears to be valid')

    def check_version(self):
        print('=> Checking version %s...' % self.version)

        try:
            request.urlopen(self.runner.phalcon_git_url + '/tree/' + self.version)
        except request.URLError:
            print('Error: cannot find version %s in the remote repository!' % self.version)


        print('=> Version %s is a valid version' % self.version)