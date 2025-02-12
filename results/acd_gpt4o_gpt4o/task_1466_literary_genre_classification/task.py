class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"excerpt": "The spaceship landed on the desolate planet, its crew ready to explore the unknown terrains and face the unexpected challenges that awaited them."},
            "2": {"excerpt": "Detective Holmes inspected the crime scene meticulously, searching for the slightest clue that could unravel the mystery behind the sudden disappearance of the famous artist."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return "Classify the following text excerpt into its correct literary genre. The genres to consider are: Science Fiction, Mystery, Fantasy, Romance, and Historical Fiction. Here is the excerpt: '" + t["excerpt"] + "'. Provide your answer as the genre name only, e.g., 'Science Fiction'."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        task_id = None
        for key, value in TaskFamily.get_tasks().items():
            if value["excerpt"] == t["excerpt"]:
                task_id = key
                break
        correct_genres = {"1": "Science Fiction", "2": "Mystery"}
        criteria = [f"The response should classify the text into the correct literary genre, which is {correct_genres[task_id]}."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
