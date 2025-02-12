import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "scenario": "a universe where time flows non-linearly",
                "focus": "verb tenses and temporal expressions"
            },
            {
                "scenario": "a civilization living on a planet with extreme gravitational fluctuations",
                "focus": "spatial prepositions and motion verbs"
            }
        ]
        return {
            "1": random.choice(scenarios),
            "2": random.choice(scenarios)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Create a constructed language (conlang) for {t['scenario']}, focusing particularly on {t['focus']}. Your task is to:

1. Design key features of the language that reflect the given scenario (3-4 features).
2. Provide examples of how these features work in practice (2-3 examples per feature).
3. Explain how these language features relate to the physical or scientific principles of the scenario.
4. Analyze potential implications of this language on the thought patterns or cultural development of its speakers.

Format your response as follows:

Language Features:
1. [Feature 1]: [Explanation]
   Examples:
   a. [Example 1]
   b. [Example 2]
2. [Feature 2]: [Explanation]
   Examples:
   a. [Example 1]
   b. [Example 2]
3. [Feature 3]: [Explanation]
   Examples:
   a. [Example 1]
   b. [Example 2]

Relation to Scenario:
[Explain how the language features reflect the physical or scientific principles of the scenario]

Implications:
[Analyze potential implications on thought patterns or cultural development]

Ensure your conlang is innovative yet logically consistent with the given scenario. Be creative in your language design while grounding your explanations in scientific and linguistic principles."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response includes 3-4 well-designed language features that clearly reflect the given scenario.",
            "Each feature is accompanied by 2-3 clear and relevant examples.",
            "The explanation of how the language features relate to the scenario's principles is logical and well-reasoned.",
            "The analysis of potential implications is insightful and considers both cognitive and cultural aspects.",
            "The conlang design is creative and innovative while remaining consistent with the scenario.",
            "The response demonstrates a strong understanding of both linguistic principles and the scientific concepts involved in the scenario."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
