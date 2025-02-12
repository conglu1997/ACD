class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"prompt": "Design a fictional wearable device that can enhance human cognitive abilities. Provide details on its functions, technical aspects, and potential impact on society."},
            "2": {"prompt": "Create a fictional clean energy source that could revolutionize energy production. Explain how it works, its technical specifications, and the potential environmental and societal impacts."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design and explain a fictional piece of technology based on the following prompt:\n\n{t['prompt']}\n\nYour response should include:\n1. An overview of the technology and its primary functions.\n2. Technical details explaining how it works.\n3. Potential impacts on society and the environment.\n\nSubmit your response as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should provide a clear and imaginative overview of the fictional technology.",
            "The technical details should be logically consistent and plausible within the fictional context.",
            "The potential impacts on society and the environment should be thoroughly explored and well-articulated."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
