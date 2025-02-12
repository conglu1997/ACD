class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "criteria": "Create a 3D shape that consists of a cube with a sphere centered inside it. The sphere should touch all six faces of the cube. Additionally, there should be a cylinder passing through the center of the cube and sphere, aligned along one of the cube's axes. The cylinder should extend beyond the cube by an equal length on both sides."
            },
            "2": {
                "criteria": "Create a 3D shape that is a cone with a cylinder intersecting it perpendicularly at its base. The cylinder should extend equally on both sides of the cone and should have a smaller radius than the base of the cone. Additionally, there should be a smaller sphere centered at the apex of the cone. The sphere's diameter should be half the radius of the cone's base."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate and describe a complex 3D shape based on the given criteria.

Criteria: {t['criteria']}

Your response should include:
1. A detailed description of the 3D shape, explaining its components and spatial relationships.
2. An explanation of how the shape meets the given criteria.
3. Ensure your description is clear and precise, using geometric terminology where appropriate.

Example response format:
- Description: The shape consists of a cube with a sphere centered inside it. The sphere has a diameter equal to the side length of the cube, so it touches all six faces of the cube. A cylinder passes through the center of the cube and sphere, aligned along one of the cube's axes. The cylinder extends beyond the cube by an equal length on both sides.
- Criteria Explanation: The shape meets the criteria as the sphere is centered inside the cube and touches all its faces. The cylinder passes through the center of both the cube and sphere, extending beyond the cube by an equal length on both sides.

Submit your response as a plain text string in the following format:
- Description: [Your description here]
- Criteria Explanation: [Your explanation here]

Make sure to follow the specified format exactly and provide a comprehensive description."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The description should accurately capture the components and spatial relationships of the 3D shape.",
            "The explanation should clearly show how the shape meets the given criteria.",
            "The response should follow the specified format precisely.",
            "The description should use appropriate geometric terminology.",
            "The explanation should be logical and thorough."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
