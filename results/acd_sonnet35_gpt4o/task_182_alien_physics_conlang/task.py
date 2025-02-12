import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "scenario": "Gravity-Wave Communication",
                "description": "Design a language for aliens who communicate through gravity waves in a high-gravity environment."
            },
            {
                "scenario": "Quantum Superposition Speech",
                "description": "Create a language for beings who exist in quantum superposition and can communicate in multiple states simultaneously."
            },
            {
                "scenario": "Photosynthetic Thought Transfer",
                "description": "Develop a language for a plant-like species that communicates through photosynthetic processes and light manipulation."
            }
        ]
        return {str(i+1): scenario for i, scenario in enumerate(random.sample(scenarios, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Create and analyze a constructed language (conlang) for an alien species based on the following scenario: {t['scenario']}. {t['description']}

Your task is to:

1. Design three key features of the language that reflect the given scenario (2-3 sentences each).

2. Provide two examples of how each feature works in practice, including both the alien 'utterance' and its English translation.

3. Explain how these language features relate to the physical laws or biological constraints of the scenario (3-4 sentences).

4. Describe how this language might handle one of the following concepts: time, negation, or quantity. Explain why this approach is suitable for the given scenario (3-4 sentences).

5. Analyze potential implications of this language on the thought patterns, culture, or technological development of its speakers (3-4 sentences).

6. Propose an experiment or study that humans could conduct to better understand or learn this alien language (2-3 sentences).

Ensure your conlang is innovative yet logically consistent with the given scenario. Be creative in your language design while grounding your explanations in scientific principles and linguistic theory. Organize your answer using clear headings for each section."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must create a language system for the scenario: {t['scenario']}",
            "The language features should be logically consistent with the given physical laws or biological constraints",
            "The response should provide specific examples for each language feature, including 'alien utterances' and English translations",
            "The analysis should consider implications on thought patterns, culture, or technological development",
            "The response should demonstrate creativity in applying scientific principles to language design",
            "The proposed experiment or study should be relevant and potentially insightful",
            "The response should be well-organized with clear headings for each section"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0