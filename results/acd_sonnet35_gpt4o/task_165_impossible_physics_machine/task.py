import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "law": "Conservation of Energy",
                "scenario": "A perpetual motion machine that seems to produce more energy than it consumes"
            },
            {
                "law": "Second Law of Thermodynamics",
                "scenario": "A device that appears to decrease entropy in a closed system without external input"
            },
            {
                "law": "Conservation of Mass",
                "scenario": "A container that seems to create matter from nothing"
            },
            {
                "law": "Special Relativity",
                "scenario": "A communication device that appears to transmit information faster than the speed of light"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a hypothetical machine that appears to violate the law of {t['law']}. The machine should seem to achieve the following: {t['scenario']}.

Your task is to:

1. Provide a detailed description of your machine, including its key components and how it appears to function (100-150 words).
2. Explain why this machine seems to violate {t['law']} (50-75 words).
3. Propose a creative explanation for how the machine might work without actually violating the law of physics. This explanation should be grounded in real scientific principles but may involve highly advanced technology or theoretical concepts (150-200 words).
4. Discuss two potential applications of this machine if it could be built, and explain their significance (75-100 words).
5. Identify one ethical concern that might arise from the existence of such a machine and propose a solution (50-75 words).

Ensure your response is scientifically grounded, creative, and demonstrates a deep understanding of the relevant physical laws and their implications. Use clear, concise language and organize your answer using the following headers:

1. Machine Description
2. Apparent Violation
3. Possible Explanation
4. Potential Applications
5. Ethical Consideration
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must address the law of {t['law']} and the scenario: {t['scenario']}",
            "The machine description should be detailed and coherent",
            "The explanation for how the machine works without violating physics should be creative yet scientifically grounded",
            "The response should demonstrate a deep understanding of the relevant physical laws",
            "The potential applications and ethical consideration should be thoughtful and relevant"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
