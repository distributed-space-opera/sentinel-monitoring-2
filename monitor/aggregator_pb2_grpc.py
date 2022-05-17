# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import aggregator_pb2 as aggregator__pb2


class AggregatorServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.PersistHeartBeat = channel.unary_unary(
                '/AggregatorService/PersistHeartBeat',
                request_serializer=aggregator__pb2.PersistableHeartBeat.SerializeToString,
                response_deserializer=aggregator__pb2.HeartBeatPersistedACK.FromString,
                )


class AggregatorServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def PersistHeartBeat(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AggregatorServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'PersistHeartBeat': grpc.unary_unary_rpc_method_handler(
                    servicer.PersistHeartBeat,
                    request_deserializer=aggregator__pb2.PersistableHeartBeat.FromString,
                    response_serializer=aggregator__pb2.HeartBeatPersistedACK.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'AggregatorService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class AggregatorService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def PersistHeartBeat(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/AggregatorService/PersistHeartBeat',
            aggregator__pb2.PersistableHeartBeat.SerializeToString,
            aggregator__pb2.HeartBeatPersistedACK.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
