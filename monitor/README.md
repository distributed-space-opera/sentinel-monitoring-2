Alert-manager proto files

python3 -m grpc_tools.protoc --proto_path=./protos ./protos/alert-manager.proto --python_out=./alert-manager/ --grpc_python_out=./alert-manager/


Master proto files

python3 -m grpc_tools.protoc --proto_path=./protos ./protos/master-comm.proto --python_out=./ --grpc_python_out=./

Node sentinel

python3 -m grpc_tools.protoc --proto_path=./protos ./protos/sentinel-comm.proto --python_out=./ --grpc_python_out=./


Aggregator 

python3 -m grpc_tools.protoc --proto_path=./protos ./protos/aggregator.proto --python_out=./ --grpc_python_out=./

