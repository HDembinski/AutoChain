from typing import Any, Optional

from autochain.tools.base import Tool


class HandOffToAgent(Tool):
    name: Optional[str] = "Hand off"
    description: str = "Hand off to a human agent"
    handoff_msg: str = "Let me hand you off to an agent now"

    def _run(self, *args: Any, **kwargs: Any) -> str:
        return self.handoff_msg
