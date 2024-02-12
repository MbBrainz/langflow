from langflow import CustomComponent
from langflow.field_typing import Object, Document, Data
from langchain_community.agent_toolkits import GmailToolkit
from googleapiclient.discovery import Resource
from langchain_community.tools.gmail.utils import (
    build_resource_service,
    get_gmail_credentials,
)

# Can review scopes here https://developers.google.com/gmail/api/auth/scopes
# For instance, readonly scope is 'https://www.googleapis.com/auth/gmail.readonly'
credentials = get_gmail_credentials(
    token_file="token.json",
    scopes=["https://mail.google.com/"],
    client_secrets_file="credentials.json",
)
api_resource = build_resource_service(credentials=credentials)
toolkit = GmailToolkit(api_resource=api_resource)


class GmailToolkitComponent(CustomComponent):
    display_name = "GmailToolkit"
    description = "Toolkit for interacting with Gmail."

    def build_config(self):
        return {"tokem_file": {"display_name": "Token File", "default": "None"},
                "client_secrets_file": {"display_name": "Client Secrets File", "default": "None"}}

    def build(self, token_file: Document, client_secrets_file: Data) -> GmailToolkit:
        
        credentials = get_gmail_credentials(
            token_file=token_file,
            scopes=["https://mail.google.com/"],
            client_secrets_file=client_secrets_file,
        )
        api_resource = build_resource_service(credentials=credentials)
        return GmailToolkit(api_resource=api_resource)
