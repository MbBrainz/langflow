from langflow import CustomComponent
from langchain_community.tools import BaseTool
from langchain_community.agent_toolkits import GitHubToolkit


class GitHubToolkitComponent(CustomComponent):
    display_name = "GitHubToolkit"
    description = "GitHub Toolkit."

    def build_config(self):
        return {"tools": {"display_name": "Tools", "default": "[]"}}

    def build(self, tools: BaseTool = None) -> GitHubToolkit:
        return GitHubToolkit(tools=tools)
