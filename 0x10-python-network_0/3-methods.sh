#!/bin/bash
# A script that displays all HTTP methods the server will accept.
curl -si "$1" | grep "Allow: " | cut -d ' ' -f 2-
