#!/bin/bash
#show the allowed methods the server will accept
curl -sI "$1" | grep "Allow:" | sed -ne 's/^Allow: //p'
