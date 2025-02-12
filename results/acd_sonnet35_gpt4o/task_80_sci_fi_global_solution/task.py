import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        sci_fi_principles = [
            {
                "principle": "The Force (Star Wars)",
                "description": "An energy field created by all living things that connects everything in the universe."
            },
            {
                "principle": "Psychohistory (Foundation series)",
                "description": "A fictional science that combines history, sociology, and mathematical statistics to make general predictions about the future behavior of very large groups of people."
            }
        ]
        global_issues = [
            "Climate change",
            "Global food security",
            "Pandemic prevention and management",
            "Sustainable energy production"
        ]
        tasks = {}
        for i in range(2):
            tasks[str(i+1)] = {
                "sci_fi_principle": random.choice(sci_fi_principles),
                "global_issue": random.choice(global_issues)
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a hypothetical technology based on the fictional scientific principle '{t['sci_fi_principle']['principle']}' from science fiction to address the real-world global issue of {t['global_issue']}. Then, analyze its potential impacts and ethical considerations.

Your response should include:

1. Technology Description (3-4 sentences):
   Describe your proposed technology and how it utilizes the given sci-fi principle to address the global issue.

2. Scientific Explanation (3-4 sentences):
   Provide a pseudo-scientific explanation of how your technology works, incorporating both the fictional principle and real-world scientific concepts.

3. Implementation Strategy (2-3 sentences):
   Briefly outline how this technology could be implemented on a global scale.

4. Potential Positive Impacts (2-3 points):
   List and briefly explain the potential positive outcomes of implementing this technology.

5. Potential Negative Consequences (2-3 points):
   Identify possible drawbacks or unintended negative consequences of the technology.

6. Ethical Considerations (3-4 sentences):
   Discuss the ethical implications of developing and using this technology, considering issues such as access, control, and potential misuse.

7. Mitigation Strategies (2-3 points):
   Propose strategies to address the identified ethical concerns and negative impacts.

Ensure your response is creative yet grounded in both the fictional scientific principle and real-world considerations. Demonstrate a nuanced understanding of the global issue, the sci-fi concept, and their potential interactions.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must design a technology based on the sci-fi principle '{t['sci_fi_principle']['principle']}' to address {t['global_issue']}",
            "The technology description should be creative and plausible within the context of the sci-fi principle",
            "The scientific explanation should incorporate both fictional and real-world concepts",
            "The implementation strategy should be logical and consider global scale application",
            "The response should thoroughly analyze both positive and negative potential impacts",
            "The ethical considerations should be thoughtful and relevant to the proposed technology",
            "The mitigation strategies should address the identified concerns and be feasible",
            "The overall response should demonstrate interdisciplinary thinking and creative problem-solving"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
