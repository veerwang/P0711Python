#! /bin/bash
#
# 前提是安装了openssl工具
#

echo "genrsa private-public key ..."

if   [ $1 = "private" ]; then
	openssl genrsa -out rsa_private_key.pem 1024
elif [ $1 = "public" ]; then
	openssl rsa -in rsa_private_key.pem -pubout -out rsa_public_key.pem
elif [ $1 = "pkcs8" ]; then
	openssl pkcs8 -topk8 -inform PEM -in rsa_private_key.pem -outform PEM -nocrypt
elif [ $1 = "clean" ]; then
	rm rsa_private_key.pem rsa_public_key.pem
fi
