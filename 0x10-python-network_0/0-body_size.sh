#!/bin/bash
#return the content-size
readarray -d ' : ' -t strarr <<< "$(curl -sI "$1" | grep 'content-length')"; echo -n "${strarr[1]}"

