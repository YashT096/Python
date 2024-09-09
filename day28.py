#Hello , Today we are going to Application programming Interface(API)
#API stands for Application Programming Interface. The kind of API we will cover in this section is going to be Web APIs. 
# Web APIs are the defined interfaces through which interactions happen between an enterprise and applications that use its assets, 
# which also is a Service Level Agreement (SLA) to specify the functional provider and expose the service path or URL for its API users.

#building API
#RESTful API is an application program interface (API) that uses HTTP requests to GET, PUT, POST and DELETE data. 
# In the previous sections, we have learned about python, flask and mongoDB.
#  We will use the knowledge we acquire to develop a RESTful API using Python flask and mongoDB database. Every application which has CRUD(Create, Read, Update, Delete) operation has an API to create data, 
# to get data, to update data or to delete data from a database.

#HTTP (Hypertext Transfer Protocol)
#HTTP is an established communication protocol between a client and a server. A client in this case is a browser and server is the place where you access data. HTTP is a network protocol used to deliver resources which could be files on the World Wide Web, whether they are HTML files, image files, query results, scripts, or other file types.

#A browser is an HTTP client because it sends requests to an HTTP server (Web server), which then sends responses back to the client.

#Structure of HTTP
#HTTP uses client-server model. An HTTP client opens a connection and sends a request message to an HTTP server and the HTTP server returns response message which is the requested resources. 
# When the request response cycle completes the server closes the connection.

#Initial Request Line(Status Line)
#The initial request line is different from the response. A request line has three parts, separated by spaces:

#method name(GET, POST, HEAD)
#path of the requested resource,
#the version of HTTP being used. eg GET / HTTP/1.1
#GET is the most common HTTP that helps to get or read resource and POST is a common request method to create resource.


#Request Methods
#The GET, POST, PUT and DELETE are the HTTP request methods which we are going to implement an API or a CRUD operation application.

#GET: GET method is used to retrieve and get information from the given server using a given URI. Requests using GET should only retrieve data and should have no other effect on the data.

#POST: POST request is used to create data and send data to the server, for example, creating a new post, file upload, etc. using HTML forms.

#PUT: Replaces all current representations of the target resource with the uploaded content and we use it modify or update data.

#DELETE: Removes data