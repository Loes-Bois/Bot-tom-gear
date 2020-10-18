import os
import sys


# Get an environment variable
# If it doesn't exist 'None' will be returned
def get_env_var(var):
    if (var in os.environ):
        return os.environ.get(var)
    else:
        return None 