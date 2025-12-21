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

def load_solution(path: str):
	input_hist = bytes(load_input_hist(path))

	s = io.BytesIO(input_hist)
	inputs = []

	while True:
		try:
			func = varint.decode_stream(s)
			sz = varint.decode_stream(s)
			buf = s.read(sz)
			inputs.append( (func, buf) )
		except EOFError:
			break
	
	with open(path, "rb") as f:
		func = varint.decode_stream(f)
		sz = varint.decode_stream(f)
		buf = f.read(sz)
		inputs.append( (func, buf) )
	
	return inputs