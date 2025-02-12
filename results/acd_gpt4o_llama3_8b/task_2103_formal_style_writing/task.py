class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"style": "legal", "constraints": ["Include terms such as 'hereby', 'notwithstanding', and 'aforementioned'.", "The passage should describe a contractual agreement between two parties regarding the sale of goods.", "Ensure the language is precise and formal."]},
            "2": {"style": "scientific", "constraints": ["Use technical terms related to biology such as 'photosynthesis', 'chlorophyll', and 'stomata'.", "The passage should describe an experiment involving plant growth under different light conditions.", "Ensure the language is objective and methodical."]}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        style = t["style"].capitalize()
        constraints = '\n'.join(t["constraints"])
        example = "\nExample for legal style:\n'Hereby, it is agreed between the parties that the aforementioned goods shall be delivered to the buyer within 30 days.'\nExample for scientific style:\n'The experiment was conducted to study the effects of red light on chlorophyll production in plants. Photosynthesis rates were measured using a spectrophotometer.'"
        return f"""Write a passage in the {style} writing style based on the following constraints:\n\n{constraints}\n\nEnsure that the passage is coherent, follows the specified style, and meets all the given constraints. Submit your passage as a plain text string.{example}"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The passage must be written in a {t['style']} style.",
            "The passage must adhere to all given constraints.",
            "The language should be formal and precise."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
