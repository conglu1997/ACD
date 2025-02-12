import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "context": "A child's birthday party",
                "characters": ["5-year-old birthday child", "8-year-old sibling", "Parent", "Grandparent with early-stage dementia"]
            },
            {
                "context": "A job interview",
                "characters": ["Nervous applicant", "Experienced interviewer", "Company CEO observing", "Receptionist with hidden agenda"]
            }
        ]
        return {
            "1": random.choice(scenarios),
            "2": random.choice(scenarios)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to demonstrate and analyze different levels of theory of mind in a dialogue set in the context of {t['context']}. The dialogue should involve the following characters: {', '.join(t['characters'])}.

1. Generate a dialogue (300-400 words) that showcases at least three different levels of theory of mind among the characters. Ensure that each character's dialogue reflects their unique perspective and ability to understand others' mental states.

2. After the dialogue, provide a brief analysis (200-250 words) of each character's demonstrated level of theory of mind. Consider the following aspects:
   a) How well does each character understand and respond to others' thoughts, beliefs, and intentions?
   b) Are there any misunderstandings or conflicts arising from differences in theory of mind abilities?
   c) How do the characters' theory of mind levels affect their interactions and the overall situation?

3. Propose a creative extension or variation of this scenario (100-150 words) that would further challenge or highlight differences in theory of mind abilities among the characters.

Ensure your response demonstrates a deep understanding of theory of mind concepts, linguistic nuances, and social cognition. Be creative in your dialogue construction while maintaining psychological plausibility."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The dialogue effectively demonstrates at least three different levels of theory of mind among the characters.",
            "Each character's dialogue accurately reflects their unique perspective and ability to understand others' mental states.",
            "The analysis provides insightful observations about each character's demonstrated level of theory of mind.",
            "The proposed extension or variation creatively challenges or highlights differences in theory of mind abilities.",
            "The overall response shows a deep understanding of theory of mind concepts, linguistic nuances, and social cognition."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
