import os
from elftools.elf.elffile import ELFFile

def get_text_size(elf: str) -> int:
	with open(elf, 'rb') as fd:
		elf = ELFFile(fd)
		for i in range(0, elf.num_sections()):
			sec = elf.get_section(i)
			if sec.name == ".text":
				return sec.header.sh_size

def main():
	bin_path = "bins/x86_64-linux-gnu"
	bin_sizes = []
	for b in os.listdir(bin_path):
		bin_sizes.append((get_text_size(os.path.join(bin_path, b)), b))
	bin_sizes.sort()
	cnt = len(bin_sizes)
	print("Number of binaries:", cnt)
	# print(bin_sizes[(cnt-20)//2 : (cnt-20)//2+20])
	beg = (cnt-20)//2
	with open("targets.txt", 'w') as fd:
		for i in range(0, 20):
			print(bin_sizes[beg + i][1], file=fd)
"""
Select 20 targets with median code sizes.
Before running this script, we should first compile all CGC binaries.
"""
if __name__ == "__main__":
	main()