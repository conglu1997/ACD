class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "answer": "time",
                "instructions": "Generate a riddle for the given answer: 'time'. Ensure that the riddle is creative, coherent, and logically leads to the answer 'time'. Avoid using the word 'time' or any direct synonym in the riddle. Submit your riddle as a plain text string.\nExample: 'I am not alive, but I can grow. I don't have lungs, but I need air. What am I?' (Answer: Fire)."
            },
            "2": {
                "riddle": "I am always moving but never stop. I am invisible but can be measured. I can be lost but never found. What am I?",
                "instructions": "Interpret the provided riddle and provide the correct answer. Ensure your answer is concise and directly addresses the riddle. Submit your answer as a plain text string."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return t["instructions"]

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if "answer" in t:
            validation_criteria = [
                "The riddle should logically lead to the given answer.",
                "The riddle should be creative, coherent, and avoid using the word 'time' or any direct synonym."]
        else:
            validation_criteria = [
                "The answer should be correct and match the riddle."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
