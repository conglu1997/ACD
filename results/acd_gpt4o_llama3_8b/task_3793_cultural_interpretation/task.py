class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "artifact": "The Japanese tea ceremony (茶道, sadō) is a traditional ritual influenced by Zen Buddhism, involving the ceremonial preparation and consumption of matcha (powdered green tea)."
            },
            "2": {
                "artifact": "The Dreamtime (or Dreaming) is a central concept in Aboriginal Australian culture, referring to the time of creation when ancestral beings shaped the world and established laws and customs."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Interpret and explain the significance of the following cultural artifact:

Artifact: {t['artifact']}

Your response should include:
1. A detailed description of the artifact and its cultural context.
2. The historical and cultural significance of the artifact within its culture.
3. Any symbolic meanings or values associated with the artifact.
4. The impact of the artifact on contemporary society or its lasting legacy.

Ensure that your response is thorough, well-researched, and demonstrates a deep understanding of the cultural context. Submit your response as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The response should include a detailed description of the artifact and its cultural context.",
            "The response should explain the historical and cultural significance of the artifact.",
            "The response should identify any symbolic meanings or values associated with the artifact.",
            "The response should discuss the impact of the artifact on contemporary society or its lasting legacy."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
