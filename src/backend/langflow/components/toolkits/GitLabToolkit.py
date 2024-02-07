from langflow import CustomComponent
from langchain_community.tools import BaseTool
from langchain_community.agent_toolkits import GitLabToolkit


class GitLabToolkitComponent(CustomComponent):
    display_name = "GitLabToolkit"
    description = "GitLab Toolkit."

    def build_config(self):
        return {"tools": {"display_name": "Tools", "default": "[]"}}

    def build(self, tools: BaseTool = None) -> GitLabToolkit:
        return GitLabToolkit(tools=tools)
