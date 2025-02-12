import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "objects": ["red cube", "blue sphere", "green cylinder", "yellow pyramid", "orange cone"],
                "relationships": [
                    "The red cube is to the left of the blue sphere.",
                    "The green cylinder is behind the blue sphere.",
                    "The yellow pyramid is in front of the red cube.",
                    "The orange cone is to the right of the blue sphere.",
                    "The green cylinder is above the orange cone."
                ],
                "question": "If you were to draw a straight line from the yellow pyramid to the green cylinder, which objects would this line pass through or touch?"
            },
            {
                "objects": ["silver ring", "golden watch", "bronze medal", "platinum necklace", "copper bracelet", "diamond earring"],
                "relationships": [
                    "The golden watch is above the silver ring.",
                    "The bronze medal is to the left of the silver ring.",
                    "The platinum necklace is below the golden watch.",
                    "The copper bracelet is to the right of the silver ring.",
                    "The diamond earring is between the bronze medal and the copper bracelet, but closer to the bronze medal.",
                    "The platinum necklace is directly below the diamond earring."
                ],
                "question": "If you were to rotate the entire configuration 90 degrees clockwise, what would be the new position of the platinum necklace relative to the other objects?"
            },
            {
                "objects": ["black book", "white paper", "brown desk", "gray laptop", "purple pen"],
                "relationships": [
                    "The black book is on top of the brown desk.",
                    "The white paper is partially underneath the black book.",
                    "The gray laptop is to the right of the black book on the brown desk.",
                    "The purple pen is lying diagonally across the white paper.",
                    "The brown desk has a drawer that is slightly open beneath the gray laptop."
                ],
                "question": "If you were to quickly slide the white paper out from under the black book, which objects would move and how?"
            }
        ]
        return {str(i+1): scenario for i, scenario in enumerate(random.sample(scenarios, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""You have 3 minutes to complete this task. Based on the following descriptions of spatial relationships, create a mental model of the scene:

{chr(10).join(t['relationships'])}

Using your mental model, answer the following question:

{t['question']}

Your response should include:

1. A step-by-step explanation of how you constructed your mental model (200-250 words).
2. A clear answer to the question, with detailed reasoning based on your mental model (150-200 words).
3. A description of any challenges or ambiguities you encountered while creating the mental model or answering the question (100-150 words).
4. A textual representation or diagram of your final mental model (describe it in words if you can't create an actual diagram).
5. An analysis of potential errors in your mental model and how they might affect your answer (100-150 words).
6. An estimation of how confident you are in your answer on a scale of 1-10, with a brief explanation of your confidence level (50-75 words).

Ensure your response demonstrates clear spatial reasoning and logical deduction based solely on the given information. Remember, you only have 3 minutes to complete this task, so manage your time wisely."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response includes a clear and logical step-by-step explanation of mental model construction",
            "The answer to the question is provided with detailed and accurate reasoning based on the mental model",
            "Challenges or ambiguities in the process are thoroughly discussed",
            "A comprehensive textual representation or diagram of the final mental model is included",
            "The response demonstrates advanced spatial reasoning and logical deduction skills",
            "The answer is entirely consistent with the given spatial relationships",
            "A thoughtful analysis of potential errors in the mental model is provided",
            "A well-justified confidence estimation is provided",
            "The response adheres to the specified word counts for each section",
            "The overall response is coherent, well-structured, and demonstrates a high level of linguistic and cognitive competence"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
