class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "problem": "You need to organize a bookshelf with the following constraints: 1) Books of the same genre should be together, 2) Heavier books should be on the bottom shelf, 3) The total number of books per shelf should not exceed 10.",
                "items": [
                    {"title": "Book A", "genre": "Fiction", "weight": 1},
                    {"title": "Book B", "genre": "Non-fiction", "weight": 3},
                    {"title": "Book C", "genre": "Fiction", "weight": 2},
                    {"title": "Book D", "genre": "Non-fiction", "weight": 2},
                    {"title": "Book E", "genre": "Fiction", "weight": 3},
                    {"title": "Book F", "genre": "Non-fiction", "weight": 2},
                    {"title": "Book G", "genre": "Science", "weight": 5},
                    {"title": "Book H", "genre": "Science", "weight": 4},
                    {"title": "Book I", "genre": "Science", "weight": 2},
                    {"title": "Book J", "genre": "Fiction", "weight": 1}
                ]
            },
            "2": {
                "problem": "You need to plan a daily schedule with the following constraints: 1) At least 8 hours of sleep, 2) 1 hour of exercise, 3) 3 meals with at least 1 hour between each, 4) Finish work tasks within an 8-hour workday.",
                "items": [
                    {"task": "Sleep", "duration": 8},
                    {"task": "Exercise", "duration": 1},
                    {"task": "Breakfast", "duration": 1},
                    {"task": "Lunch", "duration": 1},
                    {"task": "Dinner", "duration": 1},
                    {"task": "Work", "duration": 8},
                    {"task": "Commute", "duration": 1},
                    {"task": "Leisure", "duration": 2}
                ]
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate a sequence of steps to solve the following problem while adhering to the specified constraints:

Problem: {t['problem']}

Items: {t['items']}

Your solution should clearly outline each step and ensure all constraints are met. Submit your response as a plain text string in the following format:

Steps:
1. [Your first step]
2. [Your second step]
..."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The solution should adhere to all specified constraints.",
            "The sequence of steps should be logically coherent."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
