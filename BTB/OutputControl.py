__author__ = 'Stephen "TheCodeAssassin" Hoogendijk'

class OutputControl:

    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    @staticmethod
    def fail(message):
        """

        :param message:
        :return:
        """
        OutputControl.printmsg(message, OutputControl.FAIL)

    @staticmethod
    def success(message):
        """

        :param message:
        :return:
        """
        OutputControl.printmsg(message, OutputControl.OKGREEN)

    @staticmethod
    def printmsg(message, color):
        """

        :type color: str
        :type message: str
        :type self: object
        """
        print(color + message + OutputControl.ENDC)
