from langflow import CustomComponent
from langchain_community.agent_toolkits import NLAToolkit
from langchain_community.agent_toolkits.nla.tool import NLATool


class NLAToolkitComponent(CustomComponent):
    display_name = "NLAToolkit"
    description = "Natural Language API Toolkit."

    def build_config(self):
        return {"nla_tools": {"display_name": "Nla_Tools", "default": "None"}}

    def build(self, nla_tools: NLATool = None) -> NLAToolkit:
        return NLAToolkit(nla_tools=nla_tools)
