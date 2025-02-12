class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "scene_description": "The park is bustling with activity. To the left, children are playing on a jungle gym, and a mother is pushing a stroller nearby. In the center, there is a large fountain surrounded by benches, where an elderly couple is sitting and feeding pigeons. To the right, a group of teenagers are playing basketball on a court. Near the fountain, a man is painting on an easel, capturing the lively scene. The sky is clear, the sun is shining brightly, and there are a few scattered clouds. A dog is running around, chasing a ball thrown by its owner. The park also has a food stand near the entrance with a small line of people waiting to buy snacks.",
                "questions": [
                    "What activities are taking place in the park?",
                    "Who is sitting near the fountain?"
                ]
            },
            "2": {
                "scene_description": "A busy kitchen during dinner preparation. A chef is chopping vegetables on the counter. To the right, another chef is stirring a pot on the stove. In the background, a waiter is arranging plates on a serving tray. There are pots and pans hanging above the stove, and a refrigerator is to the left. The kitchen is well-lit with overhead lights, and a radio is playing in the background. A clock on the wall shows 6 PM. A cat is sitting on a stool near the counter, watching the chefs work. The kitchen window offers a view of a garden outside, with a few birds visible on a tree.",
                "questions": [
                    "What is the chef on the right doing?",
                    "What time is it according to the clock?"
                ]
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""You are given a detailed description of a visual scene. Based on the description, answer the following questions:

Scene Description:
{t['scene_description']}

Questions:
1. {t['questions'][0]}
2. {t['questions'][1]}

Submit your answers as a plain text string in the following format:

Answers:
1. [Your answer to question 1]
2. [Your answer to question 2]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The answers should correctly reflect the details provided in the scene description.",
            "The answers should be concise and directly address the questions asked.",
            "The answer to 'What activities are taking place in the park?' should include at least 4 different activities.",
            "The answer to 'Who is sitting near the fountain?' should mention the elderly couple."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
