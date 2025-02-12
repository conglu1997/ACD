class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"event": "Fall of the Roman Empire", "prompt": "Analyze the factors that contributed to the fall of the Roman Empire. Discuss the political, economic, military, and social aspects that led to its decline. Consider hypothetical scenarios where one of these factors was mitigated and discuss how it might have changed the outcome."},
            "2": {"event": "Industrial Revolution", "prompt": "Examine the impact of the Industrial Revolution on society. Discuss the technological advancements, economic changes, and social transformations that occurred during this period. Include hypothetical considerations on how a delay in one major technological advancement could have altered the course of the revolution."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        event = t["event"]
        prompt = t["prompt"]
        instructions = f"""Your task is to analyze the following historical event:

Event: {event}

{prompt}

Provide a detailed analysis that includes:
1. A comprehensive overview of the event.
2. An examination of the factors and context surrounding the event.
3. A discussion on the significance and impact of the event.
4. Consideration of hypothetical scenarios related to the event.

Ensure that your analysis is accurate, well-reasoned, and logically organized. Provide your response in plain text format, using complete sentences and paragraphs. Format your response as follows:

Analysis:
[Your detailed analysis here]"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The analysis should provide a comprehensive overview of the event.",
            "The analysis should examine the factors and context surrounding the event.",
            "The analysis should discuss the significance and impact of the event in a meaningful way.",
            "The analysis should consider hypothetical scenarios related to the event.",
            "The analysis should be well-reasoned and logically organized."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
