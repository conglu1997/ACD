class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"sentence": "The quick brown fox jumps over the lazy dog."},
            "2": {"sentence": "Artificial intelligence is transforming the way we interact with technology."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Transform the following sentence by paraphrasing it while preserving the original meaning and then summarize it to convey the main idea in fewer words:

{t["sentence"]}

Submit your response as a plain text string in the following format:
Paraphrase: [Your paraphrased sentence]
Summary: [Your summary]."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The paraphrased sentence should preserve the original meaning.", "The paraphrased sentence should be grammatically correct.", "The summary should accurately convey the main idea in fewer words."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
