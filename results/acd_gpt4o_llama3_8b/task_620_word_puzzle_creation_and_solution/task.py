class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"type": "crossword", "words": ["apple", "banana", "cherry"]},
            "2": {"type": "riddle", "prompt": "I speak without a mouth and hear without ears. I have no body, but I come alive with wind. What am I?"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t["type"] == "crossword":
            words = ", ".join(t["words"])
            return f"""Create a simple crossword puzzle using the following words: {words}. Provide the crossword puzzle in a text format where each word has a clue and a position (e.g., Across 1, Down 2). After creating the puzzle, solve it by providing the correct answers for each clue. Submit your puzzle and solution in the following format:

Puzzle:
1. Across 1: [Clue for apple]
2. Down 1: [Clue for banana]
3. Across 2: [Clue for cherry]

Solution:
1. Across 1: apple
2. Down 1: banana
3. Across 2: cherry"""
        elif t["type"] == "riddle":
            prompt = t["prompt"]
            return f"""Read the following riddle and provide the correct answer: '{prompt}'"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t["type"] == "crossword":
            criteria = [
                "The crossword puzzle should include all the given words.",
                "Each word should have a corresponding clue and position in the specified format.",
                "The provided solution should correctly solve the puzzle."
            ]
        elif t["type"] == "riddle":
            criteria = ["The answer to the riddle should be correct."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
