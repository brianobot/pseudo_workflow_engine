class TaskState:
    NOT_STARTED = 0
    WAITING = 1
    COMPLETED = 2
    CANCELLED = 3

class Task:
    """
    Task represent action, event to be executed by the workflow engine

    Every Task should have a Status indicating its current state, 
    whether it pending execution, it has been completed or it has been cancelled

    STATES are instances of the TaskState Class

    In order to aid in the proper execution of the tasks in a workflow as sequence of tasks with possible branches
    each task is assigned a sequence ID which references the task position in workflow and also its position in a branches sequence

    Example: 
    In a workflow described by the diagram below, the sequence id is as follows

                                        Task a  
                                      / 
        Root_Task -> Conditional Task 
                                      \\
                                        Task b

    Root Task sequence id would then be 1 (without a branched alternative)
    Conditional Task sequence id would be 2 (without a branched alternative)
    Task a sequence id would be 3a (where a denotes that's its at the positive branch of the current sequence number) 
    Task b sequence id would be 3b (where b denotes that's its at the negative branch of the current sequence number) 
    """
    def __init__(self, name=None, *args, **kwargs):
        self.name = name
        self.STATE = TaskState.NOT_STARTED
        self.code = kwargs.get("code")

    def run(self, *args, **kwargs):
        """ this method executes/run the  actual code implementation of the work to be carried out by the task,
            it checks if a function object has been passed into the task instance with the code attribute
            When completed returns True, and a tuple containing the return value of the computation or None
        """
        pass

    def status(self):
        return self.STATE

    def is_completed(self):
        return self.STATE == TaskState.COMPLETED

    def is_cancelled(self):
        return self.STATE == TaskState.CANCELLED

