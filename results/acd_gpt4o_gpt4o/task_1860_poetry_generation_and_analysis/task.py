class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "theme": "change"
            },
            "2": {
                "theme": "hope"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        instructions = f"""Your task is twofold: first, generate a poem based on the given theme, and second, provide an analysis of the poem you created. The analysis should cover the poetic devices used and the overall theme of the poem.\n\nTheme: {t['theme']}\n\nGuidelines for the Poem:\n1. The poem should be at least 12 lines long.\n2. Use at least three different poetic devices (e.g., metaphor, simile, alliteration, personification).\n3. Ensure the poem is coherent and reflects the given theme.\n\nGuidelines for the Analysis:\n1. Identify and explain the poetic devices used in the poem.\n2. Discuss how these devices contribute to the overall theme and meaning of the poem.\n3. Provide your response in plain text format.\n\nExample Response:\nPoem:\n  The winds of change blow ever strong,\n  Through fields of time, they dance along.\n  ...\n\nAnalysis:\n  The poem uses metaphor and personification. The metaphor of the winds of change suggests the inevitability and power of change. Personification gives the winds a gentle, guiding quality. Together, these devices emphasize the theme of change as a natural and guiding force in life.\n"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The poem is at least 12 lines long.",
            "At least three different poetic devices are used.",
            "The poem is coherent and reflects the given theme.",
            "The analysis correctly identifies and explains the poetic devices used.",
            "The analysis discusses how the devices contribute to the overall theme and meaning of the poem."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
