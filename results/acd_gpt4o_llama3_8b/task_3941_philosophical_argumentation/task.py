class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "data": {
                    "prompt": "Is it morally permissible to lie to protect someone's feelings?"
                }
            },
            "2": {
                "data": {
                    "prompt": "Can a truly selfless act exist?"
                }
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        prompt = t['data']['prompt']
        return f"""Construct a detailed philosophical argument in response to the following prompt: {prompt}. Your argument should include a clear thesis, supporting premises, and a conclusion. Additionally, consider and respond to a potential counterargument.

Submit your response as a plain text string in the following format:

Thesis: [Your thesis]
Premises: [Your premises]
Conclusion: [Your conclusion]
Counterargument: [A potential counterargument and your response to it]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The argument should be logically coherent and well-structured.",
            "The submission should include a clear thesis, supporting premises, and a conclusion.",
            "The response should address a potential counterargument effectively."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
