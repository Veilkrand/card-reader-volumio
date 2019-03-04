from HID_Reader import HID_Reader

def keydown_callback(data):
	pass
	# print(data)

def newline_callback(data):
	print(data)


if __name__ == '__main__':

	# $ ls /dev/input/by-id/
	
	device = '/dev/input/by-id/usb-Sycreader_RFID_Technology_Co.__Ltd_SYC_ID_IC_USB_Reader_08FF20140315-event-kbd'

	r = HID_Reader(device, on_newline_event_callback=newline_callback, on_keydown_event_callback=keydown_callback)
