class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "puzzle": "You find yourself locked in a room with a keypad-locked door. The room contains a bookshelf, a desk, and a painting. On the desk, you find a note that says 'The key is in the numbers.' The bookshelf has 5 shelves, each labeled with different genres of books: Fiction, History, Science, Art, and Mystery. Each shelf contains a different number of books: Fiction (3), History (7), Science (5), Art (9), and Mystery (2). The painting on the wall shows a clock with the time 3:15. Use the information provided to determine the 4-digit code to unlock the door."
            },
            "2": {
                "puzzle": "You are in another room with three locked boxes, each requiring a different key. There are three clues scattered around the room: a riddle, a map, and a poem. The riddle says 'I speak without a mouth and hear without ears. I have no body, but I come alive with wind.' The map shows the room layout with an X marking a spot under the floor. The poem reads: 'To find the first key, look beneath your feet. The second key lies where the shadows meet. The third key is hidden in plain sight, where knowledge and wisdom take flight.' Determine the locations of the three keys using the clues provided."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Solve the following escape room puzzle by providing the correct solution based on the given clues. Your solution should be detailed and logically explain how you arrived at the answer. Submit your solution as a plain text string.\n\nPuzzle: {t['puzzle']}"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The solution should accurately solve the puzzle based on the given clues.",
            "The explanation should be detailed and logically structured."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
