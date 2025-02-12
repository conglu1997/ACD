class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"event": "The construction of the Great Pyramid of Giza.", "context": "Ancient Egypt during the Old Kingdom, around 2580-2560 BC.", "description": "Analyze the construction of the Great Pyramid of Giza. Discuss the techniques used, the labor force involved, the purpose of the pyramid, and its significance in ancient Egyptian culture."},
            "2": {"event": "The Peloponnesian War.", "context": "Ancient Greece, 431-404 BC.", "description": "Analyze the causes and consequences of the Peloponnesian War between Athens and Sparta. Discuss the key events, the political and social impact on Greek city-states, and the long-term implications for ancient Greek civilization."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to analyze the following historical event and context:

Event: {t['event']}

Context: {t['context']}

{t['description']}

Ensure your analysis includes:
1. A detailed explanation of the event and its context.
2. An examination of the techniques, causes, and consequences associated with the event.
3. An exploration of the significance and implications of the event in ancient history.
4. At least 500 words in total.
5. Specific details such as key figures involved, any technological advancements, and cultural impacts.

Provide your analysis in plain text format.

Example response format:
1. Explanation: [Detailed explanation of the event and context]
2. Examination: [Examination of techniques, causes, and consequences]
3. Significance: [Exploration of the significance and implications]
4. Key Details: [Key figures, technological advancements, cultural impacts]
5. Word Count: [Total word count of the response]
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should include a detailed explanation of the event and its context.",
            "The response should examine the techniques, causes, and consequences associated with the event.",
            "The response should explore the significance and implications of the event in ancient history.",
            "The response should be at least 500 words in total.",
            "The response should include specific details such as key figures, technological advancements, and cultural impacts.",
            "The response should include a total word count."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
