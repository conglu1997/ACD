class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"constraints": ["Include at least three characters.", "The story must take place in a single location.", "Mention a hidden secret that is revealed at the end."]},
            "2": {"constraints": ["Include at least two characters.", "The story must revolve around a misunderstanding.", "End with an unexpected resolution."]}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        constraints = '\n'.join(t["constraints"])
        example = "\nExample:\nCharacter 1: 'I can't believe you're here!'\nCharacter 2: 'I had to come. There's something you need to know.'\nCharacter 3: 'What is it? Tell us!'"
        return f"""Write a short story that is entirely dialogue-based, adhering to the following constraints:\n\n{constraints}\n\nEnsure that the story is engaging, coherent, and follows a logical structure. Submit your story as a plain text string.{example}"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The story must be entirely dialogue-based.",
            "The story must adhere to all given constraints.",
            "The dialogue should be engaging and coherent."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
