class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "scenario": "A tenant has been living in an apartment for two years under a lease agreement that requires the landlord to provide 60 days' notice before termination. The landlord provides a 30-day notice of termination. The tenant refuses to move out and claims the notice is invalid. Apply the relevant legal principles to determine if the tenant's claim is valid and provide your reasoning.",
                "principles": "A lease agreement is a binding contract between the landlord and tenant. Any termination of the lease must comply with the notice period specified in the lease agreement. If the notice period is not met, the termination is invalid."
            },
            "2": {
                "scenario": "A company hires an employee under a contract that includes a non-compete clause prohibiting the employee from working for a competitor within a 50-mile radius for one year after leaving the company. The employee leaves the company and immediately joins a competitor located 30 miles away. Apply the relevant legal principles to determine if the company can enforce the non-compete clause and provide your reasoning.",
                "principles": "Non-compete clauses are enforceable if they are reasonable in scope, duration, and geographic area. They must protect a legitimate business interest and not impose undue hardship on the employee. The enforcement of non-compete clauses varies by jurisdiction."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Interpret and apply the given legal principles to the following hypothetical scenario. Provide your reasoning in a clear and concise manner.\n\nScenario:\n{t['scenario']}\n\nLegal Principles:\n{t['principles']}\n\nFormat your response as follows:\n1. State whether the claim is valid or not.\n2. Provide detailed reasoning based on the given legal principles.\n3. Ensure your argument is logically coherent and legally sound."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should clearly state whether the claim is valid or not.",
            "The reasoning should be detailed and based on the given legal principles.",
            "The argument should be logically coherent and legally sound."
        ]
        # Ensure both validity assessment and reasoning are correct for full score.
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
