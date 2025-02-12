class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"environmental_change": "introduction of an invasive species"},
            "2": {"environmental_change": "drastic temperature increase"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        environmental_change = t["environmental_change"]
        return f"""Design a fictional ecosystem, describing various species and their interactions. Once the ecosystem is designed, analyze the impact of the following environmental change: {environmental_change}. Your response should include:
1. A detailed description of the ecosystem, including various species and their roles.
2. The interactions between the species and their environment.
3. An analysis of how the specified environmental change will impact the ecosystem, including potential short-term and long-term effects.
4. Possible adaptations or changes that species might undergo in response to the environmental change.

Ensure that your ecosystem is coherent, the interactions are logical, and the analysis is thorough. Submit your response as a plain text string in the following format:

Ecosystem Description: [Your ecosystem description]
Species Interactions: [Description of interactions]
Impact Analysis: [Analysis of the impact]
Adaptations: [Possible adaptations or changes]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The ecosystem should be well-developed and coherent.",
            "The species and their roles should be clearly described.",
            "The interactions between species and their environment should be logical.",
            "The impact analysis should be thorough and consider both short-term and long-term effects.",
            "The possible adaptations or changes should be plausible.",
            "The response should follow the specified format."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
