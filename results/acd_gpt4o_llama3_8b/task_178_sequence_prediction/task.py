class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"sequence": "John left his house and walked to the store. He bought some groceries including milk, bread, and eggs, and then headed to the park. At the park, he met an old friend who he hadn't seen in years, and they decided to..."},
            "2": {"sequence": "Sara woke up early and went for a jog around the neighborhood. Along the way, she ran into her neighbor who mentioned a community event happening later in the day. After finishing her jog and taking a shower, she decided to..."},
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Given the following sequence of events, predict what happens next. Your prediction should be coherent, plausible, and logically follow from the provided context. Ensure your prediction is at least 50 words long. Submit your response as a plain text string.\n\nSequence: {t["sequence"]}"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The prediction should be coherent and logically follow from the given sequence.", "The prediction should be at least 50 words long."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
