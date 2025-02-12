class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"context": "You are given a description of a three-dimensional object composed of interlocking parts. The object is a simple mechanical toy consisting of a base, a rotating gear, and a lever. The base is a rectangular block with a hole for the gear's axle. The gear is a circular disk with teeth along its edge and an axle that fits into the base. The lever is a flat bar with a notch that fits over one of the gear's teeth. When the gear rotates, the notch in the lever causes the lever to move up and down. Describe how the parts fit together and predict the movement of the lever when the gear is rotated.", "requirements": "Provide a detailed description of how the parts fit together and explain the movement of the lever when the gear is rotated. Include a step-by-step explanation of the mechanical interactions between the parts."},
            "2": {"context": "You are given a puzzle consisting of several interlocking pieces that form a three-dimensional cube when assembled. The pieces are irregularly shaped and must be placed in a specific order to fit together. Describe the steps needed to assemble the pieces into a cube, and explain how the shapes and orientations of the pieces affect the assembly process.", "requirements": "Provide a detailed description of the steps needed to assemble the pieces into a cube. Explain how the shapes and orientations of the pieces affect the assembly process, and describe any challenges that may arise during the assembly."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        context = t["context"]
        requirements = t["requirements"]
        instructions = f"""Your task is to solve the following problem based on the given context:

{context}

Ensure that your solution meets the following requirements:
{requirements}

Provide a detailed, step-by-step explanation of your solution, including all mechanical interactions, shapes, and orientations. Your response should be clear, logical, and comprehensive. Format your response as follows:

1. Problem Statement: [Brief summary of the problem]
2. Solution Approach: [Your approach to solving the problem]
3. Mechanical Interactions: [Detailed explanation of interactions between parts]
4. Conclusion: [Your final solution and reasoning]"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The solution should be logically sound and well-explained.",
            "The mechanical interactions should be correctly described.",
            "The solution should meet the specified requirements and constraints.",
            "The response should include a clear breakdown of the assembly steps and movement predictions."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
