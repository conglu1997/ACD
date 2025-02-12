import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        concepts = [
            "perseverance",
            "innovation",
            "harmony",
            "wisdom",
            "adaptability",
            "resilience"
        ]
        cultures = [
            "Japanese",
            "Nigerian",
            "Brazilian",
            "Indian",
            "Canadian",
            "Egyptian"
        ]
        return {
            "1": {
                "concept": random.choice(concepts),
                "culture1": random.choice(cultures),
                "culture2": random.choice([c for c in cultures if c != "culture1"])
            },
            "2": {
                "concept": random.choice(concepts),
                "culture1": random.choice(cultures),
                "culture2": random.choice([c for c in cultures if c != "culture1"])
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Create novel idiomatic expressions for the concept of {t['concept']} in {t['culture1']} and {t['culture2']} cultures, then analyze their potential adoption and impact. Your response should include:

1. Idiomatic Expression Creation (200-250 words):
   a) Create a new idiomatic expression for {t['concept']} in {t['culture1']} culture.
   b) Create a new idiomatic expression for {t['concept']} in {t['culture2']} culture.
   c) Explain the cultural elements and reasoning behind each expression.
   d) Provide a literal translation and the intended meaning for each expression.

2. Cultural Context Analysis (200-250 words):
   a) Analyze how each expression aligns with the values and communication styles of its respective culture.
   b) Discuss any cultural sensitivities or potential misunderstandings that could arise from these expressions.
   c) Compare and contrast the two expressions, highlighting cultural differences in approaching the concept.

3. Linguistic Analysis (150-200 words):
   a) Examine the linguistic features (e.g., metaphors, syntax, phonetic qualities) of each expression.
   b) Explain how these features contribute to the expression's memorability and effectiveness.
   c) Discuss any challenges in translating these idioms to other languages.

4. Potential Adoption and Impact (200-250 words):
   a) Predict the likelihood of each expression being adopted within its culture and explain your reasoning.
   b) Discuss potential positive and negative impacts of these new expressions on cultural communication.
   c) Analyze how these expressions might evolve or be misused over time.

5. Cross-Cultural Communication (150-200 words):
   a) Propose a strategy for introducing these new idioms to people from different cultures.
   b) Discuss the potential of these expressions to bridge cultural understanding.
   c) Address any ethical considerations in creating and promoting new cultural expressions.

Ensure your response demonstrates deep understanding of both cultures, linguistic creativity, and analytical reasoning. Use appropriate cultural references and linguistic terminology. Be innovative while maintaining cultural sensitivity and plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 900-1150 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response creates novel and culturally appropriate idiomatic expressions for {t['concept']} in both {t['culture1']} and {t['culture2']} cultures.",
            "The cultural context analysis demonstrates a deep understanding of both cultures and their values.",
            "The linguistic analysis shows a strong grasp of language features and their impact on expression effectiveness.",
            "The adoption and impact analysis provides insightful predictions and considers multiple factors.",
            "The cross-cultural communication strategy is well-thought-out and addresses potential challenges.",
            "The response demonstrates linguistic creativity, cultural sensitivity, and analytical reasoning throughout.",
            "The response follows the specified format and adheres to the word limit guidelines."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
