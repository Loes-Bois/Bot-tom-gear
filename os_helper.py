import os
import sys

# Get a environment variable
# If it doesnt exist 'None' will be returned
def getEnvVar(var):
    if (var in os.environ):
        return os.environ.get(var)
    else:
        return None 