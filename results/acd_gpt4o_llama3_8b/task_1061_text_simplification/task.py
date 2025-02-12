class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"complex_text": "The government has implemented a series of measures to mitigate the economic impact of the pandemic, including stimulus packages and unemployment benefits, which aim to provide financial support to individuals and businesses affected by the crisis."},
            "2": {"complex_text": "The rapid advancements in artificial intelligence and machine learning have the potential to revolutionize various industries, leading to increased efficiency and automation, which could result in significant changes to the workforce and economic landscape."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Simplify the following sentence while preserving its original meaning: '{t['complex_text']}'. Your simplified sentence should be clear and easy to understand. Submit your response as a plain text string."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The simplified sentence should accurately preserve the original meaning.", "The simplified sentence should be significantly simpler and easier to understand compared to the original."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
