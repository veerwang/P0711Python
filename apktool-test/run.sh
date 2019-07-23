#! /bin/bash

if   [ $1 = "-u" ]; then
	echo "start unpack apk ......"
	java -jar apktool.jar d $2
	./main.py
elif [ $1 = "-r" ]; then
	echo "clean directory ......"
	rm -rf $2 
fi
