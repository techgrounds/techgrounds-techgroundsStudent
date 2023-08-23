from constructs import Construct
from aws_cdk import (
    Stack
)


class CdkWorkshopStack(Stack):

    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Nothing here!
