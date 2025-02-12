class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"dietary_restriction": "vegan", "base_recipe": "Spaghetti Carbonara: Spaghetti, eggs, pancetta, Parmesan cheese, black pepper."},
            "2": {"dietary_restriction": "gluten-free", "base_recipe": "Chicken Alfredo: Fettuccine, chicken breast, heavy cream, Parmesan cheese, garlic."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to modify the given base recipe to adhere to the specified dietary restriction. Ensure that the modified recipe is realistic, maintains the essence of the original dish, and adheres to the dietary restriction. Here is the information about the task:\n\nDietary Restriction: {t['dietary_restriction']}\nBase Recipe: {t['base_recipe']}\n\nSubmit your modified recipe in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [f"The modified recipe should adhere to the {t['dietary_restriction']} restriction.", "The modified recipe should be realistic and maintain the essence of the original dish."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
