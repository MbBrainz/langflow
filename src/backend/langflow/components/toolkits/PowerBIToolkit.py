from langflow import CustomComponent
from typing import Union
from langchain.base_language import BaseLanguageModel
from langchain.chat_models.base import BaseChatModel
from langchain_community.agent_toolkits import PowerBIToolkit
from langchain_community.agent_toolkits.powerbi.toolkit import PowerBIDataset
from langchain.callbacks.base import BaseCallbackManager


class PowerBIToolkitComponent(CustomComponent):
    display_name = "PowerBIToolkit"
    description = "Toolkit for interacting with Power BI dataset."

    def build_config(self):
        return {
            "powerbi": {"display_name": "Powerbi", "default": "None"},
            "llm": {"display_name": "Llm", "default": "None"},
            "examples": {"display_name": "Examples", "default": "None"},
            "max_iterations": {"display_name": "Max_Iterations", "default": "5"},
            "callback_manager": {"display_name": "Callback_Manager", "default": "None"},
            "output_token_limit": {"display_name": "Output_Token_Limit", "default": "None"},
            "tiktoken_model_name": {"display_name": "Tiktoken_Model_Name", "default": "None"},
        }

    def build(
        self,
        powerbi: PowerBIDataset = None,
        llm: Union[BaseLanguageModel, BaseChatModel] = None,
        examples: str = None,
        max_iterations: int = "5",
        callback_manager: BaseCallbackManager = None,
        output_token_limit: int = None,
        tiktoken_model_name: str = None,
    ) -> PowerBIToolkit:
        return PowerBIToolkit(
            powerbi=powerbi,
            llm=llm,
            examples=examples,
            max_iterations=max_iterations,
            callback_manager=callback_manager,
            output_token_limit=output_token_limit,
            tiktoken_model_name=tiktoken_model_name,
        )
