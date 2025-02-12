class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "area_description": "A coastal region with a mountain range to the east and a river flowing from north to south.",
                "constraints": ["Identify suitable locations for a port and a dam.", "Consider the impact on local wildlife and communities."]
            },
            "2": {
                "area_description": "A desert area with a small oasis in the center and a plateau to the north.",
                "constraints": ["Identify suitable locations for a solar power plant and a water reservoir.", "Consider the impact on the local climate and communities."]
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Analyze the given geographical area and provide logical reasoning for your decisions based on the following criteria and constraints:

Area Description: {t['area_description']}
Constraints:
{chr(10).join('- ' + constraint for constraint in t['constraints'])}

Your analysis should include detailed explanations of why the chosen locations are suitable, considering practical aspects such as environmental impact, accessibility, and sustainability. Submit your response as a plain text string in the following format:

Analysis: [Your detailed analysis here]

Example response format:
Analysis: The port should be located at the mouth of the river where it meets the ocean, providing easy access for ships. The dam should be built upstream to control water flow and provide a water source for the region. The impact on local wildlife should be minimized by creating protected areas and ensuring sustainable practices. The design should also consider the needs of local communities and economic factors."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The analysis should be detailed and coherent.",
            "The analysis should meet the specified area description and constraints.",
            "The chosen locations should be practical and logical.",
            "The analysis should consider environmental and community impacts.",
            "The analysis should demonstrate an understanding of geographical features and spatial relationships."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
