class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "context": "John had been working tirelessly for weeks. When he finally submitted his project, he felt a huge weight lift off his shoulders. Later, he decided to treat himself to a nice dinner."
            },
            "2": {
                "context": "During the meeting, Sarah broke the ice by sharing a funny story about her vacation, which made everyone laugh and feel more comfortable."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Interpret the idiomatic expression used in the following context and explain its meaning:

Context: {t['context']}

Additionally, generate a new sentence using the same idiomatic expression but in a different context.

Your response should include:
1. An explanation of the idiomatic expression
2. A new sentence using the idiomatic expression in a different context

Submit your response as a plain text string in the following format:
Explanation: [Your explanation]
New Sentence: [Your new sentence]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The explanation should accurately convey the meaning of the idiomatic expression.",
            "The new sentence should use the idiomatic expression correctly in a different context."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
