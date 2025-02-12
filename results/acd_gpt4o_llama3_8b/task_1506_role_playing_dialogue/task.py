class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"character": "a wise old wizard", "context": "You are a young apprentice seeking advice on how to control powerful magic.", "starting_line": "Greetings, wise one. I seek your counsel on mastering the arcane arts."},
            "2": {"character": "a seasoned detective", "context": "You are a rookie detective looking for guidance on solving a complex murder case.", "starting_line": "Detective, I need your help to crack this case. The clues just don't add up."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        character = t["character"]
        context = t["context"]
        starting_line = t["starting_line"]
        return f"""Engage in a role-playing dialogue with the following character and context. Respond in a manner that is coherent, contextually appropriate, and consistent with the character's persona. Begin your response with the given starting line and continue the conversation logically.

Character: {character}
Context: {context}
Starting Line: {starting_line}

Submit your response as a plain text string in the following format:

[Starting Line]
[Your Response]

Ensure that the dialogue is engaging, coherent, and maintains the character's persona throughout."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should be coherent and contextually appropriate.",
            "The dialogue should maintain the character's persona throughout.",
            "The conversation should logically follow from the starting line.",
            "The dialogue should be engaging and demonstrate creativity."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
