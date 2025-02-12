class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "problem": "You are tasked with designing a water filtration system for a small village. The available resources include sand, gravel, activated charcoal, and a large container. Describe your design, the principles behind it, and the steps for constructing and using the filtration system. Your solution should be practical and easy to understand. Additionally, ensure that the system can filter out both physical particles and chemical contaminants."
            },
            "2": {
                "problem": "A farmer is facing issues with soil erosion on their farmland. Propose a sustainable solution to mitigate soil erosion, considering the local climate and available resources. Explain the scientific principles behind your solution and provide a step-by-step plan for implementation. Also, ensure that your solution can be implemented with minimal cost and maintenance."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Solve the following scientific problem: {t['problem']} Provide a detailed explanation of your solution, including the scientific principles involved and a step-by-step plan for implementation. Ensure your solution is practical, easy to understand, and meets the specified constraints. Submit your response as a plain text string. Example format: \nSolution: [Your solution here]"

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = []
        if 'water filtration' in t['problem']:
            criteria.append("The solution should include a method to filter out physical particles.")
            criteria.append("The solution should include a method to filter out chemical contaminants.")
        elif 'soil erosion' in t['problem']:
            criteria.append("The solution should consider the local climate.")
            criteria.append("The solution should be sustainable and cost-effective.")
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
