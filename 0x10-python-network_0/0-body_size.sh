#!/usr/bin/env bash
#displays the size of the body of the reponse
var=$(curl -sI $1 | grep "content-length")
IFS=': '
read -ra strarr <<< "$var"
echo "${strarr[1]}"
