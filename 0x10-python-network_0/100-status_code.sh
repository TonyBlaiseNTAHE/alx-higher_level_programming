#!/bin/bash
# sends a request to a URL passed as argument, and display only the status code of the response
curl -so -w %{http_code} "$1" /dev/null
