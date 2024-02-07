from langflow import CustomComponent
from langchain.base_language import BaseLanguageModel
from langchain_community.agent_toolkits import SparkSQLToolkit
from langchain_community.agent_toolkits.spark_sql.toolkit import SparkSQL


class SparkSQLToolkitComponent(CustomComponent):
    display_name = "SparkSQLToolkit"
    description = "Toolkit for interacting with Spark SQL."

    def build_config(self):
        return {"db": {"display_name": "Db", "default": "None"}, "llm": {"display_name": "Llm", "default": "None"}}

    def build(self, db: SparkSQL = None, llm: BaseLanguageModel = None) -> SparkSQLToolkit:
        return SparkSQLToolkit(db=db, llm=llm)
