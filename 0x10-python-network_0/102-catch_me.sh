#!/bin/bash
#Script that makes a request to 0.0.0.0:5000/catch_me that causes a server to respond with a message.
curl -sL 0.0.0.0:5000/catch_me_3 -X PUT -d "user_id=98" -H "Origin:School"
