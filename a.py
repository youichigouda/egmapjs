import websocket
import json
import ssl


SAKURA_TOKEN = "40ae56fb-b3a6-4581-9101-a233f51693ed"

path = "sample.csv"

def on_message(ws, message):
	data = json.JSONDecoder().decode(message)
	mestype = data['type']
	if mestype == 'channels':
		module = data['module']
		val = data['payload']['channels'][0]['value']
		print('on_message: ' + module + " -> " + str(val))

		with open(path, mode='a') as f:
			s = 'トマト,' + str(val)+ ',' + str(ido) + ',' + str(kdo) + '\n'
			f.write(s)

		os.system('zzz.bat')

import os

if __name__ == "__main__":

	#commands.getstatusoutput('c:\Program\ Files\Git\bin\git.exe')3

	#os.system('zzz.bat')
	#subprocess.call('dir')

	#res = subprocess.call('c:\Program\ Files\Git\bin\git.exe commit -m \'msg\'')
	#val = 5
	#ido = 37.0
	#kdo = 135.5
	#with open(path, mode='a') as f:
	#	 s = 'トマト,' + str(val)+ ',' + str(ido) + ',' + str(kdo) + '\n'
	#	 f.write(s)

	#print("1"+1)

	websocket.enableTrace(True)
	path = "wss://api.sakura.io/ws/v1/" + SAKURA_TOKEN
	ws = websocket.WebSocketApp(path)
	ws.on_message = on_message
	ws.run_forever(sslopt = { "cert_reqs": ssl.CERT_NONE })

