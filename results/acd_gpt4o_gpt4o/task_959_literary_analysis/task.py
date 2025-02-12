class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"text": "'It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way - in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only.' - Charles Dickens, A Tale of Two Cities"},
            "2": {"text": "'All animals are equal, but some animals are more equal than others.' - George Orwell, Animal Farm"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to read the following passage and provide a detailed literary analysis. Identify the main themes, literary devices, and the overall message of the text. Provide insights into how the passage reflects the broader context of the work or the author's intent. Be sure to support your analysis with specific references to the text.\n\nText:\n\n{t["text"]}\n\nFormat your response as follows:\n\n- Main Themes: [Identified themes]\n- Literary Devices: [Identified literary devices]\n- Overall Message: [Overall message of the text]\n- Context and Author's Intent: [Insights into the broader context or author's intent]\n- Text References: [Specific references to the text to support your analysis]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The analysis should identify the main themes of the text.",
            "The analysis should reference specific parts of the text to support claims.",
            "The analysis should provide insights into the broader context of the work or the author's intent.",
            "The analysis should be clear, logical, and well-structured."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
