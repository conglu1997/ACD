class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"puzzle": "Three people (Alice, Bob, and Carol) are sitting in a row. Alice is to the left of Bob. Bob is to the left of Carol. Who is in the middle?"},
            "2": {"constraints": "Create a logic puzzle involving four people (David, Emma, Frank, and Grace) and their favorite colors (red, blue, green, yellow). The puzzle should involve seating arrangements and color preferences."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "puzzle" in t:
            return f"Your task is to solve the following logic puzzle:\n\n{t['puzzle']}\n\nProvide your answer in plain text format. Your response should be concise and directly answer the question posed by the puzzle."
        elif "constraints" in t:
            return f"Your task is to create a logic puzzle based on the following constraints:\n\n{t['constraints']}\n\nEnsure that the puzzle is coherent, challenging, and solvable. Provide the puzzle in plain text format, including any necessary clues and the solution. Your response should include a clear statement of the puzzle, followed by the clues, and finally the solution."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if "puzzle" in t:
            criteria = [
                "The answer should correctly identify who is in the middle.",
                "The response should be concise and directly answer the question posed by the puzzle."]
        elif "constraints" in t:
            criteria = [
                "The puzzle should involve four people and their favorite colors.",
                "The puzzle should involve seating arrangements and color preferences.",
                "The puzzle should be coherent and solvable.",
                "The response should include a clear statement of the puzzle, followed by the clues, and finally the solution."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0