from langflow import CustomComponent
from typing import ForwardRef
from langchain_community.agent_toolkits import PlayWrightBrowserToolkit


class PlayWrightBrowserToolkitComponent(CustomComponent):
    display_name = "PlayWrightBrowserToolkit"
    description = "Toolkit for PlayWright browser tools."

    def build_config(self):
        return {
            "sync_browser": {"display_name": "Sync_Browser", "default": "None"},
            "async_browser": {"display_name": "Async_Browser", "default": "None"},
        }

    def build(
        self,
        sync_browser: ForwardRef("Optional['SyncBrowser']") = None,
        async_browser: ForwardRef("Optional['AsyncBrowser']") = None,
    ) -> PlayWrightBrowserToolkit:
        return PlayWrightBrowserToolkit(sync_browser=sync_browser, async_browser=async_browser)
