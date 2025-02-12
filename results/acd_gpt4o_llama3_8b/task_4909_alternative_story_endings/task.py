class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"book_title": "Romeo and Juliet", "original_ending": "Romeo and Juliet both die due to a series of tragic misunderstandings.", "main_characters": "Romeo, Juliet, Friar Laurence, the Nurse, Tybalt, Mercutio", "context": "The story is set in Verona, where the Montagues and Capulets are feuding families."},
            "2": {"book_title": "1984", "original_ending": "Winston is broken by the Party and betrays Julia, ultimately accepting Big Brother.", "main_characters": "Winston Smith, Julia, O'Brien, Big Brother", "context": "The story is set in a dystopian future where the Party exerts total control over society."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        book_title = t["book_title"]
        original_ending = t["original_ending"]
        main_characters = t["main_characters"]
        context = t["context"]
        return f"""Generate an alternative ending for the following famous story or book:

Book Title: {book_title}

Original Ending: {original_ending}

Main Characters: {main_characters}

Context: {context}

Your alternative ending should maintain the integrity of the main characters and be coherent with the original narrative. Submit your alternative ending as a plain text string in the following format:

Alternative Ending: [Your alternative ending here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The alternative ending should maintain the integrity of the main characters.", "The alternative ending should be coherent with the original narrative."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
