# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import sentinel_comm_pb2 as sentinel__comm__pb2


class SentinelMonitoringStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.healthCheck = channel.unary_unary(
                '/stream.SentinelMonitoring/healthCheck',
                request_serializer=sentinel__comm__pb2.healthCheckRequest.SerializeToString,
                response_deserializer=sentinel__comm__pb2.healthCheckReply.FromString,
                )


class SentinelMonitoringServicer(object):
    """Missing associated documentation comment in .proto file."""

    def healthCheck(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SentinelMonitoringServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'healthCheck': grpc.unary_unary_rpc_method_handler(
                    servicer.healthCheck,
                    request_deserializer=sentinel__comm__pb2.healthCheckRequest.FromString,
                    response_serializer=sentinel__comm__pb2.healthCheckReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'stream.SentinelMonitoring', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class SentinelMonitoring(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def healthCheck(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/stream.SentinelMonitoring/healthCheck',
            sentinel__comm__pb2.healthCheckRequest.SerializeToString,
            sentinel__comm__pb2.healthCheckReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
