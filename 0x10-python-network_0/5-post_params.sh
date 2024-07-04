#!/bin/bash
#Sends a GET request to the URL, and displays the body
curl -X POST -H "email: test@gmail.com" -H "subject: 'I will always be here for PLD" -s "$1"
