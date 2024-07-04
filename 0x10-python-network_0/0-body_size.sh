#!/bin/bash
#print out the size of the body
readarray -d ' : ' -t strarr <<< "$(curl -sI "$1" | grep 'content-length')"; echo -n "${strarr[1]}"
