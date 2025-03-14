import sqlite3
create_tasks_table="""
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY, 
    name text NOT NULL UNIQUE, 
    checkedin  INTEGER DEFAULT 0 NOT NULL,
    running INTEGER DEFAULT 0 NOT NULL, 
    created_date DATE NOT NULL 
);
"""
create_logs_table="""
CREATE TABLE IF NOT EXISTS logs (
    id INTEGER PRIMARY KEY, 
    tasks_id INT NOT NULL, 
    started_at DATE NOT NULL,
    ended_at DATE,
    FOREIGN KEY (tasks_id) REFERENCES tasks (id)
);
"""
def createdb():
    try:
        with sqlite3.connect("tasklogger.db") as conn:
            print(f"Opened SQLite database with version {sqlite3.sqlite_version} successfully.")
            cursor = conn.cursor()
            cursor.execute(create_tasks_table)
            cursor.execute(create_logs_table)
            print(f"created table successfully.")
    except sqlite3.OperationalError as e:
        e.__traceback__
        print("Failed to open database:", e)


if __name__=="__main__":
    createdb()