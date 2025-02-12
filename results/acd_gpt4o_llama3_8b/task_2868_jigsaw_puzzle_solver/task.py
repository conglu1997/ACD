class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "pieces": [
                    {"id": 1, "shape": "corner", "connections": {"right": 2, "bottom": 3}},
                    {"id": 2, "shape": "edge", "connections": {"left": 1, "bottom": 4}},
                    {"id": 3, "shape": "edge", "connections": {"top": 1, "right": 4}},
                    {"id": 4, "shape": "center", "connections": {"left": 3, "top": 2}}
                ],
                "goal": "Complete the 2x2 jigsaw puzzle."
            },
            "2": {
                "pieces": [
                    {"id": 1, "shape": "corner", "connections": {"right": 2, "bottom": 4}},
                    {"id": 2, "shape": "edge", "connections": {"left": 1, "bottom": 3}},
                    {"id": 3, "shape": "edge", "connections": {"top": 2, "left": 4}},
                    {"id": 4, "shape": "center", "connections": {"right": 3, "top": 1}}
                ],
                "goal": "Complete the 2x2 jigsaw puzzle."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        pieces_description = "\n".join([f"Piece {p['id']} (Shape: {p['shape']}, Connections: {p['connections']})" for p in t['pieces']])
        return f"""You are given a set of jigsaw puzzle pieces with their shapes and connections described. Your task is to provide the correct sequence of moves to assemble the pieces into a complete 2x2 jigsaw puzzle. Describe each move in the format 'Place Piece X at position (row, column)'.\n\nPieces:\n{pieces_description}\n\nGoal: {t['goal']}\n\nResponse Format:\nMoves: [Provide the sequence of moves to assemble the puzzle. For example, 'Place Piece 1 at position (0, 0)', 'Place Piece 2 at position (0, 1)', 'Place Piece 3 at position (1, 0)', 'Place Piece 4 at position (1, 1)'.]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The sequence of moves should correctly assemble the jigsaw puzzle as described.", "The moves should be logically sequenced and accurate."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
