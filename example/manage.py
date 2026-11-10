#!/usr/bin/env python
import os
import sys
from pathlib import Path

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "example.settings")

    from django.core.management import execute_from_command_line

    # Allow starting the app without installing the module, and make the
    # apps inside ``example/`` (e.g. ``currencies``) importable directly.
    here = Path(__file__).resolve().parent
    sys.path[:0] = [str(here.parent), str(here)]

    execute_from_command_line(sys.argv)
