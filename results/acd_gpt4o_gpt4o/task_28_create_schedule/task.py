class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "tasks": [
                    {"name": "Task A", "duration": 2, "dependencies": []},
                    {"name": "Task B", "duration": 1, "dependencies": ["Task A"]},
                    {"name": "Task C", "duration": 3, "dependencies": ["Task A"]}
                ],
                "start_time": "09:00",
                "end_time": "17:00"
            },
            "2": {
                "tasks": [
                    {"name": "Task X", "duration": 1, "dependencies": []},
                    {"name": "Task Y", "duration": 2, "dependencies": ["Task X"]},
                    {"name": "Task Z", "duration": 2, "dependencies": ["Task Y"]},
                    {"name": "Task W", "duration": 1, "dependencies": []}
                ],
                "start_time": "08:00",
                "end_time": "12:00"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to create a detailed schedule for the following tasks within the given time frame. Each task has a specified duration and may depend on the completion of other tasks. The schedule should be feasible, respecting all task dependencies, and fitting within the specified start and end times. Provide your schedule as a list of tuples (task_name, start_time, end_time), where start_time and end_time are formatted as HH:MM.

Tasks:
{t['tasks']}

Start Time: {t['start_time']}
End Time: {t['end_time']}"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from datetime import datetime, timedelta
        import ast
        from src.eval_helper import eval_with_llm_judge

        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The schedule must respect all task dependencies.",
            "All tasks must be scheduled within the given start and end times.",
            "The schedule must be feasible given the task durations."
        ]

        try:
            schedule = ast.literal_eval(submission)
            task_dict = {task['name']: task for task in t['tasks']}
            time_format = "%H:%M"
            start_time = datetime.strptime(t['start_time'], time_format)
            end_time = datetime.strptime(t['end_time'], time_format)

            # Check if all tasks are scheduled
            scheduled_tasks = set(task[0] for task in schedule)
            if scheduled_tasks != set(task_dict.keys()):
                return 0.0

            # Check the feasibility of the schedule
            for task_name, start, end in schedule:
                task = task_dict[task_name]
                task_start = datetime.strptime(start, time_format)
                task_end = datetime.strptime(end, time_format)

                # Check if the task's duration is correct
                if (task_end - task_start) != timedelta(hours=task['duration']):
                    return 0.0

                # Check if the task is within the allowed time frame
                if task_start < start_time or task_end > end_time:
                    return 0.0

                # Check if dependencies are respected
                for dependency in task['dependencies']:
                    dep_end = next(end for t_name, _, end in schedule if t_name == dependency)
                    if task_start < datetime.strptime(dep_end, time_format):
                        return 0.0

        except (ValueError, SyntaxError):
            return 0.0

        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0