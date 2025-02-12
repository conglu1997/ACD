class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"concept": "A bustling cityscape at night", "synthetic_examples": ["A tranquil beach at sunrise", "A serene countryside in autumn"]},
            "2": {"concept": "A dense forest with a hidden waterfall", "synthetic_examples": ["A snowy mountain peak under a clear sky", "A vibrant coral reef"]}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        examples = '\n'.join(t.get('synthetic_examples', []))
        return f"""Generate a detailed visual description of the following concept. Your description should be vivid, clear, and provide enough detail for someone to visualize the scene accurately. Ensure your description is at least 150 words long.

Concept: {t['concept']}

Additional examples:
{examples}

Submit your response as a plain text string in the following format:

Visual Description:
[Your detailed visual description]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        try:
            from src.eval_helper import eval_with_llm_judge
            instructions = TaskFamily.get_instructions(t)
            criteria = [f"The response should provide a vivid and detailed visual description of the concept: {t['concept']}"]
            return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
        except Exception as e:
            return 0.0
