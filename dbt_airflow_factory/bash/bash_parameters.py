"""POD representing Kubernetes operator config file."""

from typing import Any, Dict, List, Optional




class BashExecutionParameters:
    """POD representing Bash operator config file.
    :param execution_script: Script that will be executed inside pod.
    :type execution_script: str
    """

    def __init__(
        self,
        execution_script: str = "dbt --no-write-json",
        **kwargs: Any,
    ) -> None:
        self.execution_script = execution_script

