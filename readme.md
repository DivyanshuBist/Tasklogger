# Tasklogger
## utlity tool to track time
### how to install
* create and activate virtual environment 
* install package locally using the following command `pip install .`.Use `pip install --editable .` for development. 
* run dbinit.py file `python dbinit.py`. 
* now you are ready to use.

### how tasklogger works
* first step is to create task `tasklogger create <taskname>`.remember,task names are unique 
* now you have to checkout to the task `tasklogger checkout <taskname>`
* you are ready to track .use `tasklogger start` to start tracking time
* `tasklogger stop` to end tracking.

### Some points to consider
* task name are unique
* you can only checkout to new task only if previous task is not being tracked currently i.e. first `tasklogger end` to end tracking previous task and then `tasklogger checkout <taskname>`.


