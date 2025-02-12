class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "elements": ["a haunted house", "a lost treasure", "a family secret"],
                "constraints": ["must include a twist ending", "should be set in the 19th century", "main character is an archaeologist"]
            },
            "2": {
                "elements": ["a futuristic city", "a forbidden love", "a rebellion"],
                "constraints": ["must include a betrayal", "should be set in an alien world", "main character is a rebel leader"]
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        instructions = f"""Your task is to create a compelling story plot based on the following elements and constraints.

Elements: {', '.join(t['elements'])}

Constraints: {', '.join(t['constraints'])}

Your story plot should be coherent, engaging, and follow a logical narrative structure. Ensure that you incorporate all the given elements and adhere to the constraints. Provide your response in plain text format, structured as follows:

1. Setting
2. Main Characters
3. Plot Overview
4. Key Events
5. Twist Ending (if applicable)

The twist ending for Task 1 should be surprising and change the direction of the story significantly. The betrayal in Task 2 should be a significant event that impacts the main character and the overall plot."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The story plot should include all the given elements.",
            "The story plot should adhere to the constraints.",
            "The narrative should be coherent and engaging.",
            "The structure should include Setting, Main Characters, Plot Overview, Key Events, and Twist Ending (if applicable).",
            "For Task 1, the plot must include a twist ending that changes the direction of the story significantly.",
            "For Task 2, the plot must include a significant betrayal that impacts the main character and the overall plot."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
