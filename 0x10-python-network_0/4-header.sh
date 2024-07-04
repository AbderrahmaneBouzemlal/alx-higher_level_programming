#!/bin/bash
#Sends a GET request to the URL, and displays the body
curl -X GET -H "X-School-User-Id : 98" -Is "$1"
