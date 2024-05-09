#!/bin/bash
#Script that takes a URL and displays the size of a body of the response
curl -Is "$1" | grep -w 'Content-Length' | cut -f2 -d' '
