from langflow import CustomComponent
from langchain_community.tools import BaseTool
from langchain_community.agent_toolkits import NasaToolkit


class NasaToolkitComponent(CustomComponent):
    display_name = "NasaToolkit"
    description = "Nasa Toolkit."

    def build_config(self):
        return {"tools": {"display_name": "Tools", "default": "[]"}}

    def build(self, tools: BaseTool = None) -> NasaToolkit:
        return NasaToolkit(tools=tools)
