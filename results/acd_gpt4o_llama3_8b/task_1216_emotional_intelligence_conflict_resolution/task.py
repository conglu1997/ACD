class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "conflict": "Two colleagues, John and Sarah, have a disagreement at work. John feels that Sarah is not contributing equally to a team project, while Sarah feels that John is being overly critical and not acknowledging her efforts. Resolve this conflict by understanding both perspectives, empathizing with each person, and proposing a solution that addresses both their concerns.",
                "context": "Workplace conflict between colleagues"
            },
            "2": {
                "conflict": "A couple, Alex and Jamie, are arguing about how to spend their weekend. Alex prefers to stay at home and relax, while Jamie wants to go out and explore new places. Resolve this conflict by understanding both preferences, empathizing with each person, and proposing a solution that satisfies both their needs.",
                "context": "Personal conflict between partners"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""You are required to resolve an interpersonal conflict based on the following details:

Context: {t['context']}

Conflict: {t['conflict']}

Respond to the conflict by demonstrating your understanding of each person's perspective, empathizing with their feelings, and proposing a solution that addresses both their concerns. Your response should be coherent, contextually appropriate, and maintain a respectful tone throughout the interaction. Submit your response as a plain text string with the following format:

1. Understanding: [Your understanding of each person's perspective here]
2. Empathy: [Your empathetic response to each person's feelings here]
3. Solution: [Your proposed solution here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The response should demonstrate understanding of each person's perspective.",
            "The response should show empathy towards each person's feelings.",
            "The response should propose a viable solution that addresses both concerns.",
            "The response should be coherent and contextually appropriate."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
