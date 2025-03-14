import sqlite3
import datetime
import traceback
DB_name="tasklogger.db"

def create_connection()->sqlite3.Connection:
    try:
        conn=sqlite3.connect(DB_name)
        return conn
    except sqlite3.OperationalError as e:
        print("failed to open database",e)
        return None

def initstatus()->dict:
    currenttaskquery="""
        Select * from tasks where checkedin=1
    """
    currentlogsquery="""
        Select * from logs where ended_at IS NULL
    """
    try:
        with create_connection() as conn :
            cursor=conn.cursor()
            cursor.execute(currenttaskquery)
            task=cursor.fetchall()
            cursor.execute(currentlogsquery)
            logs=cursor.fetchall()
            return {"tasks":task,"logs":logs}
    except Exception as e:  
        print(e)

def DB_insert_task(title)->bool:
    currenttaskquery="""
        Insert into tasks(name,checkedin,running,created_date) values (?,?,?,?)
    """
    try:
        with create_connection() as conn:
            cursor=conn.cursor()
            parameters=(title,0,0,datetime.datetime.now())
            cursor.execute(currenttaskquery,parameters)
            conn.commit()
            return True
    except sqlite3.IntegrityError as e:
        print("task with this name already exists.please use different name")
        return False
    except Exception as ex:
        print(ex)
        return False

def DB_checkout_task(title:str,prevcheckedintask:str)->dict:
    outmap:dict=dict()
    checkouttaskquery="""
        UPDATE tasks set
        checkedin=1 where 
        name=(?)
    """
    updateprevtaskquery="""
        UPDATE tasks set
        checkedin=0 where 
        name=(?)
"""
    try:
        with create_connection() as conn:
            cursor=conn.cursor()
            parameters:tuple=(title,)
            cursor.execute(checkouttaskquery,parameters)
            if(cursor.rowcount==0):
                raise Exception("the task you provided doesn't exists")
            cursor.execute(updateprevtaskquery,(prevcheckedintask,))
            conn.commit()
            outmap["Error"]="ok"
    except sqlite3.OperationalError as e:
        print(e)
        outmap["Error"]=e
        conn.rollback()
    except Exception as e:
        print(e)
        outmap["Error"]=e
        conn.rollback()

def DB_insert_logs(taskid):
    insertlogquery="""
        INSERT into logs(tasks_id,started_at,ended_at) values (?,?,?)
    """
    updatetaskfieldquery="""
    Update tasks set running=1 where id=(?)
    """
    try:
        with create_connection() as conn:
            cursor=conn.cursor()
            cursor.execute(insertlogquery,(taskid,datetime.datetime.now(),None))
            cursor.execute(updatetaskfieldquery,(taskid,))
            conn.commit()
    except Exception as e:
        print(e)    

def DB_update_logs(logid,taskid):
    updatelogquery="""
        UPDATE logs SET ended_at=(?) 
        WHERE id=(?)
    """
    updatetaskquery="""
        UPDATE tasks SET running=0
        where id=(?)
    """
    try:
        with create_connection() as conn:
            cursor=conn.cursor()
            cursor.execute(updatelogquery,(datetime.datetime.now(),logid))
            cursor.execute(updatetaskquery,(taskid,))
            conn.commit()
    except Exception as e:
        print(e)    
        traceback.print_exc()