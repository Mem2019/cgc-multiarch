import os
import re

builtin_names = []

def gather_builtin_defs(content: str):
	content

def replace_builtins(code_dir: str):
	for dirpath, dirnames, filenames in os.walk(code_dir):
		for filename in filenames:
			file_path = os.path.join(dirpath, filename)

