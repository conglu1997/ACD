class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"scenario": "A factory has 5 machines and 8 tasks to complete. Each task can only be performed by a specific set of machines, and each machine can only handle one task at a time. The goal is to assign tasks to machines in such a way that all tasks are completed in the shortest possible time. The following are the processing times (in hours) for each task on each machine:\n\nMachine 1: Task 1 (3), Task 2 (2)\nMachine 2: Task 1 (4), Task 3 (1)\nMachine 3: Task 2 (5), Task 4 (3)\nMachine 4: Task 3 (2), Task 5 (4), Task 6 (1)\nMachine 5: Task 4 (1), Task 6 (2), Task 7 (3), Task 8 (2)\n\nTasks 1 and 2 must be completed before Task 4 can start. Tasks 3 and 5 must be completed before Task 7 can start.", "question": "Devise a schedule that minimizes the total time required to complete all tasks. Provide the optimal schedule and the total time required."},
            "2": {"scenario": "A conference is being organized with 6 sessions and 4 available rooms. Each session has a specific duration and certain sessions must be scheduled before others. The following are the durations (in hours) and dependencies for each session:\n\nSession 1: 2 hours\nSession 2: 1 hour\nSession 3: 3 hours\nSession 4: 2 hours (after Session 1)\nSession 5: 1 hour (after Session 2)\nSession 6: 2 hours (after Session 3 and Session 5)\n\nThe goal is to schedule all sessions in the available rooms while respecting the dependencies, and minimizing the total time required for the conference.", "question": "Devise a schedule that minimizes the total time required for the conference. Provide the optimal schedule and the total time required."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to solve the following scheduling problem by optimizing resource allocation and meeting the specified constraints:\n\n{t['scenario']}\n\nYour response should include:\n1. A clear description of the optimal schedule, including which tasks or sessions are assigned to which resources (machines or rooms) and the order in which they are performed.\n2. The total time required to complete all tasks or sessions.\n\nEnsure your response is well-organized, logically structured, and includes all required components in a clear manner."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should include a clear description of the optimal schedule, including which tasks or sessions are assigned to which resources (machines or rooms) and the order in which they are performed.",
            "The response should include the total time required to complete all tasks or sessions.",
            "The response should be well-organized and logically structured."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
