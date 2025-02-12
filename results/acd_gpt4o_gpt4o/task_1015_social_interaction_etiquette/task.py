class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            '1': {'scenario': 'You are at a formal dinner party. The host introduces you to an important guest who has just arrived. How do you greet them and what do you say to start a conversation?', 'analysis_text': 'At a formal dinner party, Emily was introduced to Mr. Johnson, a renowned author. She smiled warmly, extended her hand, and said, "It’s a pleasure to meet you, Mr. Johnson. I’ve heard so much about your work." Mr. Johnson responded with a nod and replied, "Thank you, Emily. I’m glad to be here." They began discussing Mr. Johnson’s latest book.'},
            '2': {'scenario': 'You are in a business meeting, and a colleague makes a suggestion that you believe is flawed. How do you respond to address the issue without offending your colleague?', 'analysis_text': 'During a business meeting, John suggested a new marketing strategy. Sarah believed it had several flaws. She responded, "John, I appreciate your innovative idea. However, I have some concerns about the potential risks involved. Could we perhaps discuss some alternatives to mitigate these risks?" John nodded, appreciating Sarah’s respectful approach.'}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task involves two parts: response generation and interaction analysis.

Part 1: Response Generation
Read the given social scenario and generate an appropriate response. Ensure your response is respectful, contextually appropriate, and follows social etiquette. Provide your response in plain text format.

Scenario: {t['scenario']}

Part 2: Interaction Analysis
Analyze the provided social interaction. Identify key elements of social etiquette, potential pitfalls, and suggest improvements. Provide your analysis in plain text format.

Provided Interaction: {t['analysis_text']}"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            'The generated response should be respectful and contextually appropriate.',
            'The response should follow social etiquette.',
            'The analysis should correctly identify key elements, potential pitfalls, and suggest improvements.'
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
