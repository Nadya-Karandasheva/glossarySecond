from concurrent import futures
import logging

import grpc
import glossary_pb2
import glossary_pb2_grpc

glossary =  {
    'Component-Based Architecture': 'A design approach where user interfaces are built using reusable and self-contained components, enabling scalability and modularity in UI libraries.',
    'Atomic Design': 'A methodology for crafting UI libraries that decompose interfaces into five distinct levels: atoms, molecules, organisms, templates, and pages.',
    'Design Tokens': 'Variables that store design decisions (e.g., colors, typography, spacing) to ensure consistent theming across components and platforms.',
    'Theming': 'The capability to customize the appearance of a UI library to match a corporate brand\'s identity, often achieved through design tokens and CSS variables.',
    'Accessibility (A11y)': 'Ensuring components are usable by individuals with disabilities, adhering to standards like WCAG to support inclusive design practices.',
    'Responsive Design': 'Designing components to adapt seamlessly to different screen sizes and orientations, ensuring usability across devices.',
    'State Management': 'Techniques and patterns for handling component states (e.g., loading, error, or success states) within a UI library to maintain predictable behavior.',
    'Style Guide': 'A comprehensive document or tool that outlines the visual and functional standards for components, serving as a reference for developers and designers.',
    'Storybook': 'A popular tool for developing, testing, and documenting UI components in isolation, aiding in the iterative design process.',
    'Component Testing': 'The practice of validating individual UI components for correctness, interactivity, and visual integrity using tools like Jest, React Testing Library, or Cypress.',
}

class Glossary(glossary_pb2_grpc.GlossaryServicer):

    def About(self, request, context):
        return glossary_pb2.Reply(text="This is a glosary. You can get, create and modify them.")

    def Author(self, request, context):
        return glossary_pb2.Reply(text="Karandasheva Nadya")

    def All(self, request, context):
        return glossary_pb2.AllReply(definitions=glossary)

    def List(self, request, context):
        responseDict = {}
        counter = 1
        for item in glossary.keys():
            responseDict[counter] = item.capitalize()
            counter += 1
        return glossary_pb2.ListReply(concepts=responseDict)

    def Definition(self, request, context):
        return glossary_pb2.DefinitionReply(description=glossary[request.name])

    def Create(self, request, context):
        glossary[request.name.lower()] = request.description
        return glossary_pb2.CompleteReply(status=200, message=f'Successfully added your definition of {request.name.capitalize()}')

    def Update(self, request, context):
        glossary[request.name.lower()] = request.description
        return glossary_pb2.CompleteReply(status=200, message=f'Successfully changed definition of {request.name.capitalize()}')

    def Remove(self, request, context):
        glossary.pop(request.name.lower())
        return glossary_pb2.CompleteReply(status=200, message=f'{request.name.capitalize()} successfully removed from glossary')


def serve():
    port = "50051"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    glossary_pb2_grpc.add_GlossaryServicer_to_server(Glossary(), server)
    server.add_insecure_port("[::]:" + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    serve()