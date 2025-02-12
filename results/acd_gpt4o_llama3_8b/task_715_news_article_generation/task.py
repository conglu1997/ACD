class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "headline": "Breakthrough in Renewable Energy Technology",
                "key_points": [
                    "A new solar panel technology has been developed.",
                    "The technology increases efficiency by 20%.",
                    "It is expected to reduce the cost of solar energy significantly.",
                    "Experts believe it could accelerate the transition to renewable energy sources."]
            },
            "2": {
                "headline": "Historic Peace Agreement Signed",
                "key_points": [
                    "Leaders of two warring countries have signed a peace agreement.",
                    "The agreement ends a decade-long conflict.",
                    "It includes provisions for disarmament and economic cooperation.",
                    "International organizations have praised the agreement as a major step towards global peace."]
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate a news article based on the following headline and key points:

Headline: {t['headline']}
Key Points:
- {t['key_points'][0]}
- {t['key_points'][1]}
- {t['key_points'][2]}
- {t['key_points'][3]}

Ensure your article is at least 300 words long, follows journalistic standards, and includes an engaging introduction, body, and conclusion. The article should be coherent, factual, well-structured, and include quotes from experts or sources. Integrate the quotes naturally into the narrative. Submit your article as a plain text string. Make sure the article covers all the key points provided in a coherent manner."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The article should be at least 300 words long.",
            "The article should include an engaging introduction, body, and conclusion.",
            "The article should cover all key points provided in a coherent manner.",
            "The article should be coherent, factual, and well-structured.",
            "The article should include quotes from experts or sources integrated naturally into the narrative."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
