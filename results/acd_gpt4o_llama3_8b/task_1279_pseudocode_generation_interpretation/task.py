class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "description": "Generate pseudocode for a function that takes an array of integers and returns the sum of all even numbers in the array.",
                "instructions": "Write the pseudocode for the described function. Ensure that the pseudocode clearly outlines the steps and logic needed to achieve the desired functionality. Your pseudocode should include variable initialization, a loop to check each number, a condition to check if the number is even, and an accumulator to sum the even numbers. Submit your pseudocode as a plain text string."
            },
            "2": {
                "pseudocode": "BEGIN\n    FUNCTION FindMax(A):\n        SET max TO A[0]\n        FOR EACH num IN A DO\n            IF num > max THEN\n                SET max TO num\n            END IF\n        END FOR\n        RETURN max\n    END FUNCTION\nEND",
                "instructions": "Interpret the provided pseudocode and describe its functionality in plain text. Explain what the function does and how it achieves its goal. Your interpretation should include an explanation of the initialization step, the loop, the condition, and the return statement. Submit your response as a plain text string."
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
                "The pseudocode should correctly implement the described functionality.",
                "The pseudocode should include variable initialization, a loop to check each number, a condition to check if the number is even, and an accumulator to sum the even numbers."]
        else:
            validation_criteria = [
                "The interpretation should accurately describe the functionality of the pseudocode.",
                "The explanation should include an explanation of the initialization step, the loop, the condition, and the return statement."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
