class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"story_start": "John found a wallet on the street with a significant amount of money and no identification. He was struggling financially and this money could solve many of his problems. He picked up the wallet and..."},
            "2": {"story_start": "Sarah discovered her friend was cheating on an important exam. The friend begged Sarah not to report it, promising that it would never happen again. Sarah was torn between her loyalty to her friend and her sense of justice. She decided to..."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to complete the given story and then analyze the ethical implications of the actions taken by the main character. Ensure that your completion is coherent and logically follows from the given start. Provide your response in two parts:

1. Story Completion: Continue the story from the provided starting point. Write at least 100 words.
2. Ethical Analysis: Analyze the ethical implications of the actions taken by the main character in your story completion. Discuss whether the actions were morally right or wrong and why. Write at least 100 words.

Here is the start of the story:

{t['story_start']}"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The response should include both a completed story and an ethical analysis.", "The story completion should be coherent and logically follow from the given start.", "The ethical analysis should discuss the moral implications of the actions taken by the main character."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
