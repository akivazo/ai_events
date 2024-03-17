from .open_ai import AIRequestAPI
from .tool_product import ToolProduct
from .tools_creator import ToolCreator
from .event import Event
import sys

class System:
    def __init__(self) -> None:
        tool_json = ToolCreator.get_tool_json(Event)
        tools_activations = {Event.__name__: Event}
        self.__logger_stream = sys.stdout
        self.__chat_api = AIRequestAPI(tools_json=[tool_json], tools_functions=tools_activations, logger_stream=self.__logger_stream)

    def start_chatting(self):
        while True:
            request = input("What is the event?")
            self.__chat(request)

    def __chat(self, message: str):
        if self.__chat_api.new_request(message):
            self.__logger_stream.write("SUCCESS")
        else:
            self.__logger_stream.write("FAILED")

