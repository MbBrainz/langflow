from langflow import CustomComponent
from langchain_community.agent_toolkits import MultionToolkit


class MultionToolkitComponent(CustomComponent):
    display_name = "MultionToolkit"
    description = "Toolkit for interacting with the Browser Agent."

    def build_config(self):
        return {}

    def build(self) -> MultionToolkit:
        return MultionToolkit()
