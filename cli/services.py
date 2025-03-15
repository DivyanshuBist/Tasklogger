from  cli.dbservices import * 
from .models.task import Task
from .models.log import Log
class cliservices:
    current_task=None
    def __init__(self):
        self.current_task:list= [Task(id=row[0], name=row[1], checkedin=row[2],running=row[3],createddate=row[4]) for row in initstatus()["tasks"]]
        self.current_logs=[Log(id=row[0],tasks_id=row[1],started_at=row[2],ended_at=row[3]) for row in initstatus()["logs"]]
    def createtask(self,title)->dict:
        outmap:dict=dict()
        if(DB_insert_task(title)==True):
            outmap["Error"]="ok"      
        else:
            outmap["Error"]="error" 
        return outmap

    def checkouttask(self,title)->dict:
        if len(self.current_task)==0: 
            return DB_checkout_task(title,None)
        elif (len(self.current_task)>0 and self.current_task[0].running==0):
            return DB_checkout_task(title,self.current_task[0].name)
        else:
            return {"Error":"already logging task.please end the task before new task checkout"}
        
    def current_status(self)->dict:
        outmap:dict=dict()
        outmap["task"]=""
        outmap["logging"]="No"        
        if(len(self.current_task)>0):
            outmap["task"]=self.current_task[0].name
            outmap["logging"]="Yes" if self.current_task[0].running==True else "No"
        return outmap

    def starttasklogging(self)->dict:
        outmap:dict=dict()
        if len(self.current_task)==0:
            outmap["Error"]="Checkout task before start logging"
        elif self.current_task[0].running==1:
            outmap["Error"]="End current logging before starting again"
        else:
            outmap["Error"]=DB_insert_logs(self.current_task[0].id)
        return outmap

    def endtasklogging(self)->dict:
        outmap:dict=dict()
        if len(self.current_task)==0:
            outmap["Error"]="Checkout  task and start logging"
        elif self.current_task[0].running==0:
            outmap["Error"]="Start logging  task before ending"
        else :
            outmap["Error"]=DB_update_logs(self.current_logs[0].id,self.current_task[0].id)
        return outmap