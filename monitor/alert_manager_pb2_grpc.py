# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import alert_manager_pb2 as alert__manager__pb2


class AlertManagerServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.NodeDown = channel.unary_unary(
                '/unary.AlertManagerService/NodeDown',
                request_serializer=alert__manager__pb2.NodeStatusRequest.SerializeToString,
                response_deserializer=alert__manager__pb2.NodeStatusResponse.FromString,
                )


class AlertManagerServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def NodeDown(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AlertManagerServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'NodeDown': grpc.unary_unary_rpc_method_handler(
                    servicer.NodeDown,
                    request_deserializer=alert__manager__pb2.NodeStatusRequest.FromString,
                    response_serializer=alert__manager__pb2.NodeStatusResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'unary.AlertManagerService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class AlertManagerService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def NodeDown(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/unary.AlertManagerService/NodeDown',
            alert__manager__pb2.NodeStatusRequest.SerializeToString,
            alert__manager__pb2.NodeStatusResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)