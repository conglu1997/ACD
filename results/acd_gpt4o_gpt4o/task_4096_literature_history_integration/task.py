class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "historical_event": "The French Revolution",
                "literary_work": "A Tale of Two Cities by Charles Dickens"
            },
            "2": {
                "historical_event": "The American Civil War",
                "literary_work": "Gone with the Wind by Margaret Mitchell"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        historical_event = t["historical_event"]
        literary_work = t["literary_work"]
        instructions = (
            f"Your task is to analyze and draw connections between the following historical event and literary work:\n"
            f"Historical Event: {historical_event}\n"
            f"Literary Work: {literary_work}\n"
            "\nIn your analysis, address the following points:\n"
            "1. Provide a brief summary of the historical event.\n"
            "2. Provide a brief summary of the literary work.\n"
            "3. Identify and explain at least three connections between the historical event and the literary work.\n"
            "4. Discuss how the historical context influenced the themes, characters, and plot of the literary work.\n"
            "\nEnsure your analysis is well-structured, coherent, and demonstrates a deep understanding of both the historical event and the literary work."
        )
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The analysis should provide accurate summaries of both the historical event and the literary work.",
            "The analysis should identify and explain at least three connections between the historical event and the literary work.",
            "The analysis should discuss how the historical context influenced the themes, characters, and plot of the literary work.",
            "The analysis should be well-structured and coherent."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
