class Log():
    id:int
    tasks_id:str
    started_at:str
    ended_at:str
    def __init__(self,id,tasks_id,started_at,ended_at):
        self.id=id
        self.tasks_id=tasks_id
        self.started_at=started_at
        self.ended_at=ended_at
    def __repr__(self):
        return f"Log(task_id='{self.tasks_id},start={self.started_at},end={self.ended_at}')"