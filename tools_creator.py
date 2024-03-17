from typing import *
from .tool_product import ToolProduct
from dataclasses import dataclass, fields, is_dataclass



class ToolCreator:
    @staticmethod
    def get_tool_json(cls: Type[ToolProduct]) -> None:
        if not is_dataclass(cls):
            raise Exception(f"{cls} should be a dataclass class")
        fields_data = []
        for field in fields(cls):
            field_description = field.__doc__.strip('\n').strip() if field.__doc__ is not None else ""
            fields_data.append((field.name, field_description))

        properties_json = {}
        for field in fields_data:
            properties_json[field[0]] = {
                "type": "string", # currently we only support string
                "description": ""
            }
        product_name = cls.__name__
        product_description = cls.__doc__
        return {
            "type": "function",
            "function": {
                "name": f"{product_name}",
                "description": f"Used to create {product_name}. {product_name}: {product_description}",
                "parameters": {
                    "type": "object",
                    "properties": properties_json,
                    "required": [],
                }
            }
        }
            