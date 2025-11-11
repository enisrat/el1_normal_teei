import struct
import os

def unpack_archive(file_path, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    
    with open(file_path, 'rb') as f:
        # Read number of entries and array offset
        f.seek(0x14)
        num_entries = struct.unpack('<I', f.read(4))[0]
        array_offset = struct.unpack('<I', f.read(4))[0]
        
        # Read all array entries
        entries = []
        f.seek(array_offset)
        for _ in range(num_entries):
            entry = f.read(16)
            blob_offset, blob_end, name_offset, _ = struct.unpack('<IIII', entry)
            entries.append((blob_offset, blob_end, name_offset))
        
        # Process each entry
        for blob_offset, blob_end, name_offset in entries:
            # Read blob name
            f.seek(name_offset)
            name = b''
            while (byte := f.read(1)) != b'\x00':
                name += byte
            name = name.decode('utf-8')

            
            if "/" in name:
                os.makedirs(output_dir + "/" + "/".join(name.split("/")[:-1]), exist_ok=True)

            # Extract blob
            f.seek(blob_offset)
            blob_data = f.read(blob_end-blob_offset)
            
            # Save blob to file
            with open(os.path.join(output_dir, name), 'wb') as out_file:
                out_file.write(blob_data)

if __name__ == '__main__':
    import sys
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <archive_file> <output_directory>")
        sys.exit(1)
    unpack_archive(sys.argv[1], sys.argv[2])