#!/bin/bash
#Sends a GET request to the URL, and displays the body
curl -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" -s "$1"
