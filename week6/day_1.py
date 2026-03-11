'''
This imports a simple built-in web server from python
It understands WSGI rules (Web Server Gateway Interface)
'''

from wsgiref.simple_server import make_server


#this helps us convert Python dictionaries to javascripts Object 
import json

def application(environ, start_response):
  


    #This is where you get the http methods. where you know what type of request was mode.
    method = environ['REQUEST_METHOD']

    #Get the url path
    path = environ['PATH_INFO']


    # Request body
    content_length = environ.get('CONTENT_LENGTH')#Get the length of the body (how many bytes were sent)
    #if there is no body, set length to zero
    if content_length:
        content_length = int(content_length)
    else:
        content_length = 0  


    body = environ['wsgi.input'].read(content_length)
    body_text = body.decode("utf-8")if body else ''


    print(method, "METHOD")
    print(path, "PATH")
    print(body_text, "BODY")

    if method == "GET":



        message  = {
            "name": "Boluwatife" ,
            "email": "Boluwatife@gmail.com" ,
            "country": "Nigeria"
        }


        # send HTTP status and headers
        start_response("200 OK",[("Content-type","application/json")])
            # Returns back a response
        return [json.dumps(message).encode()]
    elif method == "POST":
       
       start_response("200 OK",[("Content-type","application/json")])
       return[json.dumps({"message": "your post has been created","data": body_text}).encode()]
    
     
    # Create  = make_server on localhost part 8000 or it's sharping resources on this server which is on part 8000
server = make_server("localhost", 8000, application)
print("Server is running on http://127.0.0.1:8000")

    

# Keep the server running forever
server.serve_forever()    
