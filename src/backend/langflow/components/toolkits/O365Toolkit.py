from langflow import CustomComponent
from typing import ForwardRef
from langchain_community.agent_toolkits import O365Toolkit


class O365ToolkitComponent(CustomComponent):
    display_name = "O365Toolkit"
    description = "Toolkit for interacting with Office 365."

    def build_config(self):
        return {"account": {"display_name": "Account", "default": "None"}}

    def build(self, account: ForwardRef("Account") = None) -> O365Toolkit:
        return O365Toolkit(account=account)
