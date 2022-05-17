Generate files

`python3 -m grpc_tools.protoc --proto_path=./protos ./protos/alert-manager.proto --python_out=. --grpc_python_out=.`


### Port numbers

alert-manager - 50051
