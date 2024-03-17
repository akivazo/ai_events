import os, json
from openai import OpenAI

def create_event(self, start_date, end_date, time, location, title, description):
    print(locals())

client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
)

tools = [
        {
            "type": "function",
            "function": {
                "name": "create_an_event",
                "description": "Create an events given the date, time, location, title and description",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "start_date": {
                            "type": "string",
                            "description": "The date where the event will start. the format: YY/MM/DD",
                        },
                        "end_date": {
                            "type": "string",
                            "description": "The date where the event will end. the format: YY/MM/DD",
                        },
                        "time": {
                            "type": "string",
                            "description": "The time un the day when the event will takes place. if emitted the event will be all dat. the format: HH:MM ",
                        },
                        "location": {
                            "type": "string",
                            "description": "The location where the event will takes place.",
                        },
                        "title": {
                            "type": "string",
                            "description": "The title of the event.",
                        },
                        "description": {
                            "type": "string",
                            "description": "The description of the event. can be long description.",
                        },
                    },
                    "required": ["start_date", "title"],
                },
            },
        }
    ]

response = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": """""",
        },
        
    ],
    tools=tools,
    model="gpt-3.5-turbo",
)

args = ["start_date", "end_date", "time", "location", "title", "description"]
response_message = response.choices[0].message
tool_calls = response_message.tool_calls
# Step 2: check if the model wanted to call a function
if tool_calls:
    # Step 3: call the function
    # Note: the JSON response may not always be valid; be sure to handle errors
    available_functions = {
        "create_an_event": create_event,
    }  # only one function in this example, but you can have multiple
    # Step 4: send the info for each function call and function response to the model
    for tool_call in tool_calls:
        function_name = tool_call.function.name
        function_to_call = available_functions[function_name]
        function_args = json.loads(tool_call.function.arguments)
        print(function_args)
         