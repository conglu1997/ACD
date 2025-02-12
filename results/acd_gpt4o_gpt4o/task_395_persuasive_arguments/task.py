class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"prompt": "Identify the thesis statement, main arguments, and conclusion in the following persuasive text:\n\n'To reduce pollution and improve public health, our city should invest in a comprehensive public transportation system. Public transportation reduces the number of cars on the road, leading to lower emissions. Moreover, it provides a reliable and affordable means for people to commute, especially for those who cannot afford private vehicles. Investing in public transportation is not only environmentally sound but also promotes equality and improves the quality of life for all residents.'"},
            "2": {"prompt": "Generate a persuasive argument on the topic: 'The importance of regular exercise for mental health.' Ensure your argument includes a clear thesis statement, at least three supporting arguments, and a conclusion."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task involves understanding and generating persuasive arguments:

Prompt: {t['prompt']}

For Task 1: Identify the thesis statement, main arguments, and conclusion in the provided text. Clearly label each element in your response (e.g., 'Thesis statement: ...', 'Main argument 1: ...', 'Main argument 2: ...', 'Conclusion: ...').
For Task 2: Generate a persuasive argument on the given topic. Ensure your argument includes a clear thesis statement, at least three supporting arguments, and a conclusion. Your response should be coherent, logical, and persuasive. Clearly label each part of your argument (e.g., 'Thesis statement: ...', 'Supporting argument 1: ...', 'Supporting argument 2: ...', 'Supporting argument 3: ...', 'Conclusion: ...').
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The response for Task 1 should accurately identify the thesis statement, main arguments, and conclusion.", "The argument generated in Task 2 should include a clear thesis statement, at least three supporting arguments, and a conclusion.", "The generated argument should be coherent, logical, and persuasive."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
