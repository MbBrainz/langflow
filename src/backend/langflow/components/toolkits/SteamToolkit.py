from langflow import CustomComponent
from langchain_community.tools import BaseTool
from langchain_community.agent_toolkits import SteamToolkit


class SteamToolkitComponent(CustomComponent):
    display_name = "SteamToolkit"
    description = "Steam Toolkit."

    def build_config(self):
        return {"tools": {"display_name": "Tools", "default": "[]"}}

    def build(self, tools: BaseTool = None) -> SteamToolkit:
        return SteamToolkit(tools=tools)
