class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"prompt": "Write a journal entry from the perspective of Leonardo da Vinci describing a day in his life while working on the Mona Lisa. Ensure the entry reflects the historical context and includes his thoughts and feelings about the painting. The journal entry should be between 300 to 500 words."},
            "2": {"prompt": "Write a letter from the perspective of Marie Curie to her husband Pierre Curie, describing her discoveries in radioactivity and her hopes for their scientific work. Ensure the letter reflects the historical context and includes her thoughts and feelings about their research. The letter should be between 300 to 500 words."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Generate a historically accurate and engaging piece of writing based on the following prompt: '{t['prompt']}'. Ensure that the writing reflects the historical context and includes the thoughts and feelings of the historical figure. Submit your writing as a plain text string in the format of a journal entry or letter, and ensure it is between 300 to 500 words."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The writing should be historically accurate and engaging.", "The perspective of the historical figure should be clearly conveyed.", "The thoughts and feelings of the historical figure should be included.", "The length should be between 300 to 500 words."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
