import sys
from elftools.elf.elffile import ELFFile

import itertools
def fun(a):
    a = sorted(set(a))
    b = []
    for k, g in itertools.groupby(enumerate(a), 
        key=lambda t: t[1] - t[0]):
        g = list(g)
        b.append([g[0][1], g[-1][1]]) 
    return b



if __name__ == '__main__':
	import sys
	if len(sys.argv) != 3:
		print(f"Usage: {sys.argv[0]} <physdump_0x70000000> <elf>")
		sys.exit(1)

	listpa = []

	with open(sys.argv[1], "rb") as f:
		mem = f.read()

	with open(sys.argv[2], "rb") as f:
		elfdata = f.read()
	with open(sys.argv[2], "rb") as f:
		elffile = ELFFile(f)
		for segment in elffile.iter_segments():
			header = segment.header			
			if header["p_flags"] == 0x5:
				off = header["p_offset"]
				sz = header["p_filesz"]

				for coff in range(off, off+sz, 4096):
					found=False
					for poff in range(0, len(mem), 4096):
						if elfdata[coff:coff+4096] == mem[poff:poff+4096]:
							print(f"0x{0x70000000+poff:x}")
							listpa.append(0x70000000+poff)
							found=True
							break
					if not found:
						print(f"File page @off 0x{coff:x} not found!")
		
	
	listpa = sorted(set(listpa))
	ranges = []

	firsta = listpa[0]
	olda = firsta
	for a in listpa[1:]:
		if a-olda == 4096:
			olda += 4096
		else:
			ranges.append( (firsta, olda+4096) )
			print(f"new range: 0x{firsta:x} - 0x{olda+4096:x}")
			firsta = a
			olda = a

	ranges.append( (firsta, olda+4096) )
	print(f"last range: 0x{firsta:x} - 0x{olda+4096:x}")

