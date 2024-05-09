#!/bin/bash
#Script that sends a delete request to the URL
#passed as the argument, and displays the body of the response
curl -s "$1" -X DELETE
