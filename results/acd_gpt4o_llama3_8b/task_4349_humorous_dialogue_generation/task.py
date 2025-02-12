class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "scenario": "An astronaut and an alien meet on a distant planet and have a conversation about Earth food.",
                "characters": ["Astronaut", "Alien"]
            },
            "2": {
                "scenario": "A detective interviews a suspect who has a peculiar alibi involving a time machine.",
                "characters": ["Detective", "Suspect"]
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate a humorous dialogue based on the following scenario and characters:

Scenario: {t['scenario']}
Characters: {', '.join(t['characters'])}

Your dialogue should be:
1. Humorous and engaging.
2. Contextually appropriate to the given scenario and characters.
3. Coherent and logically structured.

Submit your dialogue as a plain text string in the following format:

Character 1: [Dialogue line]
Character 2: [Dialogue line]
...
Character N: [Dialogue line]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The dialogue should be humorous.",
            "The dialogue should be contextually appropriate to the given scenario and characters.",
            "The dialogue should be coherent and logically structured."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0