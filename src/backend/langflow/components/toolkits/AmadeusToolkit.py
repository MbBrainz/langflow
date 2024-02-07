from langflow import CustomComponent
from typing import ForwardRef
from langchain.base_language import BaseLanguageModel
from langchain_community.agent_toolkits import AmadeusToolkit


class AmadeusToolkitComponent(CustomComponent):
    display_name = "AmadeusToolkit"
    description = "Toolkit for interacting with Amadeus which offers APIs for travel."

    def build_config(self):
        return {
            "client": {"display_name": "Client", "default": "None"},
            "llm": {"display_name": "Llm", "default": "None"},
        }

    def build(self, client: ForwardRef("Client") = None, llm: BaseLanguageModel = None) -> AmadeusToolkit:
        return AmadeusToolkit(client=client, llm=llm)
