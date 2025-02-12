class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "scenario": "An interview with a famous scientist about their groundbreaking discovery.",
                "characters": ["Interviewer", "Scientist"],
                "required_elements": ["The interviewer must ask at least 5 questions.", "The scientist's responses must be detailed and insightful."]
            },
            "2": {
                "scenario": "A conversation between two friends planning a surprise birthday party.",
                "characters": ["Friend 1", "Friend 2"],
                "required_elements": ["The friends must discuss at least 3 different aspects of the party (e.g., location, guest list, theme).", "The conversation must be lively and collaborative."]
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate a structured conversation based on the given scenario and characters. Ensure the dialogue is coherent, engaging, and contextually appropriate. The conversation should flow naturally and incorporate all the required elements.

Scenario:
{t['scenario']}

Characters:
{', '.join(t['characters'])}

Required Elements:
{'; '.join(t['required_elements'])}"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The dialogue must be coherent and contextually appropriate.",
            "The dialogue must incorporate all the required elements.",
            "The conversation should be engaging and maintain context over multiple turns."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
