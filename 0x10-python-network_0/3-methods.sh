#!/bin/bash
#show the allowed methods the server will accept
curl -s "$1" | grep "Allow " | cut -d ":" -f2 
