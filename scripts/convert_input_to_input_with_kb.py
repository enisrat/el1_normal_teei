import varint
import sys
import struct


with open(sys.argv[1], 'rb') as f:
	func = varint.decode_stream(f)
	sz = varint.decode_stream(f)
	buf = f.read(sz)

	bufpre = b""
	kb = b""
	bufpost = b""

	match func:
		case 4 | 0x18:
			# 01 00 00 00 10 generic keyblob header
			kbstart = buf.find(b"\x00\x00\x01\x00\x00\x00\x10")
			kblen = struct.unpack("<I", buf[kbstart-2:kbstart+2])[0]
			kblen = kblen - 5 # keep generic header for fuzzer mutations
			bufpre, kb, bufpost = buf[:kbstart], buf[kbstart:kbstart+kblen], buf[kbstart+kblen:]
		case _:
			bufpre = buf
	
	sys.stdout.buffer.write( varint.encode(func) )
	sys.stdout.buffer.write( varint.encode(3) )
	sys.stdout.buffer.write( varint.encode(len(bufpre)) )
	sys.stdout.buffer.write( bufpre )	
	sys.stdout.buffer.write( varint.encode(len(kb)) )
	sys.stdout.buffer.write( kb )
	sys.stdout.buffer.write( varint.encode(len(bufpost)) )
	sys.stdout.buffer.write( bufpost )