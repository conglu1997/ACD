class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "scenario": "A formal business meeting in Japan where the participants are discussing a new partnership. One participant is a senior executive who places high importance on respect and formality.",
                "cultural_context": "Japanese business etiquette"
            },
            "2": {
                "scenario": "A casual family dinner in Italy discussing plans for a summer vacation. The family includes members of different generations with varying opinions.",
                "cultural_context": "Italian family dynamics"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate a dialogue based on the following scenario and cultural context. Ensure that the dialogue reflects the cultural norms, behaviors, and context provided. The dialogue should be coherent, culturally appropriate, and relevant to the scenario. Your response should be between 150 and 300 words.

Scenario: {t['scenario']}
Cultural Context: {t['cultural_context']}

Submit your dialogue as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The dialogue should be coherent and relevant to the scenario.",
            "The dialogue should reflect the cultural norms and behaviors specified.",
            "The dialogue should include contextually appropriate interactions between participants.",
            "The response should be between 150 and 300 words."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
