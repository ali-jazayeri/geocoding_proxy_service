# geocoding_proxy_service
A proxy service for geocoding allowing to resolve the latitude and longitude coordinates for a given address.

Author: Ali Jazayeri
Date: 2018-03-29

To install this service on a new environment, run the setup command:
```
python setup.py install
```

To run this service, run the main.py:
```
python main.py
```
The default port is 8081. If non-default port is needed, provide the port parameter:
```
python main.py --port 8082
```

To test this application, go to this address in a web browser:
http://127.0.0.1:8081/MyAddress

For example, go to:
http://127.0.0.1:8081/University%20of%20Alberta

