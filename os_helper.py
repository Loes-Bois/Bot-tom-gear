import os
import sys

# Get a environment variable
# If it doesnt exist 'None' will be returned
def get_env_var(var):
    if (var in os.environ):
        return os.environ.get(var)
    else:
        return None 