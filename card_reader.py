from __future__ import print_function
from HID_Reader import HID_Reader
from volumio import Volumio
import time

v = Volumio()

# Test RFID DB
_db = {
	'0015470303' : {
		'name' : 'Japanese Piano',
		'service' : 'spop',
		'uri' : 'spotify:user:1234374189:playlist:2FS4FRrjcERsRpIbn8CYg6'
	},
	'0015493820' : {
		'name' : '1 - The Beatles',
		'service' : 'spop',
		'uri' : 'spotify:album:7vEJAtP3KgKSpOHVgwm3Eh' # 1 the Beatles
	},
	'0015764039' : {
		'name' : 'Pica Pica',
		'service' : 'spop',
		'uri' : 'spotify:artist:3oaNnQa52hlN69wvaatUE2' # Pika Pika
	},
	'0015767683' : {
		'name' : 'Opera 100',
		'service' : 'spop',
		'uri' : 'spotify:user:dgdeccaclassics:playlist:2PjVPkj4a9kBvQIXaZ6UUt'
	},

	'0015764413' : {
		'name' : 'Daft Punk and more',
		'service' : 'spop',
		'uri' : 'spotify:user:randyhenderson428:playlist:18j1dFpWKFCurQDvOtpYjV'
	}


}

_last_uri = ''
_last_time = 0.0

def newline_callback(data):
	print(data)
	play_id(data)


def volumio_callback(data, *args):
	print('callback',args)


def play_id(id):
	global _last_uri, _last_time
	if id in _db:
		_delta = time.time()-_last_time
		if (_last_uri == _db[id]['uri'] and _delta<5):
			print('Uri already opened 5 seconds ago')
			return False

		print('Queueing {}'.format(_db[id]['name']))
		service = _db[id]['service']
		uri = _db[id]['uri']
		v._send('clearQueue')
		v._send('addPlay', {'status':'play', 'service':service, 'uri':uri}, callback=volumio_callback)
		_last_uri = uri
		_last_time = time.time()
		return True
	else:
		print('Id not found!')
		return False

if __name__ == '__main__':

	# $ ls /dev/input/by-id/	
	device = '/dev/input/by-id/usb-Sycreader_RFID_Technology_Co.__Ltd_SYC_ID_IC_USB_Reader_08FF20140315-event-kbd'

	# while v.ready is False:
	while(len(v._state)==0):
		print('.', end='')
	print(' Volumio client ready!')

	r = HID_Reader(device, on_newline_event_callback=newline_callback)

	

