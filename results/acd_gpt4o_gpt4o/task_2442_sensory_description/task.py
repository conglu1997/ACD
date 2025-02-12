class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"scenario": "You are tasting a freshly baked chocolate chip cookie for the first time."},
            "2": {"scenario": "You are walking through a flower garden filled with various blooming flowers in the spring."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return (
            f"Describe the following sensory experience in detail:\n{t['scenario']}\n\n"
            "Your description should include vivid and detailed sensory elements, focusing on taste and/or smell as appropriate. Use descriptive and evocative language to convey the essence of the sensory experience. Ensure your description is coherent, immersive, and captures the sensory impact of the scenario. Provide your response in plain text format."
        )

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The description should be coherent and well-structured.",
            "The description should include vivid and detailed sensory elements.",
            "The language should be descriptive and evocative.",
            "The description should convey the sensory impact of the scenario.",
            "The response should be in plain text format."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0