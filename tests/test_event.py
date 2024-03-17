from ..open_ai import AIRequestAPI
from ..tools_creator import ToolCreator
from ..event import Event
import pytest
from datetime import datetime

product_instances = []

@pytest.fixture
def setup_teardown():
    product_instances = []

def create_instance(*args, **kwargs):
    inst = Event(*args, **kwargs)
    product_instances.append(inst)
    return inst


def test_simple_event():
    tool_json = ToolCreator.get_tool_json(Event)
    tools_activations = {Event.__name__: create_instance}
    chat_api = AIRequestAPI(tools_json=[tool_json], tools_functions=tools_activations)
    chat_api.new_request("Event in 23/02 2025 at 1:30 pm. Breakfast with Meredith in Dowson's club.")

    assert len(product_instances) == 1

    instance = product_instances[0]
    if isinstance(instance, Event):
        result = datetime.strptime(instance.start_date, "%d/%m/%Y %H:%M")
        excepted = datetime.strptime("23/02/2025 13:30", "%d/%m/%Y %H:%M")
        assert result == excepted
        assert instance.end_date == ""
        description = instance.description.lower()
        assert "breakfast" in description
        assert "meredith" in description
        assert "dowson's club" in description
        assert instance.location == "Dowson's club"
        assert instance.title.lower() == "breakfast with meredith"
