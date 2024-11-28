from string import Template
from typing import Any, List

from autochain.agent.message import BaseMessage, UserMessage
from pydantic import BaseModel, ConfigDict


class JSONPromptTemplate(BaseModel):
    """
    Format prompt with string Template and dictionary of variables
    """

    template: Template
    """The prompt template."""

    input_variables: List[str]
    """A list of the names of the variables the prompt template expects."""
    model_config = ConfigDict(extra="forbid", arbitrary_types_allowed=True)

    def format_prompt(self, **kwargs: Any) -> List[BaseMessage]:
        variables = {v: "" for v in self.input_variables}
        variables.update(kwargs)
        prompt = self.template.substitute(**variables)
        return [UserMessage(content=prompt)]
