#!/usr/bin/env python
import os
import sys

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cardgame.settings")

from cards.setup import setup_constant_values

if __name__ == "__main__":

    if len(sys.argv) == 2 and sys.argv[1] == "setup":
        setup_constant_values()
    else:
        from django.core.management import execute_from_command_line
        execute_from_command_line(sys.argv)
