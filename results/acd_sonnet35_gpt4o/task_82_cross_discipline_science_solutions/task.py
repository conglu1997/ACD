import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "problem_field": "Agriculture",
                "problem": "Develop a method to increase crop yield in arid regions",
                "solution_field": "Astrophysics"
            },
            {
                "problem_field": "Urban Planning",
                "problem": "Design a traffic flow system to reduce congestion in large cities",
                "solution_field": "Microbiology"
            },
            {
                "problem_field": "Medicine",
                "problem": "Create a non-invasive method for early detection of cardiovascular diseases",
                "solution_field": "Geology"
            },
            {
                "problem_field": "Environmental Science",
                "problem": "Develop a new method for removing microplastics from oceans",
                "solution_field": "Quantum Physics"
            }
        ]
        return {
            "1": random.choice(scenarios),
            "2": random.choice(scenarios)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Your task is to solve a problem in {t['problem_field']} using principles from {t['solution_field']}. The problem is: {t['problem']}\n\nProvide your solution in the following format:\n\n1. Proposed Solution (3-4 sentences):\nDescribe your innovative solution that applies principles from {t['solution_field']} to address the problem.\n\n2. Scientific Explanation (4-5 sentences):\nExplain the scientific principles from {t['solution_field']} that you're applying and how they relate to solving the problem in {t['problem_field']}.\n\n3. Potential Challenges (2-3 points):\nIdentify possible obstacles or limitations in implementing your solution.\n\n4. Future Implications (2-3 sentences):\nDiscuss how this cross-disciplinary approach might impact future research or applications in both fields."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The solution creatively applies principles from {t['solution_field']} to the problem in {t['problem_field']}.",
            "The scientific explanation is clear, accurate, and demonstrates a good understanding of both fields.",
            "The potential challenges identified are relevant and well-reasoned.",
            "The future implications discussed are insightful and consider both fields.",
            "The response follows the requested format and addresses all parts of the task."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
