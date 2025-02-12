class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "scenario": "You are an astronaut on a mission to Mars in the year 2050. On your journey, you encounter an unexpected alien species. Describe your interactions with the aliens and how you communicate with them. Include factual information about space travel and Mars in your story.",
                "constraints": [
                    "The narrative should include at least three scientific facts about space travel or Mars.",
                    "The story should be between 300 and 500 words.",
                    "The interactions with the aliens should be detailed and imaginative."
                ]
            },
            "2": {
                "scenario": "You are a historian in the year 2150, uncovering a hidden library from the 21st century. In the library, you find a book that predicts major events from 2020 to 2150. Write a story about your discovery and the contents of the book, blending historical facts with imaginative predictions.",
                "constraints": [
                    "The narrative should include at least three historical facts from 2020 to 2150.",
                    "The story should be between 300 and 500 words.",
                    "The predictions should be imaginative but plausible."
                ]
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        instructions = f"""Your task is to write a creative story based on the following scenario:

Scenario: {t['scenario']}

Ensure that your story adheres to the following constraints:
1. {t['constraints'][0]}
2. {t['constraints'][1]}
3. {t['constraints'][2]}

Provide your story in plain text format. The story should be coherent, engaging, and adhere to the specified constraints. Format your response as follows:

Story: <Your story here>"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The story should include the required factual information.",
            "The story should be within the word limit.",
            "The interactions or predictions should be imaginative and detailed.",
            "The narrative should be coherent and engaging."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
