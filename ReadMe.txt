Written By 
Brian David Obot 
email-brianobot9@gmail.com (check the bottom for more contact details)
_________________________________________________________________________________


This Project is a pure python pseudo-implementation of a WorkFLow Engine. 

It consists of two python modules 
* tasks.py
* workflow_engine.

*task.py:
    <TaskState: class>
    this class is used to represent the possible state/status of a task, its contains class attributes that include;

    NOT_STARTED -> to represent a state that a task has not be started,
    WAITING     -> to represent a state that a started task is still running
    COMPLETED   -> to represent a state that a task has completed it execution
    CANCELLED   -> to represent a state that a started task execution was stoppe before its finished


    <Task: class>
    this class is to be used to create task objects, the task object enscapulate a code implementation to 
    be used to carry out some automated task, it should be initiated with its first argument being a name (str) to represent the name of the task
    and a second code argument which is a function object which represent the actual code implementation to be perform by the task when 
    executed and any other arbitrary positional or keyword arguments that best fit the specified task instance.

    the task class can also be used a subclass to further give the developer more control over its API

    Example:
    >>> from tasks import Task
    >>> from my_module import send_email_to  #some arbitrary code to be perform by the task

    >>> task_one = Task(name=send_email, code=send_email_to)


*workflow_engine.py:
    <WorkFLowEngine: class>
    this class is the main entry point to start, manage and inspect all tasks in the workflow engine,
    it can be instantiated without any arguments and subsequently fed a list of Task or can be instantiated with a
    first argument as the name :

    Example:
    >>> from workflow_engine import WorkFLowEngine
    >>> from tasks import task1, tasks2

    >>> engine1 = WorkFLowEngine()
    >>> engine2 = WorkFLowEngine(name='Customer Email Verification WorkFlow')
    >>> engine3 = WorkFLowEngine(name='Customer Email Verification WorkFlow', tasks=[task1, tasks2])

    All the instantiation method above are all valid and accepted

    the workflow_engine can be used to execute the task by calling the engine's execute_task method when calls the run method on the current tasks
    the engine can be used to attached unique task sequence id to the task to aid manage the flow of task execution


More specified documentation are presented in the code as docstrings to aid usage, use python's help() function to access more specific 
documentation on the various classes and methods

for More imformation contact the developer at 
email - brianobot9@gmail.com 
phone_1 = +234 7018 977 031
phone_2 = +234 8073 487 154
