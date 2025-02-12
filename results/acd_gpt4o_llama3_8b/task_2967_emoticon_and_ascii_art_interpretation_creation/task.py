class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "type": "emoticon",
                "content": ":-) :-( :-P",
                "instructions": "Interpret the meaning of the following emoticons and explain the emotions they represent: :-) :-( :-P. For example, :-) typically represents happiness or a smile. Then, create three new emoticons to represent the emotions of surprise, love, and confusion. Submit your response as a plain text string in the following format: \nInterpretation: [Your interpretation of each given emoticon] \nCreation: [Your new emoticons for surprise, love, and confusion]"
            },
            "2": {
                "type": "ascii_art",
                "content": "\n  __\n /__\ \n |  |",
                "instructions": "Interpret the meaning of the following ASCII art and explain what it represents: \n  __\n /__\ \n |  |. For example, this could represent a house. Then, create a simple ASCII art representation for a tree and a house. Submit your response as a plain text string in the following format: \nInterpretation: [Your interpretation of the given ASCII art] \nCreation: [Your new ASCII art for a tree and a house]"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return t["instructions"]

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The interpretation of the emoticons or ASCII art should be clear and accurate.",
            "The created emoticons or ASCII art should appropriately represent the specified themes or emotions."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
