class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"text": "We should implement a four-day workweek because it would increase productivity, improve employee well-being, and reduce operational costs.", "criteria": "Identify and explain the persuasive techniques used in the text."},
            "2": {"topic": "The importance of renewable energy", "criteria": "Create a persuasive argument about the importance of renewable energy, focusing on environmental, economic, and social benefits. Ensure your argument is logically coherent and emotionally appealing."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "text" in t:
            instructions = f"""Your task is to analyze the following persuasive text and identify the persuasive techniques used:

Text: {t['text']}

Provide your analysis in plain text format, clearly explaining the techniques used and their effectiveness. Format your response as follows:
1. Technique: <name of technique>
2. Explanation: <how the technique is used and its effectiveness>"""
        else:
            instructions = f"""Your task is to create a persuasive argument based on the following topic:

Topic: {t['topic']}

Ensure your argument is logically coherent and emotionally appealing. Focus on the following criteria:
1. Environmental benefits
2. Economic benefits
3. Social benefits

Provide your argument in plain text format, structured as follows:
1. Introduction: <your introduction>
2. Body: <your main points and supporting arguments>
3. Conclusion: <your conclusion>"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should accurately identify and explain the persuasive techniques used.",
            "The response should be logically coherent and emotionally appealing.",
            "The response should include all required sections: Introduction, Body, and Conclusion.",
            "The response should focus on environmental, economic, and social benefits." if "topic" in t else "The explanation should clearly describe how each technique is used and its effectiveness." 
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
