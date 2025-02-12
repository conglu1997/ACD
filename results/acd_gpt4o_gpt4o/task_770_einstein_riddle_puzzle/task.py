class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "clues": [
                    "1. There are five houses in a row in different colors.",
                    "2. The Englishman lives in the red house.",
                    "3. The Spaniard owns the dog.",
                    "4. Coffee is drunk in the green house.",
                    "5. The Ukrainian drinks tea.",
                    "6. The green house is immediately to the right of the ivory house.",
                    "7. The Old Gold smoker owns snails.",
                    "8. Kools are smoked in the yellow house.",
                    "9. Milk is drunk in the middle house.",
                    "10. The Norwegian lives in the first house.",
                    "11. The man who smokes Chesterfields lives in the house next to the man with the fox.",
                    "12. Kools are smoked in the house next to the house where the horse is kept.",
                    "13. The Lucky Strike smoker drinks orange juice.",
                    "14. The Japanese smokes Parliaments.",
                    "15. The Norwegian lives next to the blue house."
                ],
                "question": "Who drinks water? Who owns the zebra?"
            },
            "2": {
                "clues": [
                    "1. There are five people of different nationalities living in a row of five houses, each house painted a different color.",
                    "2. Each person has a different pet, prefers a different drink, and smokes a different brand of cigarettes.",
                    "3. The Brit lives in the red house.",
                    "4. The Swede keeps dogs as pets.",
                    "5. The Dane drinks tea.",
                    "6. The green house is immediately to the left of the white house.",
                    "7. The owner of the green house drinks coffee.",
                    "8. The person who smokes Pall Mall rears birds.",
                    "9. The owner of the yellow house smokes Dunhill.",
                    "10. The man living in the center house drinks milk.",
                    "11. The Norwegian lives in the first house.",
                    "12. The man who smokes blends lives next to the one who keeps cats.",
                    "13. The man who keeps horses lives next to the man who smokes Dunhill.",
                    "14. The man who smokes Blue Master drinks beer.",
                    "15. The German smokes Prince.",
                    "16. The Norwegian lives next to the blue house.",
                    "17. The man who smokes blends has a neighbor who drinks water."
                ],
                "question": "Who drinks water? Who keeps the fish?"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        clues_text = '\n'.join(t['clues'])
        return f"""Your task is to solve the following logical puzzle. Use the clues provided to determine the answers to the questions.

Clues:
{clues_text}

Questions:
{t['question']}

Provide your answers in the following format:
Water: [Your answer]
Zebra/Fish: [Your answer]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        correct_answers = {
            "1": {"water": "Norwegian", "zebra": "Japanese"},
            "2": {"water": "Norwegian", "fish": "German"}
        }
        task_id = "1" if "zebra" in t['question'] else "2"
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The person who drinks water is the {correct_answers[task_id]['water']}.",
            f"The person who owns the {t['question'].split(' ')[-1].strip('?')} is the {correct_answers[task_id][t['question'].split(' ')[-1].strip('?')]}"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
