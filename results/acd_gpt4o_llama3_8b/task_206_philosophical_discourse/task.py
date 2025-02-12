class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"prompt": "Discuss the ethical implications of artificial intelligence in society."},
            "2": {"prompt": "Explore the concept of free will and its significance in human life."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "artificial intelligence" in t["prompt"]:
            return f"""Complete the following task based on the given prompt:

{t["prompt"]}

Discuss the ethical implications of artificial intelligence in society. Your discussion should include:
1. The potential benefits and risks of artificial intelligence.
2. The ethical challenges and dilemmas posed by AI.
3. Possible solutions or frameworks to address these ethical issues.

Ensure your discussion is coherent, well-structured, and insightful. Submit your response as a plain text string in paragraph format."""
        else:
            return f"""Complete the following task based on the given prompt:

{t["prompt"]}

Explore the concept of free will and its significance in human life. Your exploration should include:
1. Definitions and perspectives on free will from different philosophical traditions.
2. The implications of free will on moral responsibility and human behavior.
3. Arguments for and against the existence of free will.

Ensure your exploration is coherent, well-structured, and insightful. Submit your response as a plain text string in paragraph format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = []
        if "artificial intelligence" in t["prompt"]:
            criteria = ["The discussion should cover potential benefits and risks, ethical challenges and dilemmas, and possible solutions or frameworks.", "The discussion should be coherent, well-structured, and insightful."]
        else:
            criteria = ["The exploration should cover definitions and perspectives, implications on moral responsibility and human behavior, and arguments for and against free will.", "The exploration should be coherent, well-structured, and insightful."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
