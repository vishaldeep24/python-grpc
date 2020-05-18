# Python-gRPC
Example of python-grpc

### Creating python virtual environment
python3 -m venv env

### Activate environment
source env/bin/activate

### Installing required packages
- pip install grpcio
- pip install grpcio-tools

### Generating client and server code
```
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. detailservice.proto
OR
python -m grpc_tools.protoc -I../../protos --python_out=. --grpc_python_out=. ../../protos/detailservice.proto
OR
python -m grpc_tools.protoc -I./protos --python_out=./generatedFiles --grpc_python_out=./generatedFiles detailservice.proto
```

### Start using the server
python server.py

### Starting the client
python client.py

### Resources
- [Official Quick Start](https://grpc.io/docs/quickstart/python/)
