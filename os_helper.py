import os
import sys

# Get an environment variable
# If it doesn't exist 'None' will be returned
def getEnvVar(var):
    if (var in os.environ):
        return os.environ.get(var)
    else:
        return None 