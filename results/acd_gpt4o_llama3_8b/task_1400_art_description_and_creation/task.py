class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "description": "A serene landscape painting featuring a calm lake surrounded by lush green trees. The sky is clear with a few fluffy white clouds. A small wooden boat is gently floating on the lake, and in the background, there are distant mountains with snow-capped peaks.",
                "theme": "transformation into a night scene"
            },
            "2": {
                "description": "A lively cityscape with tall skyscrapers, bustling streets, and colorful street markets. The sun is setting, casting a warm golden glow over the buildings. People are walking, shopping, and interacting with street vendors. There are cars, buses, and bicycles moving through the streets.",
                "theme": "transformation into a winter wonderland"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Interpret the following description of a piece of visual art: \"{t['description']}\". Based on this description, generate a new detailed description that transforms the scene according to the specified theme: \"{t['theme']}\". Ensure that your new description is vivid, coherent, and accurately reflects the transformation theme. Submit your response as a plain text string."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should be a detailed and vivid description.",
            f"The response should accurately reflect the transformation theme: {t['theme']}.",
            "The response should be coherent and logically structured."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
