import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_principles = [
            {
                "principle": "superposition",
                "description": "Words exist in multiple meaning states simultaneously until observed or used in context.",
                "explanation": "In quantum mechanics, superposition allows particles to exist in multiple states at once until measured."
            },
            {
                "principle": "entanglement",
                "description": "Certain words or phrases are intrinsically linked, affecting each other's meaning instantly regardless of distance in the text.",
                "explanation": "Quantum entanglement describes particles that are connected so that the quantum state of each particle cannot be described independently."
            },
            {
                "principle": "quantum tunneling",
                "description": "Words can 'tunnel' through semantic barriers, allowing for unexpected connections between seemingly unrelated concepts.",
                "explanation": "Quantum tunneling is a phenomenon where particles can pass through barriers that they classically shouldn't be able to overcome."
            },
            {
                "principle": "uncertainty principle",
                "description": "The more precisely a word's meaning is determined, the less precisely its contextual relations can be known, and vice versa.",
                "explanation": "Heisenberg's uncertainty principle states that the more precisely the position of a particle is determined, the less precisely its momentum can be known, and vice versa."
            }
        ]
        return {
            "1": random.choice(quantum_principles),
            "2": random.choice(quantum_principles)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a language system based on the quantum mechanics principle of {t['principle']}. The key characteristic of this language is: {t['description']}

Brief explanation of the quantum principle: {t['explanation']}

Your task is to:

1. Develop 3-4 key features of this quantum language system that incorporate the given principle.
2. Provide 2-3 examples for each feature, demonstrating how it would work in practice.
3. Explain how these language features relate to the quantum principle and its implications for communication.
4. Analyze the potential advantages and challenges of using this language system for information transfer and comprehension.

Format your response as follows:

Quantum Language Features:
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

Relation to Quantum Principle:
[Explain how the language features embody the quantum principle and its implications for communication]

Advantages and Challenges:
Advantages:
1. [Advantage 1]
2. [Advantage 2]
3. [Advantage 3]

Challenges:
1. [Challenge 1]
2. [Challenge 2]
3. [Challenge 3]

Ensure your quantum language system is innovative yet logically consistent with the given quantum principle. Be creative in your language design while grounding your explanations in both linguistic and quantum mechanical concepts."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response includes 3-4 well-designed language features that clearly incorporate the given quantum principle.",
            "Each feature is accompanied by 2-3 clear and relevant examples that demonstrate its practical application.",
            "The explanation of how the language features relate to the quantum principle is logically sound and demonstrates a good understanding of both linguistics and quantum mechanics.",
            "The analysis of advantages and challenges is insightful, well-structured, and considers both communicative and cognitive aspects.",
            "The quantum language system design is creative and innovative while remaining consistent with the given principle.",
            "The response demonstrates a strong ability to apply complex scientific concepts to linguistic scenarios in a meaningful way."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
