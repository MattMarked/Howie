# Command to build:
from distutils.core import setup
import glob
import py2exe

setup(name="Howie",
	author="Cort Stratton",
	author_email="cort@users.sourceforge.net",
	description="Howie The Chatterbot",
	url="http://howie.sourceforge.net/",
	scripts=["runme.py"],
	data_files=[
		("scripts", glob.glob("scripts\\*.py")),
		("standard", glob.glob("standard\\*.aiml")),
		(".", ("std-startup.xml", "README.txt", "CHANGES.txt", "my-howie.aiml", "howie.ini")),	  
	],
)
