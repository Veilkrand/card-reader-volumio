#!/bin/bash
app_name='card_reader.py'
service_name='card-reader-volumio.service'
app_path="$(pwd)/$app_name"
service_path="$(pwd)/$service_name"

echo $service_path

if [ ! -f $app ]; then
	echo "Fatal error! I can't find $app"
	exit 1
fi

systemctl enable $service_path
systemctl start $service_name

echo "Done"
