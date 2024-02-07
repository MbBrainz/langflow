from langflow import CustomComponent
from typing import ForwardRef
from langchain_community.agent_toolkits import SlackToolkit


class SlackToolkitComponent(CustomComponent):
    display_name = "SlackToolkit"
    description = "Toolkit for interacting with Slack."

    def build_config(self):
        return {"client": {"display_name": "Client", "default": "None"}}

    def build(self, client: ForwardRef("WebClient") = None) -> SlackToolkit:
        return SlackToolkit(client=client)
