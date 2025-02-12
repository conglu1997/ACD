class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"scientific_principle": "Quantum Entanglement"},
            "2": {"scientific_principle": "Artificial Intelligence and Consciousness"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to create an engaging and scientifically plausible science fiction concept based on the following scientific principle:

{t["scientific_principle"]}

Your response should include:
1. A brief summary of the science fiction concept.
2. An explanation of how the scientific principle is applied in this concept.
3. A description of the main characters, setting, and plot elements involved.

Ensure that your concept is imaginative, yet grounded in scientific plausibility. Your explanation should articulate how the scientific principle is realistically integrated into the fiction. Provide your response in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should include an engaging science fiction concept based on the given scientific principle.",
            "The response should include a brief summary of the concept, an explanation of how the scientific principle is applied, and a description of the main characters, setting, and plot elements.",
            "The concept should be imaginative yet grounded in scientific plausibility, and the explanation should articulate how the scientific principle is realistically integrated into the fiction."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
