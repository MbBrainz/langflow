from langflow import CustomComponent
from langchain_community.tools import BaseTool
from langchain_community.agent_toolkits import JiraToolkit


class JiraToolkitComponent(CustomComponent):
    display_name = "JiraToolkit"
    description = "Jira Toolkit."

    def build_config(self):
        return {"tools": {"display_name": "Tools", "default": "[]"}}

    def build(self, tools: BaseTool = None) -> JiraToolkit:
        return JiraToolkit(tools=tools)
