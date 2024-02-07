from langflow import CustomComponent
from langchain_community.agent_toolkits import AzureCognitiveServicesToolkit


class AzureCognitiveServicesToolkitComponent(CustomComponent):
    display_name = "AzureCognitiveServicesToolkit"
    description = "Toolkit for Azure Cognitive Services."

    def build_config(self):
        return {}

    def build(self) -> AzureCognitiveServicesToolkit:
        return AzureCognitiveServicesToolkit()
