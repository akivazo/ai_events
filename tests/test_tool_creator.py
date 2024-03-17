from ..tools_creator import ToolCreator
from ..tool_product import ToolProduct
from dataclasses import dataclass

@dataclass
class ProductTest(ToolProduct):
    '''
    This is test product description.
    '''
    prop1: str 
    #  description1
    prop2: str 
    # description2

def test_tools_creator():
    creator = ToolCreator()

    tool_json = creator.get_tool_json(ProductTest)



    assert tool_json == {
        'type': 'function', 
        'function': 
            {
                'name': 'ProductTest', 
                'description': 'Used to create ProductTest. ProductTest: \n    This is test product description.\n    ', 
                'parameters': {
                    'type': 'object', 
                    'properties': {
                            'prop1': {'type': 'string', 'description': ''},
                            'prop2': {'type': 'string', 'description': ''}
                        },
                    'required': []
                    }
             }
            }
