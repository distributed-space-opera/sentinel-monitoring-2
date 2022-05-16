# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import monitor_pb2 as monitor__pb2


class MonitorStub(object):
    """for testing purpose
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.PersistHeartbeat = channel.unary_unary(
                '/monitor.Monitor/PersistHeartbeat',
                request_serializer=monitor__pb2.HeartBeat.SerializeToString,
                response_deserializer=monitor__pb2.HeartBeatReceivedACK.FromString,
                )


class MonitorServicer(object):
    """for testing purpose
    """

    def PersistHeartbeat(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MonitorServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'PersistHeartbeat': grpc.unary_unary_rpc_method_handler(
                    servicer.PersistHeartbeat,
                    request_deserializer=monitor__pb2.HeartBeat.FromString,
                    response_serializer=monitor__pb2.HeartBeatReceivedACK.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'monitor.Monitor', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Monitor(object):
    """for testing purpose
    """

    @staticmethod
    def PersistHeartbeat(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/monitor.Monitor/PersistHeartbeat',
            monitor__pb2.HeartBeat.SerializeToString,
            monitor__pb2.HeartBeatReceivedACK.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
