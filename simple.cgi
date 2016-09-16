#! /bin/bash

# This is a little CGI program


###################################################################
# The following are environment variables that are available to you
#
# CONTENT_TYPE:      The MIME type of associated with the option body of the HTTP request.
# CONTENT_LENGTH:    The length of the query information.
# GATEWAT_INTERFACE: Currently CGI/1.1
# HTTP_HOST:         The name of the vhost of the server.  
# HTTP_USER_AGENT:   Information about the browser/client that made requested.
# QUERY_STRING:      The query string.
# REQUEST_METHOD:    The method used to make the request. The most common methods are GET and POST.
# REQUEST_URI:       The URI of the request
# SERVER_PROTOCOL:   Currently HTTP/1.1
# SCRIPT_FILENAME:   The full path to the CGI script.
# SCRIPT_NAME:       The name (i.e., URI) of the CGI script.
# SERVER_NAME:       The server's hostname or IP Address
# SERVER_PORT:       The port of the server



echo "Content-type: text/html"
echo ""

echo "<head>"
echo "<title>Dr. Light</title>"
echo "<link rel="stylesheet" type="text/css" href="onstyle.css">"
echo "</head>"

echo "<h2>"
echo "To think or not to think..."
echo "<br>"
echo "&emsp; &emsp; &emsp; &emsp;"
echo "&emsp; &emsp; &emsp; &emsp;"
echo "I like turtles + $QUERY_STRING"
echo "</h2>"


echo "<br>"
echo "<br>"
echo "<br>"
echo "<br>"
echo "<br>"
echo "<br>"
echo "<br>"


/usr/bin/curl https://www.csun.edu/~jeffw/

ls -l > content.html

cat content.html


fi
