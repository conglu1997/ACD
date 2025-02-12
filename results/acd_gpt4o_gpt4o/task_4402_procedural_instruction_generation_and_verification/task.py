class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"task_description": "How to set up a home network with multiple devices, including a router, a modem, and three devices (e.g., a laptop, a smartphone, and a smart TV)."},
            "2": {"procedural_instructions": "1. Preheat oven to 350°F (175°C). 2. Grease and flour two 9-inch round baking pans. 3. In a large bowl, stir together the sugar, flour, cocoa, baking powder, baking soda, and salt. 4. Add the eggs, milk, oil, and vanilla, and mix for 2 minutes on medium speed of mixer. 5. Stir in the boiling water last. Batter will be thin. 6. Pour evenly into the prepared pans. 7. Bake 30 to 35 minutes in the preheated oven, until the cake tests done with a toothpick. 8. Cool in the pans for 10 minutes, then remove to a wire rack to cool completely."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "task_description" in t:
            return f"""Your task is to generate detailed procedural instructions for the following task:

{t["task_description"]}

Ensure that the instructions are clear, comprehensive, and follow a logical sequence. Include all necessary steps and any specific details required to complete the task successfully. Provide the instructions in a numbered list format."""
        elif "procedural_instructions" in t:
            return f"""Your task is to verify the correctness of the following procedural instructions:

{t["procedural_instructions"]}

Check if the instructions are clear, comprehensive, and follow a logical sequence. Identify any missing steps, errors, or ambiguities. Provide your verification and any corrections needed in plain text format with the following structure:

1. General Feedback: [Your general feedback on the instructions]
2. Corrections: [Any specific corrections or missing steps]"""
        return ""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if "task_description" in t:
            criteria = [
                "The generated instructions should be clear and comprehensive.",
                "The instructions should follow a logical sequence.",
                "All necessary steps should be included.",
                "Specific details required to complete the task should be present.",
                "The instructions should be provided in a numbered list format.",
            ]
        elif "procedural_instructions" in t:
            criteria = [
                "The verification should identify any missing steps, errors, or ambiguities.",
                "The verification should provide corrections where necessary.",
                "The response should be clear and comprehensive.",
                "The response should follow the specified structure with general feedback and corrections.",
            ]
        else:
            criteria = []
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
