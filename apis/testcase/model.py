# --coding:utf-8--
from samaker import samaker


@samaker.dataclass
class CreatePlan:
    name: str
    env: list
    case_list: list
    project_id: int
    priority: str = "P0"
    cron: str = "* 23 * * *"
    ordered: bool = True
    pass_rate: int = 100
