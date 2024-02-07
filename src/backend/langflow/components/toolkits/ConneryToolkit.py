from langflow import CustomComponent
from langchain_community.tools import BaseTool
from langchain_community.agent_toolkits import ConneryToolkit


class ConneryToolkitComponent(CustomComponent):
    display_name = "ConneryToolkit"
    description = "A LangChain Toolkit with a list of Connery Actions as tools."

    def build_config(self):
        return {"tools": {"display_name": "Tools", "default": "None"}}

    def build(self, tools: BaseTool = None) -> ConneryToolkit:
        return ConneryToolkit(tools=tools)
