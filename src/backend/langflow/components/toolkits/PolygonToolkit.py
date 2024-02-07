from langflow import CustomComponent
from langchain_community.tools import BaseTool
from langchain_community.agent_toolkits import PolygonToolkit


class PolygonToolkitComponent(CustomComponent):
    display_name = "PolygonToolkit"
    description = "Polygon Toolkit."

    def build_config(self):
        return {"tools": {"display_name": "Tools", "default": "[]"}}

    def build(self, tools: BaseTool = None) -> PolygonToolkit:
        return PolygonToolkit(tools=tools)
