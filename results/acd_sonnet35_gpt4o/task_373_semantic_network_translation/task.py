import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        domains = [
            "quantum physics",
            "medieval folklore",
            "modern social media",
            "ancient Greek philosophy",
            "blockchain technology",
            "culinary arts",
            "marine biology",
            "abstract expressionism"
        ]
        concepts = [
            "uncertainty",
            "transformation",
            "connectivity",
            "balance",
            "value",
            "fusion",
            "adaptation",
            "chaos"
        ]
        return {
            "1": {
                "source_domain": random.choice(domains),
                "target_domain": random.choice(domains),
                "concept": random.choice(concepts)
            },
            "2": {
                "source_domain": random.choice(domains),
                "target_domain": random.choice(domains),
                "concept": random.choice(concepts)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a semantic network translation system to map the concept of '{t['concept']}' from the domain of {t['source_domain']} to the domain of {t['target_domain']}. Your task has the following parts:

1. Semantic Network Design (200-250 words):
   a) Create a semantic network for the concept '{t['concept']}' in the {t['source_domain']} domain.
   b) Include at least 8 nodes (including the central concept) and their relationships.
   c) Explain the rationale behind your network structure and relationships.

2. Translation Mechanism (150-200 words):
   a) Describe the process your system uses to translate semantic networks between domains.
   b) Explain how it preserves semantic relationships while adapting to the new context.
   c) Discuss how your system handles ambiguity or cultural differences.

3. Translated Semantic Network (200-250 words):
   a) Present the translated semantic network for '{t['concept']}' in the {t['target_domain']} domain.
   b) Include at least 8 nodes (including the central concept) and their relationships.
   c) Explain how each node and relationship corresponds to or differs from the original network.

4. Analysis of Translation (150-200 words):
   a) Discuss the challenges encountered in this specific translation.
   b) Analyze how the meaning of '{t['concept']}' changes or is preserved in the new domain.
   c) Identify any insights or novel connections revealed by the translation process.

5. Potential Applications (100-150 words):
   a) Propose two potential applications of your semantic network translation system.
   b) Explain how these applications could benefit from cross-domain concept mapping.

Ensure your response demonstrates a deep understanding of both domains, creative problem-solving in establishing meaningful connections, and analytical reasoning in examining the translation process and its implications.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must include a semantic network for '{t['concept']}' in the {t['source_domain']} domain with at least 8 nodes and explained relationships.",
            "The translation mechanism must be clearly described, addressing how it preserves semantic relationships and handles ambiguity.",
            f"A translated semantic network for '{t['concept']}' in the {t['target_domain']} domain must be presented with at least 8 nodes and explained relationships.",
            "The analysis should discuss challenges, meaning preservation/changes, and insights from the translation process.",
            "Two potential applications of the semantic network translation system must be proposed and explained.",
            "The response should demonstrate deep understanding of both domains, creative problem-solving, and analytical reasoning."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
