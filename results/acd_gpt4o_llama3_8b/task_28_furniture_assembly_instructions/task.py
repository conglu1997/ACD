class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"item": "bookshelf", "dimensions": "height 180cm, width 80cm, depth 30cm", "parts": {"shelves": 5, "side panels": 2, "back panel": 1, "screws": 20, "brackets": 10, "screwdriver": 1}},
            "2": {"item": "table", "dimensions": "height 75cm, length 120cm, width 60cm", "parts": {"table top": 1, "legs": 4, "screws": 16, "brackets": 8, "screwdriver": 1}}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        item = t["item"]
        dimensions = t["dimensions"]
        parts = ", ".join([f"{part} ({count})" for part, count in t["parts"].items()])
        return f"""Generate step-by-step assembly instructions for a {item} with the following specifications: {dimensions}. The following parts are provided: {parts}. Ensure the instructions are clear, logically sequenced, and easy to follow. Each step should use one or more parts and be described in a single sentence. Submit your instructions as a plain text string with each step separated by a newline character."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The instructions should be clear and easy to follow.",
            "The steps should be logically sequenced.",
            "All provided parts should be mentioned and used appropriately.",
            "The final assembly should match the given dimensions.",
            "Each step should use one or more parts and be described in a single sentence."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
