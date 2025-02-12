class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"scenario": "Two friends, Alex and Jamie, are having a conversation about their weekend plans. Alex wants to go hiking, while Jamie prefers staying home to read a book. Write a dialogue where they discuss their preferences and try to persuade each other.", "analysis_prompt": "Analyze the dialogue and explain how each character's personality and preferences are reflected in their speech."},
            "2": {"scenario": "A teacher, Mr. Smith, is talking to a student, Taylor, who has been frequently late to class. Write a dialogue where Mr. Smith addresses the issue and Taylor responds.", "analysis_prompt": "Analyze the dialogue and explain how Mr. Smith's approach and Taylor's responses reflect their respective roles and attitudes."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        instructions = f"""Your task has two parts:

Part 1: Generate a dialogue between the following characters based on the given scenario.

Scenario:
{t['scenario']}

Part 2: Analyze the generated dialogue.

Analysis Prompt:
{t['analysis_prompt']}

Your response should be structured as follows:

1. Dialogue: [Generated dialogue]
2. Analysis: [Your analysis of the dialogue]

Ensure that the dialogue is coherent, reflects the characters' personalities and preferences, and that the analysis is insightful and relevant."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The dialogue should be coherent and reflect the characters' personalities and preferences as described in the scenario.",
            "The analysis should be insightful and relevant to the dialogue."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
