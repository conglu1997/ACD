class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"theme": "technology", "context": "Describe a humorous situation involving a robot and a human."},
            "2": {"theme": "animals", "context": "Create a joke about a cat and a dog getting into a funny situation."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to generate a joke based on the given theme and context.

Theme: {t['theme']}

Context: {t['context']}

Ensure that your joke is humorous, contextually appropriate, and clearly conveys the intended humor. Provide your response in the following format:

Joke: [Your joke]

Example:

Theme: Food
Context: Create a joke about a chef and a talking vegetable.
Joke: Why did the tomato turn red? Because it saw the salad dressing!"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The joke should be humorous and contextually appropriate.",
            "The joke should clearly convey the intended humor.",
            "The joke should be original and not a common cliché.",
            "The joke should be coherent and easily understandable." 
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
