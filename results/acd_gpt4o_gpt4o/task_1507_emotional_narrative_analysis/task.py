class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"passage": "John walked into the room, his shoulders slumped and eyes downcast. He barely acknowledged his friends, who were chatting animatedly in the corner. He went straight to the window and stared out, lost in thought."},
            "2": {"passage": "Sarah received the letter with trembling hands. Her eyes scanned the words quickly, and a smile slowly spread across her face. She clutched the letter to her chest and ran to find her brother, laughing with joy."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to interpret the emotions and motivations of the main character in the following narrative passage. Provide a detailed explanation of what the character might be feeling and why, based on the context provided. Your response should demonstrate a deep understanding of the character's emotional state and motivations.

Narrative Passage: {t['passage']}

Your interpretation should be between 150 and 300 words long."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The interpretation should demonstrate a deep understanding of the character's emotional state.",
            "The explanation should be clear, coherent, and well-structured.",
            "The response should be between 150 and 300 words long."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
