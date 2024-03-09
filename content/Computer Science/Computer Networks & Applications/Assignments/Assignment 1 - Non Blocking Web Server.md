

 
> [!idea]+ Idea
> In this practical, we will develop a web server. In the end, you will have built a non-blocking web server that is capable of processing multiple simultaneous service requests in parallel. You should be able to demonstrate that your Web server is capable of delivering your home page to a web browser and that your server returns standards compliant responses.
> 
> - For a full assignment specification, see [here](https://myuni.adelaide.edu.au/courses/95212/assignments/385087)
> - The repostory containing the full implemenation can be found [here](https://github.com/santiagosayshey/CNA-S1-2024/tree/assignment1)
> 
> 

> [!code] Step 1: Create a socket
>
> ```c
> listen_socket = socket(AF_INET, SOCK_STREAM, 0);
> if (listen_socket == -1) {
>   printf("Could not create socket");
> }
> printf("Socket created successfully.\n");
> ```

> [!code] Step 2: Set the values for the server address structure
>
> ```c
> server_address.sin_family = AF_INET;                   // Set address family (IPv4)
> server_address.sin_addr.s_addr = htonl(INADDR_ANY);    // Listen on any network interface
> server_address.sin_port = htons(port);                 // Set port number, converting to network byte order
> ```

> [!code] Step 3: Bind the socket to the address information set in server_address
>
> ```c
> if (bind(listen_socket, (struct sockaddr *)&server_address, sizeof(server_address)) < 0) {
>   perror("bind failed");
>   exit(EXIT_FAILURE);
> }
> printf("Bind successful. Listening on port %d...\n", port);
> ```

> [!code] Step 4: Start listening for connections
>
> ```c
> if (listen(listen_socket, 10) < 0) {
>   perror("listen failed");
>   exit(EXIT_FAILURE);
> }
> printf("Server is now listening on port %d...\n", port);
> ```

> [!code] Step 5: Accept a connection
>
> ```c
> socklen_t client_address_len = sizeof(client_address);
> connection_socket = accept(listen_socket, (struct sockaddr *)&client_address, &client_address_len);
> if (connection_socket < 0) {
>     perror("accept failed");
>     continue; // or exit based on your error handling policy
> }
> char clientIP[INET_ADDRSTRLEN]; // Buffer to store the IP address in string format
> inet_ntop(AF_INET, &client_address.sin_addr, clientIP, INET_ADDRSTRLEN); // Convert the IP to a string
> printf("Accepted connection from %s:%d\n", clientIP, ntohs(client_address.sin_port));
> ```

> [!code] Step 6: Call helper function to read the request
>
> ```c
> if (!Parse_HTTP_Request(connection_socket, &new_request)) {
>   fprintf(stderr, "Error parsing HTTP request\n");
>   close(connection_socket); // Ensure the socket is closed before exiting
>   exit(EXIT_FAILURE);       // Exit the child process if parsing fails
> }
> /* Print the parsed request method and URI for debugging */
> printf("Parsed HTTP Request: Method = %s, URI = %s\n", new_request.method, new_request.URI);
> ```

> [!code] Step 7: Decide which status_code and reason phrase to return to client
>
> ```c
> if (strcmp(new_request.method, "GET") == 0 || strcmp(new_request.method, "HEAD") == 0) {
>   if (Is_Valid_Resource(new_request.URI)) {
>     status_code = 200;
>     status_phrase = "OK";
>   } else {
>     status_code = 404;
>     status_phrase = "Not Found";
>     Send_Error_Response(connection_socket, status_code, status_phrase);
>     exit(EXIT_SUCCESS);
>   }
> } else {
>   status_code = 501;
>   status_phrase = "Not Implemented";
>   Send_Error_Response(connection_socket, status_code, status_phrase);
>   exit(EXIT_SUCCESS);
> }
> ```

> [!code] Step 8: Set the reply message to the client
>
> ```c
> sprintf(response_buffer, "HTTP/1.0 %d %s\r\n", status_code, status_phrase);
> ```

> [!code] Step 9: Send the reply message to the client
>
> ```c
> send(connection_socket, response_buffer, strlen(response_buffer), 0);
> ```


> [!code] Step 10: Send resource (if requested)
>
> ```c
> is_ok_to_send_resource = (status_code == 200);
>
> if (is_ok_to_send_resource)
> {
>   Send_Resource(connection_socket, new_request.URI, new_request.method);
> }
> ```


> [!code] Step 11: Do not send resource (End the HTTP headers)
>
> ```c
> send(connection_socket, "\r\n\r\n", strlen("\r\n\r\n"), 0);
> ```
