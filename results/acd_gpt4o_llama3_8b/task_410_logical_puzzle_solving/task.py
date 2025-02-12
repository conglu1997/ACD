class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "puzzle": "There are five houses in a row, each with a different color. In each house lives a person with a different nationality. Each person drinks a different beverage, smokes a different brand of cigar, and keeps a different pet. The following clues are given:\n1. The Brit lives in the red house.\n2. The Swede keeps dogs as pets.\n3. The Dane drinks tea.\n4. The green house is immediately to the left of the white house.\n5. The green house's owner drinks coffee.\n6. The person who smokes Pall Mall rears birds.\n7. The owner of the yellow house smokes Dunhill.\n8. The man living in the center house drinks milk.\n9. The Norwegian lives in the first house.\n10. The man who smokes blends lives next to the one who keeps cats.\n11. The man who keeps horses lives next to the man who smokes Dunhill.\n12. The man who smokes Blue Master drinks beer.\n13. The German smokes Prince.\n14. The Norwegian lives next to the blue house.\n15. The man who smokes blend has a neighbor who drinks water.\nWho owns the fish?"
            },
            "2": {
                "puzzle": "In a certain town, there are three houses in a row, each painted a different color: red, blue, and green. Each house is inhabited by a person of a different profession: a teacher, a doctor, and an artist. The following clues are given:\n1. The red house is on the left of the blue house.\n2. The artist lives in the red house.\n3. The teacher lives to the right of the artist.\nWho lives in the green house?"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Solve the following logical puzzle based on the given clues:

Puzzle: {t['puzzle']}

Submit your response as a plain text string in the following format:
Answer: [Your answer]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            'The answer should be correct and based on logical deduction from the given clues.',
            'The answer should match the expected solution without any ambiguity.'
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
