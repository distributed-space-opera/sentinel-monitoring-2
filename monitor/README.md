Alert-manager proto files

python3 -m grpc_tools.protoc --proto_path=./protos ./protos/alert-manager.proto --python_out=./alert-manager/ --grpc_python_out=./alert-manager/

python3 -m grpc_tools.protoc --proto_path=./protos ./protos/master-comm.proto --python_out=./master/ --grpc_python_out=./master/