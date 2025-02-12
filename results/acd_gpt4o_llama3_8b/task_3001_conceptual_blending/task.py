class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "concepts": ["quantum mechanics", "ancient mythology"]
            },
            "2": {
                "concepts": ["artistic expression", "mathematical theorems"]
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        instructions = "Combine the given concepts into a coherent and creative analogy or narrative."
        concepts = t['concepts']
        instructions += f"\nConcepts: {concepts[0]} and {concepts[1]}"
        instructions += "\nYour response should blend these two domains in a way that highlights their similarities or creates an interesting story."
        instructions += "\nSubmit your response as a plain text string with the following format:"
        instructions += "\nAnalogy/Narrative: [Your analogy or narrative here]"
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The response should creatively blend the given concepts.", "The response should be coherent.", "The response should highlight similarities or create an interesting narrative."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
