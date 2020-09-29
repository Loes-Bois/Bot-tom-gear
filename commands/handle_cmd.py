# Loads all .py files from the commands directory
# Uses: https://stackoverflow.com/questions/1057431/how-to-load-all-modules-in-a-folder

from os.path import dirname, basename, isfile, join
import glob
modules = glob.glob(join(dirname(__file__), "*.py"))
__all__ = [basename(f)[:-3] for f in modules if isfile(f)
           and not f.endswith('__init__.py')]


def handle(self, message):
    # Takes in a discord.py message
    message_content = message.content[len(self.bot_keyword) + 1:]

    # Run commands files here
    # ...
