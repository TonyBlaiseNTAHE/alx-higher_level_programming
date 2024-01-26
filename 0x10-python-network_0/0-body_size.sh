#!/bin/bash
# a script that display body content of a http's response
curl -sI "$1" | grep -i content-length | awk '{print $2}'
