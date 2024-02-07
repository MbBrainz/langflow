from langflow import CustomComponent
from langchain_community.agent_toolkits import GmailToolkit
from googleapiclient.discovery import Resource


class GmailToolkitComponent(CustomComponent):
    display_name = "GmailToolkit"
    description = "Toolkit for interacting with Gmail."

    def build_config(self):
        return {"api_resource": {"display_name": "Api_Resource", "default": "None"}}

    def build(self, api_resource: Resource = None) -> GmailToolkit:
        return GmailToolkit(api_resource=api_resource)
