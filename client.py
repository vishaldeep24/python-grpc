import grpc

# import the generated classes
import detailservice_pb2
import detailservice_pb2_grpc

# open a gRPC channel
channel = grpc.insecure_channel('localhost:50051')

# create a stub (client)
stub = detailservice_pb2_grpc.DetailServiceStub(channel)

# create a valid request message
details = detailservice_pb2.Details()
details.id = 1

# make the call
response = stub.GetPerson(details)
print(response.SerializeToString())
print(response)