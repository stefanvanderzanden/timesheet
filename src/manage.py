#!/usr/bin/env python
import os, sys

IMPORT_HOME = os.path.abspath(os.path.dirname(__file__))
sys.path.append(os.path.join(IMPORT_HOME, "data_apps"))
sys.path.append(os.path.join(IMPORT_HOME, "common_apps"))

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
