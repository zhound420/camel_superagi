
from superagi.tools.base_toolkit import BaseToolkit, BaseTool
from typing import Type, List
from camel_tool import CamelTool

class CamelToolkit(BaseToolkit):
    name: str = "Camel Toolkit"
    description: str = "Toolkit for facilitating multi-turn conversations using CAMEL"

    def get_tools(self) -> List[Type[BaseTool]]:
        return [CamelTool()]

    def get_env_keys(self) -> List[str]:
        return []  # Add any environment keys required by your toolkit
