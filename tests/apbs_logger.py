#! /usr/bin/env python

"""
Provides a logger that prints regular messages and logger messages.
Logged messages are typically written to a log file, while regular messages
typically are printed to stdout
"""

import sys


class Logger:
    def __init__(self, message_fd, logfile_fd):
        self.message_fd = message_fd
        self.logfile_fd = logfile_fd

    def message(self, message):
        self.message_fd.write(message)

    def log(self, message):
        self.logfile_fd.write(message)

    def both(self, message):
        self.message(message)
        self.log(message)


if __name__ == "__main__":
    sys.stderr.write(
        f"The python source file {sys.argv[0]} is a module and not runnable"
    )
    sys.exit(1)
