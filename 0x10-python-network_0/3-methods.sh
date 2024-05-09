#!/bin/bash
# Script that takes URL, and dis[lays all HTTP methods the server will accept
curl -s -I -X OPTIONS "$1" | grep 'Allow:' | cut -f2- -d' '
