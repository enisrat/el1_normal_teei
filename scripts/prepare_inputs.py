import varint
import sys


def km1(funcid, data):
	sys.stdout.buffer.write( varint.encode(funcid) )
	sys.stdout.buffer.write( varint.encode(len(data)) )
	sys.stdout.buffer.write( data )



match sys.argv[1]:
	case "km1": 
		km1( eval(sys.argv[2]), open(sys.argv[3],"rb").read())
	case _:
		print("UNKNOWN TYPE")