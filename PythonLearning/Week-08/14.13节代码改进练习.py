# 给 Task 增加字段 priority: Literal["low", "mid", "high"] = "mid" 
# 和 due: datetime | None = None，
# 并加一个校验器：截止时间不能早于创建时间。
from datetime import datetime
from pathlib import Path
from typing import Literal

from pydantic import BaseModel, Field, field_validator


class Task(BaseModel):
    id: int
    status: Literal["todo", "doing", "dong"] = "todo"
    title: str = Field(min_length=1, max_length=80)
    created_at: datetime = Field(default_factory=datetime.now)
    priority: Literal["low", "mid", "heigh"] = "mid"
    due: datetime | None = None

    @field_validator(mode="after")      # 先检查之前的，再检查自定义的
    def due_should_gt_created(self) -> "Task":
        if self.due and self.due <= self.created_at:
            raise ValueError(f"结束时间：{self.due} 早于创建时间：{self.created_at}")
        return self

class TaskList(BaseModel):
    tasks: list[Task] = []

    def add(self, new_title: str) -> Task:
        new_id = max((t.id for t in self.tasks), default=0) + 1
        t = Task(id=new_id, title=new_title, due=datetime.now)
        self.tasks.append(t)
        return t

    def done(self, tid: int) -> None:
        for t in self.tasks:
            if t.id == tid:
                t.status = "dong"
        raise ValueError(f"任务 id={tid} 不存在")

    def save(self, path: Path) -> None:
        path.write_text(self.model_dump_json(indent=2), encoding="utf-8")

    @classmethod
    def load(cls, path: Path) -> "TaskList":
        if not path.exists():
            return cls()
        return cls.model_validate_json(path.read_text(encoding="utf-8"))
