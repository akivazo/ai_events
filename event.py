from .tools_creator import ToolProduct
from dataclasses import dataclass

@dataclass
class Event(ToolProduct):
    """
    An event class with start and end date, date, time, location, title and description.
    The Event properties:
        start_date: The date and time where the event will start. the format: DD/MM/YYYY HH:MM
        end_date: The date and time where the event will end. the format: DD/MM/YYYY HH:MM
        location: The location where the event will takes place.
        title: The title of the event.
        description: The description of the event. can be long description.
    """
    start_date: str="", 
    end_date: str="" 
    time: str="" 
    location: str=""
    title: str=""
    description: str=""

    def act(self):
        print(dir(self))