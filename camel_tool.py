import camel
from superagi.tools.base_tool import BaseTool
from camel.agents import ChatAgent
from camel.messages import BaseMessage
from typing import Type, List
from camel_tool_input import CamelToolInput

class CamelTool(BaseTool):
    name: str = "Camel Tool"
    args_schema: Type[BaseModel] = CamelToolInput
    description: str = "Tool to facilitate multi-turn conversations using CAMEL"

    def _execute(self, messages: List[str] = None):
        # Initialize the chat agent
        agent = ChatAgent(BaseMessage.make_assistant_message(role_name="Assistant", content="I am an assistant."))

        # Reset the agent (if necessary)
        agent.reset()

        # Initialize a list to hold the agent's responses
        responses = []

        # Loop over the input messages
        for message in messages:
            # Make a user message with the current input message
            user_msg = BaseMessage.make_user_message(role_name="User", content=message)

            # Get the assistant's response
            assistant_response = agent.step(user_msg)

            # Add the assistant's response to the list of responses
            responses.append(assistant_response.msg.content)

        # Return the list of responses
        return responses
