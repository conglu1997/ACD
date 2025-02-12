class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"prompt": "Imagine a future where humans have developed technology to control the weather. Describe this technology and its potential implications for society, the environment, and global politics."},
            "2": {"prompt": "Speculate on a scenario where humans discover a microorganism on Mars that can significantly extend human lifespan. Describe the scientific, ethical, and societal implications of this discovery."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Create a speculative scientific scenario based on the following prompt. Describe the technology or discovery in detail and discuss its potential implications and outcomes. Your response should be at least 300 words long and include at least three distinct implications or outcomes.

Prompt: {t['prompt']}

Provide your scenario in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The scenario should be scientifically plausible.", "The implications and outcomes should be logically reasoned and detailed.", "The response should be at least 300 words long.", "The response should include at least three distinct implications or outcomes."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
