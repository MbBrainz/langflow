from langflow import CustomComponent
from langchain.base_language import BaseLanguageModel
from langchain_community.agent_toolkits import SQLDatabaseToolkit
from langchain_community.tools.sql_database.tool import SQLDatabase


class SQLDatabaseToolkitComponent(CustomComponent):
    display_name = "SQLDatabaseToolkit"
    description = "Toolkit for interacting with SQL databases."

    def build_config(self):
        return {"db": {"display_name": "Db", "default": "None"}, "llm": {"display_name": "Llm", "default": "None"}}

    def build(self, db: SQLDatabase = None, llm: BaseLanguageModel = None) -> SQLDatabaseToolkit:
        return SQLDatabaseToolkit(db=db, llm=llm)
