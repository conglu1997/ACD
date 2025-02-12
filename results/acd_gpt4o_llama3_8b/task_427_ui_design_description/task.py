class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "task_description": "Describe the layout of a user interface for an online bookstore application.",
                "instructions": "Design a user interface (UI) for an online bookstore application. Include the following components: 1. A homepage with featured books, categories, and a search bar. 2. A product page with book details, reviews, and purchase options. 3. A shopping cart page with a list of selected books, total price, and a checkout button. Describe the layout and functionality of each component in detail. Submit your description as a plain text string in the following format:\n\nHomepage:\n[Description]\n\nProduct Page:\n[Description]\n\nShopping Cart Page:\n[Description]\n"
            },
            "2": {
                "task_description": "Describe the layout of a user interface for a fitness tracking application.",
                "instructions": "Design a user interface (UI) for a fitness tracking application. Include the following components: 1. A dashboard with an overview of daily activity, workouts, and progress. 2. A workout tracking page with options to start, pause, and stop workouts, and track various metrics. 3. A profile page with user information, goals, and settings. Describe the layout and functionality of each component in detail. Submit your description as a plain text string in the following format:\n\nDashboard:\n[Description]\n\nWorkout Tracking Page:\n[Description]\n\nProfile Page:\n[Description]\n"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a user interface (UI) for the following application scenario: {t['task_description']}. Include the specified components and describe the layout and functionality of each in detail. Here are the detailed instructions:\n\n{t['instructions']}\n"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The description should be clear and logically structured.",
            "The UI components should be accurately described.",
            "The layout and functionality should be user-friendly and coherent."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
