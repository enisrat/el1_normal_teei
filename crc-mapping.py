import sys
import re

def map_crc(trace_file, memmap_file, output_file):
    crc_map = {}
    with open(memmap_file, "r") as f:
        for line in f:
            parts = line.strip().split()
            if len(parts) >= 2:
                crc = parts[0].lower()
                fname = parts[-1] # parts = ["e79a2fe5", "ree_agent"]
                crc_map[crc] = fname # fname = "ree_agent"

    # parse trace-file
    with open(trace_file, "r") as f_in, open(output_file, "w") as f_out:
        for line in f_in:
            m = re.search(r"CRC\s+([0-9a-fA-F]+)", line) # m -> match
            if m:
                crc = m.group(1).lower()    # m.group(1) = "E79A2FE5"   ->    m.group(1).lower() = "e79a2fe5"
                if crc in crc_map:
                    f_out.write(f"{line.strip()} -> {crc_map[crc]}\n")
                else:
                    f_out.write(f"{line.strip()} -> [no mapping]\n")
            else:
                f_out.write(line)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script_name.py  <trace_file> <memmap_file> <output_file>")
        sys.exit(1)
    
    trace_file = sys.argv[1]
    memmap_file = sys.argv[2]
    output_file = sys.argv[3]
    
map_crc(trace_file, memmap_file, output_file)