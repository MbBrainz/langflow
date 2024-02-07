# %%
from typing import Literal


ignore_functions = [
    "construct",
    "copy",
    "dict",
    "from_orm",
    "json",
    "parse_file",
    "parse_obj",
    "parse_raw",
    "schema",
    "schema_json",
    "update_forward_refs",
    "validate",
]


def is_function_ignored(attr_name):
    return any(attr_name == func for func in ignore_functions)


def is_private_attribute(attr_name):
    return attr_name.startswith("_") or attr_name.startswith("__")


def analyze_class_attributes(cls):
    attributes_info = []
    toolkit_description = cls.__doc__.strip() if cls.__doc__ else "No description provided."

    # Resolve forward references where possible
    try:
        # Attempt to resolve forward references
        cls.update_forward_refs()
    except NameError as e:
        print(f"Failed to resolve forward references for {cls.__name__}. {str(e)}")
    # Use get_type_hints to resolve type annotations, including forward references

    # Use Pydantic's __fields__ to introspect model fields
    if hasattr(cls, "__fields__"):
        for name, field in cls.__fields__.items():
            try:
                attributes_info.append(
                    {"name": name, "type": field.type_.__name__, "default": field.default, "required": field.required}
                )
            except Exception:
                attributes_info.append(
                    {
                        "name": name,
                        "type": field.type_,
                        "default": str(field.default)
                        if field.type_ == Literal or field.type_ == str
                        else field.default,
                        "required": field.required,
                    }
                )

    return attributes_info, toolkit_description


def generate_component_code(class_name, attributes_info, toolkit_description):
    """Generate component code for the class."""
    component_class_name = f"{class_name}Component"
    display_name = class_name
    description = toolkit_description.split("\n")[0].strip()

    # Adjusted imports and class declaration
    component_code = f"""from langflow import CustomComponent
from typing import Type, Literal, ForwardRef, Any, Union
from langchain_community.tools import BaseTool
from langchain.base_language import BaseLanguageModel
from langchain.chat_models.base import BaseChatModel
from langchain_community.utilities.requests import TextRequestsWrapper
from langchain_community.agent_toolkits import {class_name}


class {component_class_name}(CustomComponent):
    display_name = "{display_name}"
    description = "{description}"

    def build_config(self):
        return {{
"""

    # Generating build_config entries
    for attribute in attributes_info:
        component_code += f'            "{attribute["name"]}": {{"display_name": "{attribute["name"].title()}", "default": "{attribute["default"]}"}},\n'

    # Correct the trailing comma and add the build method
    component_code = component_code.rstrip(",\n") + "\n        }\n"

    component_code += """
    def build(
        self,"""

    # Parameters for the build method
    for attribute in attributes_info:
        if attribute["default"]:
            component_code += f"""
            {attribute['name']}: {attribute['type']} = '{attribute['default']}',"""
        else:
            component_code += f"""
            {attribute['name']}: {attribute['type']} = None,"""

    # Finalize the build method
    component_code = component_code.rstrip(",")  # Remove the last comma
    component_code += f"""
    ) -> {class_name}:
        return {class_name}("""

    # Add parameters to the toolkit instantiation
    for attribute in attributes_info:
        component_code += f"{attribute['name']}={attribute['name']}, "

    # Closing the class instantiation and method
    component_code = component_code.rstrip(", ")  # Remove trailing comma and space
    component_code += """
        )
"""

    return component_code


def generate_component_for_toolkit(toolkit):
    attributes_info, toolkit_description = analyze_class_attributes(toolkit)
    component_code = generate_component_code(toolkit.__name__, attributes_info, toolkit_description)
    return component_code


def generate_and_store_component_file(toolkit, folder=None):
    """
    Generate and store a component file for a given toolkit.

    Args:
        toolkit: The toolkit object.

    Example:
        from langchain_community.agent_toolkits.json.toolkit import JsonToolkit
        generate_and_store_component_file(JsonToolkit)
    """
    component_code = generate_component_for_toolkit(toolkit)

    # print(component_code) # print a component code for a given toolkit
    if folder:
        with open(f"{folder}/{toolkit.__name__}.py", "w") as file:
            file.write(component_code)
    else:
        with open(f"./{toolkit.__name__}.py", "w") as file:
            file.write(component_code)


# %%
