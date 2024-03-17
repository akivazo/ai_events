import os, json, sys
from openai import OpenAI
from typing import *


class AIRequestAPI:
    def __new_session(self):
        self.__messages = []

    def __init__(self, tools_functions: Mapping[str, Callable], tools_json: Any, 
                 logger_stream: TextIO=None) -> None:
        self.__logger_stream = logger_stream if logger_stream is not None else sys.stdout
        self.__tools_functions = tools_functions
        self.__tools_json = tools_json
        self.__client = OpenAI(
            # This is the default and can be omitted
            api_key=os.environ.get("OPENAI_API_KEY"),
        )
        self.__new_session()

    def __add_user_message(self, message: str):
        self.__add_message({
                    "role": "user",
                    "content": message,
                })
        
    def __add_message(self, message):
        self.__messages.append(message)

    def __add_current_time_message(self):
        import datetime
        self.__add_message({
                    "role": "user",
                    "content": f"I you need to know what is current time, use the time stamp: {datetime.datetime.now()}." ,
                })
        
    def new_request(self, message: str):
        # self.__add_current_time_message()
        self.__add_user_message(message)
        response  = self.__client.chat.completions.create(
            messages=self.__messages,
            tools=self.__tools_json,
            model="gpt-3.5-turbo")
        response_message = response.choices[0].message
        self.__add_message(response_message)
        try:
            tool_calls = response_message.tool_calls
            # Step 2: check if the model wanted to call a function
            if tool_calls:
                # Step 3: call the function
                # Note: the JSON response may not always be valid; be sure to handle errors
                # Step 4: send the info for each function call and function response to the model
                for tool_call in tool_calls:
                    function_name = tool_call.function.name
                    function_to_call = self.__tools_functions[function_name]
                    function_args = json.loads(tool_call.function.arguments)
                    function_to_call(**function_args)
        except Exception as e:
            self.__logger_stream.write(str(e))
            return False
        return True


    

    