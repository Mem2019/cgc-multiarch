import os
import re
from typing import Set

builtin_names = ["memcpy", "memmove", "memset", "memcmp", "memchr",
	"strlen", "strcpy", "strncpy", "strchr", "strsep", "strcmp",
	"strncmp", "strcasecmp", "strncasecmp", "strcat", "strdup",
	"fdprintf", "sprintf", "strtol", "strtoul", "malloc", "calloc",
	"realloc", "free", "malloc_size", "exit", "main"]
builtin_defs = []
for bn in builtin_names:
	builtin_defs.append((bn.encode(),
		re.compile(b"\\b%s\\([^\\)]*\\)[\\n\\t ]*\\{" % bn.encode())))
del builtin_names

def gather_builtin_defs(content: bytes, defined: Set[bytes]):
	for name, dr in builtin_defs:
		if re.search(dr, content):
			defined.add(name)

def replace_builtins(code_dir: str):
	defined = set()
	for dirpath, _, filenames in os.walk(code_dir):
		for filename in filenames:
			file_path = os.path.join(dirpath, filename)
			with open(file_path, 'rb') as fd:
				gather_builtin_defs(fd.read(), defined)

	print(code_dir, b' '.join(defined).decode())
	for dirpath, _, filenames in os.walk(code_dir):
		for filename in filenames:
			file_path = os.path.join(dirpath, filename)
			with open(file_path, 'rb') as fd:
				content = fd.read()
			for bn in defined:
				content = re.sub(b"\\b" + bn + b"\\b", b"cgc_std_" + bn, content)
				content = re.sub(b"cgc_std_" + bn + b"\\.h", bn + b".h", content)
			with open(file_path, 'wb') as fd:
				fd.write(content)

def main():
	cgc_re = re.compile("[A-Z0-9]+_[0-9]+")
	cgc_src = "cgc-challenge-corpus"
	for cgc in os.listdir(cgc_src):
		if re.match(cgc_re, cgc):
			replace_builtins(os.path.join(cgc_src, cgc))

if __name__ == "__main__":
	main()