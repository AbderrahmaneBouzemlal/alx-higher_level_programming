#!/usr/bin/env bash
readarray -d ' : ' -t strarr <<< $(curl -sI $1 | grep "content-length"); printf "${strarr[1]}"

