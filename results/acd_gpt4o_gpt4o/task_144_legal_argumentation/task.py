class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"scenario": "A company is being sued for breach of contract by a former client. The client claims that the company failed to deliver the agreed-upon services, while the company argues that the client's demands exceeded the scope of the original contract.", "role": "Defend the company by drafting a legal argument that addresses the client's claims and supports the company's position."},
            "2": {"scenario": "An individual is suing a restaurant for negligence after slipping and falling on a wet floor. The restaurant contends that clear warning signs were posted and that the individual was not paying attention.", "role": "Represent the individual by drafting a legal argument that demonstrates the restaurant's negligence and supports the individual's claim for damages."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        scenario = t["scenario"]
        role = t["role"]
        instructions = f"""Your task is to draft a legal argument based on the following scenario:\n\nScenario:\n{scenario}\n\nRole:\n{role}\n\nPlease provide a well-reasoned and coherent argument that addresses the key issues and supports your assigned position. Your response should be formatted as follows:\n\nLegal Argument:\n[Your argument here]"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The argument should be well-reasoned and coherent.",
            "The argument should address the key issues in the scenario.",
            "The argument should support the assigned position."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
