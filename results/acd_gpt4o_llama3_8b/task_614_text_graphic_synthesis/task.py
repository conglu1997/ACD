class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "text": "The diagram shows a decision-making process for troubleshooting a computer that won't turn on. The steps are: 1) Check if the power cable is plugged in. 2) Check if the power button is working. 3) Check if the power supply unit is functioning. 4) If all steps fail, call technical support.",
                "diagram": "(Start) --> [Check Power Cable] --[Yes]--> [Check Power Button] --[Yes]--> [Check Power Supply] --[Yes]--> (Call Support)\n (No) <-- [Check Power Cable] <-- (End)"
            },
            "2": {
                "text": "The diagram shows a Venn diagram of the overlap between different programming languages used for web development. Circle A represents languages used for front-end development, Circle B represents languages used for back-end development, and the intersection represents languages that can be used for both.",
                "diagram": "(Front-End: HTML, CSS, JavaScript)\n (Both: JavaScript)\n (Back-End: Python, Ruby, PHP)"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Interpret the following textual and graphical data to generate a coherent summary or explanation:\n\nText: {t['text']}\n\nDiagram: {t['diagram']}\n\nEnsure your response integrates both the text and the diagram in a meaningful way. Submit your response as a plain text string with the following sections:\n\n1. Text Interpretation: [Your interpretation of the text]\n2. Diagram Interpretation: [Your interpretation of the diagram]\n3. Combined Summary: [A coherent summary that integrates both the text and the diagram]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = ["The response should include separate sections for text interpretation, diagram interpretation, and combined summary.", "The response should accurately interpret both the text and the diagram.", "The combined summary should meaningfully integrate information from both sources.", "The response should be coherent and logical."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
