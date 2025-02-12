class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "word": "enigma",
                "definition": "A mysterious or puzzling person or thing"
            },
            "2": {
                "word": "labyrinth",
                "definition": "A complex maze or network of paths"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate a cryptic crossword clue for the given word and definition, and then solve it. Ensure that the clue includes wordplay elements such as anagrams, hidden words, homophones, or charades. Provide the clue and the explanation of the wordplay used.

Word: {t['word']}
Definition: {t['definition']}

Submit your response as a plain text string in the following format:
Clue: [Your cryptic crossword clue]
Explanation: [Your explanation of the wordplay used]

Example:
Word: cat
Definition: A small domesticated carnivorous mammal
Clue: Animal acts strangely (3)
Explanation: The word 'cat' is hidden in the phrase 'acts' (hidden word)."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The clue should be a valid cryptic crossword clue.",
            "The clue should include wordplay elements such as anagrams, hidden words, homophones, or charades.",
            "The explanation should clearly describe the wordplay used.",
            "The clue should lead to the given word as the solution."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
