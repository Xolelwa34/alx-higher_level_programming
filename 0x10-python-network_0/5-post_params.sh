#!/bin/bash
#Takes a URL, sends a POST request passed to the URL
curl -s "$1" -X POST -d "email=test@gmail.com&subject=I will always be here for PLD"
