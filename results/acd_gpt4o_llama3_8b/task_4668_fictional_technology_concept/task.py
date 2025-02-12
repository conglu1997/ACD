class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "context": "Design a fictional technology concept related to transportation."
            },
            "2": {
                "context": "Design a fictional technology concept related to healthcare."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate a fictional technology concept based on the given context:

Context: {t['context']}

Your response should include the following sections:
1. Technology Concept: Describe the fictional technology, including its name, functionality, and key features.
2. Real-world Applications: Explain how this technology could be applied in real-world scenarios. Provide at least three distinct applications.
3. Implications: Discuss the potential social, economic, and ethical implications of this technology. Consider both positive and negative impacts.

Ensure that your description is clear, coherent, and imaginative. Submit your response as a plain text string in the following format:

Technology Concept: [Your description]
Real-world Applications: [Your applications]
Implications: [Your implications]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = ["The technology concept should be imaginative and coherent.", "The real-world applications should be feasible and distinct.", "The implications should consider multiple perspectives, including social, economic, and ethical impacts."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
