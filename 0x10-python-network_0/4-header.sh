#!/bin/bash
#Takes a URL as an argument, and displays the body of the response when it sends a GET request to the URL
curl -s "$1" -H "X-School-User-Id: 98"
