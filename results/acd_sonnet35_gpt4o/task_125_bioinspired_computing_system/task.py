import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        biological_inspirations = [
            {
                "inspiration": "Slime mold networks",
                "computing_task": "Optimization of resource distribution"
            },
            {
                "inspiration": "Neural plasticity",
                "computing_task": "Adaptive learning and memory storage"
            }
        ]
        return {
            "1": random.choice(biological_inspirations),
            "2": random.choice(biological_inspirations)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a hypothetical biological computing system inspired by {t['inspiration']} to perform the computing task of {t['computing_task']}. Your response should include:

1. A creative name for your bio-inspired computing system (1 sentence).
2. A brief explanation of the biological inspiration and its relevant properties (2-3 sentences).
3. A detailed description of your proposed bio-inspired computing system, including its components and how they interact (5-6 sentences).
4. An explanation of how your system performs the specified computing task, with a step-by-step breakdown of the process (4-5 sentences).
5. A comparison of your bio-inspired system to traditional computing approaches for the same task, highlighting potential advantages and limitations (3-4 sentences).
6. A discussion of one ethical consideration and one potential real-world application of your proposed system (2-3 sentences each).
7. A suggestion for a future research direction to enhance or expand your proposed system (2-3 sentences).

Ensure your response is grounded in scientific principles while demonstrating creativity in applying biological concepts to computing. Your total response should not exceed 550 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must be based on the biological inspiration of {t['inspiration']}.",
            f"The proposed system must address the computing task of {t['computing_task']}.",
            "The submission must include all seven required elements as specified in the instructions, including a creative name for the system.",
            "The proposed bio-inspired computing system must be logically coherent and demonstrate a clear understanding of both biological and computing principles.",
            "The response must be creative while remaining grounded in scientific concepts."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
