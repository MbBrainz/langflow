from langflow import CustomComponent
from typing import Literal, ForwardRef
from langchain_community.agent_toolkits import AINetworkToolkit


class AINetworkToolkitComponent(CustomComponent):
    display_name = "AINetworkToolkit"
    description = "Toolkit for interacting with AINetwork Blockchain."

    def build_config(self):
        return {
            "network": {"display_name": "Network", "default": "testnet"},
            "interface": {"display_name": "Interface", "default": "None"},
        }

    def build(self, network: Literal = "testnet", interface: ForwardRef("Optional[Ain]") = None) -> AINetworkToolkit:
        return AINetworkToolkit(network=network, interface=interface)
