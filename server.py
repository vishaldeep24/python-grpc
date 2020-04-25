from concurrent import futures
import time
import grpc
import detailservice_pb2
import detailservice_pb2_grpc

class Details(detailservice_pb2_grpc.DetailServiceServicer):
    def GetPerson(self, request, context):
        person = detailservice_pb2.Person()
        person.name = "Vishal Deep"
        person.id = request.id
        person.email = "vdeep@ext.uber.com"
        phone = person.phones.add()
        phone.type = detailservice_pb2.Person.MOBILE
        phone.number = "8971800406"
        return person

server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
detailservice_pb2_grpc.add_DetailServiceServicer_to_server(Details(), server)
# listen on port 50051
print('Starting server. Listening on port 50051.')
server.add_insecure_port('[::]:50051')
server.start()

# since server.start() will not block,
# a sleep-loop is added to keep alive
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)
