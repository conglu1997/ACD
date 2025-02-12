class TaskFamily:

    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "project_description": "Develop a new mobile application.",
                "tasks": [
                    {"task": "Design user interface", "estimated_time": "2 weeks", "priority": "high", "dependencies": []},
                    {"task": "Develop backend", "estimated_time": "4 weeks", "priority": "high", "dependencies": ["Design user interface"]},
                    {"task": "Integrate frontend and backend", "estimated_time": "3 weeks", "priority": "medium", "dependencies": ["Develop backend"]},
                    {"task": "Test application", "estimated_time": "2 weeks", "priority": "high", "dependencies": ["Integrate frontend and backend"]},
                    {"task": "Deploy to app store", "estimated_time": "1 week", "priority": "medium", "dependencies": ["Test application"]}
                ]
            },
            "2": {
                "project_description": "Organize a corporate event.",
                "tasks": [
                    {"task": "Book venue", "estimated_time": "1 week", "priority": "high", "dependencies": []},
                    {"task": "Arrange catering", "estimated_time": "2 weeks", "priority": "medium", "dependencies": ["Book venue"]},
                    {"task": "Send invitations", "estimated_time": "1 week", "priority": "high", "dependencies": ["Book venue"]},
                    {"task": "Confirm RSVPs", "estimated_time": "2 weeks", "priority": "medium", "dependencies": ["Send invitations"]},
                    {"task": "Set up event space", "estimated_time": "3 days", "priority": "high", "dependencies": ["Confirm RSVPs"]}
                ]
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        project_description = t["project_description"]
        tasks = t["tasks"]
        instructions = f"Your task is to manage the following project: {project_description}\n\nYou are provided with a list of tasks, each with an estimated time to complete, a priority level, and any dependencies it may have. Your goal is to create a project timeline that optimizes for efficiency and ensures the high-priority tasks are completed on time.\n\nTasks:\n"
        for task in tasks:
            instructions += f"- {task['task']} (Estimated time: {task['estimated_time']}, Priority: {task['priority']}, Dependencies: {', '.join(task['dependencies'])})\n"
        instructions += "\nYour response should include:\n1. A step-by-step timeline for completing the project.\n2. Justification for the order in which tasks are completed.\n3. Identification of any potential risks and how you plan to mitigate them.\n\nProvide your response in plain text format, ensuring that it is comprehensive and well-structured."
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should include a clear and logical step-by-step timeline.",
            "The response should justify the order of task completion.",
            "The response should identify potential risks and propose mitigation strategies.",
            "The response should be comprehensive and well-structured."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
