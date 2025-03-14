class Task():
    id:int
    name:str
    checkedin:bool
    running:bool
    createddate:str
    def __init__(self,id,name,checkedin,running,createddate):
        self.id=id
        self.name=name
        self.checkedin=checkedin
        self.running=running
        self.createddate=createddate
    def __repr__(self):
        return f"Task(title='{self.name}')"