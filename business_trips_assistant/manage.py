#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from dotenv import load_dotenv


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'business_trips_assistant.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    load_dotenv()
    variables_env = ['CHROMEDRIVER', 'PASSWORD_DATA_BASE', 'NAME_DATA_BASE',
                     'USER_DATA_BASE', 'HOST_DATA_BASE', 'PORT_DATA_BASE']
    for variable in variables_env:
        assert os.environ.get(variable) is not None
    main()
