from __future__ import print_function

import logging

import grpc
import glossary_pb2
import glossary_pb2_grpc


def run():
    print("Starting dictionary client")
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = glossary_pb2_grpc.GlossaryStub(channel)

        # About
        response = stub.About(glossary_pb2.EmptyRequest())
        print("About: \n" + response.text + "\n")

        # Author
        response = stub.Author(glossary_pb2.EmptyRequest())
        print("Author: \n" + response.text + "\n")

        # All
        response = stub.All(glossary_pb2.EmptyRequest())
        print("All: \n" + str(response.definitions) + "\n")

        # List
        response = stub.List(glossary_pb2.EmptyRequest())
        print("List: \n" + str(response.concepts) + "\n")

        # Definition
        response = stub.Definition(glossary_pb2.DefinitionRequest(name="Storybook"))
        print("Definition: Storybook\n" + str(response.description) + "\n")

        # Create
        response = stub.Create(glossary_pb2.CreateRequest(name='codesplitting', description='A technique to load parts of an application or UI library on demand, improving performance by reducing initial load time.'))
        print("Create: codesplitting = A technique to load parts of an application or UI library on demand, improving performance by reducing initial load time.\nStatus: " + str(response.status) + "\nMessage: " + response.message +"\n")

        # Definition
        response = stub.Definition(glossary_pb2.DefinitionRequest(name="codesplitting"))
        print("Definition: codesplitting\n" + str(response.description) + "\n")

        # Update
        response = stub.Update(glossary_pb2.CreateRequest(name='codesplitting', description='-'))
        print("Create: codesplitting = -\nStatus: " + str(response.status) + "\nMessage: " + response.message +"\n")

        # Definition
        response = stub.Definition(glossary_pb2.DefinitionRequest(name="codesplitting"))
        print("Definition: codesplitting\n" + str(response.description) + "\n")

        # Remove
        response = stub.Remove(glossary_pb2.DefinitionRequest(name="codesplitting"))
        print("Create: codesplitting\nStatus: " + str(response.status) + "\nMessage: " + response.message +"\n")

        # All
        response = stub.All(glossary_pb2.EmptyRequest())
        print("All: \n" + str(response.definitions) + "\n")


if __name__ == "__main__":
    logging.basicConfig()
    run()