class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "description": "Translate the following natural language statement into a formal logic expression: 'If it is raining, then the ground is wet.'",
                "instructions": "Write the formal logic expression for the given statement. Use standard logical notation, including symbols for implication (→), conjunction (∧), disjunction (∨), negation (¬), and variables to represent the statements. For this task, use 'R' to represent 'It is raining' and 'W' to represent 'The ground is wet'. Submit your formal logic expression as a plain text string in the following format: [Your formal logic expression]."
            },
            "2": {
                "formal_logic": "(P ∧ Q) → R",
                "instructions": "Interpret the provided formal logic expression and describe its meaning in natural language. Explain what the expression means, including the roles of each variable and the overall logical structure. For this task, use the following interpretations: 'P' represents 'It is sunny', 'Q' represents 'It is a weekend', and 'R' represents 'I will go to the beach'. Submit your response as a plain text string in the following format: [Your interpretation]."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return t["instructions"]

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if "description" in t:
            validation_criteria = [
                "The formal logic expression should correctly represent the natural language statement.",
                "The expression should use standard logical notation and accurately reflect the logical relationship described in the statement."]
        else:
            validation_criteria = [
                "The interpretation should accurately describe the meaning of the formal logic expression.",
                "The explanation should include an interpretation of each variable and the overall logical structure."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
