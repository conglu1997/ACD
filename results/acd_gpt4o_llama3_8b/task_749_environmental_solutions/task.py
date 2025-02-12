class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "problem": "Plastic pollution in oceans",
                "constraints": [
                    "The solution should be cost-effective",
                    "The solution should be scalable",
                    "Consider the impact on marine life"]
            },
            "2": {
                "problem": "Deforestation in the Amazon rainforest",
                "constraints": [
                    "The solution should protect biodiversity",
                    "The solution should involve local communities",
                    "Consider sustainable economic alternatives"]
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        problem = t["problem"]
        constraints = "\n".join(t["constraints"])
        return f"""Propose an innovative solution to the following environmental problem: {problem}.\n
Here are the constraints:\n{constraints}\n
Submit your solution as a plain text string in the following format: 'Solution: [Your solution]\nExplanation: [Your explanation]'."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The solution should be innovative.", 
            "The solution should address the constraints provided.", 
            "The explanation should logically follow from the problem and constraints."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
