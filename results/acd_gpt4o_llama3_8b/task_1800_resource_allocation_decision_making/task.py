class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "resources": 100,
                "projects": {
                    "A": {"cost": 50, "benefit": 60},
                    "B": {"cost": 30, "benefit": 40},
                    "C": {"cost": 20, "benefit": 25},
                    "D": {"cost": 10, "benefit": 15}
                }
            },
            "2": {
                "resources": 200,
                "projects": {
                    "X": {"cost": 70, "benefit": 90},
                    "Y": {"cost": 60, "benefit": 80},
                    "Z": {"cost": 50, "benefit": 70},
                    "W": {"cost": 40, "benefit": 50},
                    "V": {"cost": 30, "benefit": 35}
                }
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        projects_str = '\n'.join([f"{proj}: Cost = {details['cost']}, Benefit = {details['benefit']}" for proj, details in t['projects'].items()])
        return f"""You are given {t['resources']} units of resources to allocate among the following projects. Each project has a cost and a corresponding benefit. Your goal is to maximize the total benefit while not exceeding the available resources.

Projects:
{projects_str}

Provide your allocation as a comma-separated list of project names in the format: 'Project1, Project2, ...'."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        projects = t['projects']
        allocated_projects = submission.split(', ')
        try:
            total_cost = sum(projects[proj]['cost'] for proj in allocated_projects)
            total_benefit = sum(projects[proj]['benefit'] for proj in allocated_projects)
        except KeyError:
            return 0.0  # Fail if the submission includes invalid project names
        if total_cost <= t['resources']:
            validation_criteria = ["The response should be a comma-separated list of project names in the format: 'Project1, Project2, ...'."]
            return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
        return 0.0
