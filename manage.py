#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    from django.core.management import execute_from_command_line
    from demo_tmp.settings import read_env
    read_env()
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "demo_tmp.settings")
    execute_from_command_line(sys.argv)
