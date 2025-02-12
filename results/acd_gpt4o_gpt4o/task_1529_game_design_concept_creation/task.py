class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"theme": "Medieval Fantasy", "mechanic": "Turn-based Strategy", "requirements": "Design a game concept that includes a compelling story with at least three major plot points, main characters with unique abilities, core gameplay mechanics involving resource management and tactical combat, and unique features like dynamic weather systems or player-driven economies that differentiate it from existing games in the genre."},
            "2": {"theme": "Cyberpunk", "mechanic": "Open World RPG", "requirements": "Design a game concept that includes a detailed setting with various districts, main characters with customizable cybernetic enhancements, core gameplay mechanics involving hacking and combat, and unique features like branching storylines or a reputation system that make the game stand out."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        instructions = f"""Your task is to create a detailed game design concept based on the given theme and mechanic. Ensure that your concept includes the following components:\n\nTheme: {t['theme']}\nMechanic: {t['mechanic']}\nRequirements: {t['requirements']}\n\nProvide your game design concept in the following format:\n1. Title: [Your game title]\n2. Story: [Brief description of the game's story with at least three major plot points]\n3. Main Characters: [List and description of main characters with unique abilities or customizable features]\n4. Core Gameplay Mechanics: [Detailed description of core gameplay mechanics involving the specified elements]\n5. Unique Features: [Description of unique features that differentiate the game, such as dynamic weather systems, branching storylines, or player-driven economies]\n\nEnsure that your design is coherent, creative, and meets all the specified requirements."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The game design concept should include all specified components (title, story with at least three major plot points, main characters with unique abilities or customizable features, core gameplay mechanics involving the specified elements, unique features that differentiate the game).",
            "The design should be coherent, creative, and meet the specified requirements."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
