import varint
import json
import os
import io

def load_input_hist(path: str):
	# isolate fname from path
	fname = os.path.basename(path)
	# get the solution directory
	sol_dir = os.path.dirname(path)
	metapath = os.path.join(sol_dir, f".{fname}_1.metadata")
	if not os.path.exists(metapath):
		print(f"Solution {metapath} does not exist.")
		return
	meta = json.load(open(metapath))

	match meta:
		case {
			'metadata': {
				'map': inner1
				}
			}:
			for k,v in inner1.items():
					match v:
						case [v1,{
							'input_hist': input_hist,
							**other
						}]:
							return input_hist
		case _:
			pass
		
	print("Could not parse")

def ser_to_buf(stream, kind):
	func = None
	buf = None
	
	match kind:
		case 's':
			func = varint.decode_stream(stream)
			sz = varint.decode_stream(stream)
			buf = stream.read(sz)
		case 'm':
			func = varint.decode_stream(stream)
			num = varint.decode_stream(stream)
			assert num == 3
			for i in range(num):
				sz = varint.decode_stream(stream)
				buf += stream.read(sz)
		case _:
			print("No kind given")		
	
	return func, buf

def load_solution(path: str, kind: str):
	input_hist = bytes(load_input_hist(path))

	s = io.BytesIO(input_hist)
	inputs = []

	while True:
		try:
			func, buf = ser_to_buf(s, kind)
			inputs.append( (func, buf) )
		except EOFError:
			break
	
	with open(path, "rb") as f:
		func = varint.decode_stream(f)
		sz = varint.decode_stream(f)
		buf = f.read(sz)
		inputs.append( (func, buf) )
	
	return inputs