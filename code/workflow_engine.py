# Written by Brian David Obot
# email: brianobot9@gmail.com

from asyncio import current_task


class WorkFLowEngine:
    """
    This is the class interface for managing tasks execution automatically 
    """
    def __init__(self, name=None, tasks=None, *args, **kwargs):
        self.current_task_id = None
        self.tasks = tasks if tasks is not None else []

    def is_completed(self):
        """ checks that all the task in the current workflow has been completed"""
        pass

    def get_next_task(self):
        """ checks for the current task and get the next tasks in the sequence and sets the current task id to the next task"""
        pass
    
    def get_previous_task(self):
        """ checks for the previous task and get the previous tasks in the sequence using the current_task_id as a reference """
        pass

    def get_current_task(self):
        """ uses the current_task_id to gets the current tasks in the workflow"""
        pass

    def execute_task(self, task=None, *args, **kwargs):
        """ when called, takes a tasked attached to the WFE and executes its appropriately with provided arguments """
        assert task is not None, "the task provided!"
        executed, result = task.run(*args, **kwargs)
        pass

    def add_task(self, task):
        """ adds a task instance to the Engine's current list of task """
        pass

    def remove_task(self, task):
        """ tries to remove a specified task from the list of the tasks attached to the Engine """
        pass

    def number_of_completed_tasks(self):
        """ returns the number of task that be completed """
        pass

    def number_of_waiting_tasks(self):
        """ returns the number of tasks that are waiting execution """
        pass

    def number_of_tasks(self):
        """ returns the number of tasks currently in the workflow engine """
        return len(self.tasks)

    def __repr__(self):
        return f"WorkFlowEngine(number of tasks = {self.number_of_tasks()})"




