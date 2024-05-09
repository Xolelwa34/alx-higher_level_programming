#!/bin/bash
#Sends a json POST request to the URL
curl -s -d "@$2" -H "Content-Type: application/json" -X POST "$1"
