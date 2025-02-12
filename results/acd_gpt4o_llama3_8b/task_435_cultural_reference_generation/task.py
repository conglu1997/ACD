class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"prompt": "Write a paragraph that describes a festive event in a small town, incorporating references to local folklore and traditional celebrations from any culture of your choice."},
            "2": {"prompt": "Create a short story that includes references to famous historical events and figures from any two different cultures."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Generate a response based on the following prompt: {t['prompt']}\nEnsure that your response includes relevant cultural references and is contextually appropriate. Format your response as a coherent paragraph or short story."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The response should include relevant and contextually appropriate cultural references.", "The references should be accurate and integrated smoothly into the text.", "The response should be coherent and follow the format of a paragraph or short story."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
