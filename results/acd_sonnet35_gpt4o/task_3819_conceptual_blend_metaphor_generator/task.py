import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        domains = [
            "Music", "Architecture", "Biology", "Economics",
            "Astronomy", "Cuisine", "Technology", "Sports"
        ]
        concepts = [
            "Harmony", "Structure", "Growth", "Exchange",
            "Expansion", "Fusion", "Innovation", "Competition"
        ]
        return {
            "1": {
                "domain1": random.choice(domains),
                "domain2": random.choice(domains),
                "concept": random.choice(concepts)
            },
            "2": {
                "domain1": random.choice(domains),
                "domain2": random.choice(domains),
                "concept": random.choice(concepts)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a system that generates novel conceptual blends and metaphors based on the input domains of {t['domain1']} and {t['domain2']}, exploring the concept of {t['concept']}. Your response should include:

1. System Architecture (250-300 words):
   a) Describe the key components of your conceptual blend and metaphor generation system.
   b) Explain how your system integrates knowledge from cognitive linguistics and artificial intelligence.
   c) Detail the mechanisms used to create novel blends and metaphors from the given domains.
   d) Include a high-level diagram or pseudocode representation of your system's architecture.

2. Conceptual Blend Generation (200-250 words):
   a) Generate a specific conceptual blend that combines elements from {t['domain1']} and {t['domain2']}.
   b) Explain the cognitive processes and AI techniques your system would use to create this blend.
   c) Discuss how the blend explores or relates to the concept of {t['concept']}.
   d) Provide a concrete example of how this blend could be applied or manifested in the real world.

3. Metaphor Creation (200-250 words):
   a) Create a novel metaphor that relates {t['domain1']} to {t['domain2']} or vice versa.
   b) Explain how your system would generate and evaluate the quality of this metaphor.
   c) Analyze the linguistic and cognitive implications of the generated metaphor.
   d) Give an example of how this metaphor could be used in a specific context (e.g., education, advertising, or scientific explanation).

4. Cognitive and Linguistic Analysis (250-300 words):
   a) Analyze the cognitive processes involved in understanding your generated blend and metaphor.
   b) Discuss how your system's outputs might influence or reflect human conceptual thinking.
   c) Explain any insights about the relationship between language, thought, and creativity revealed by your system.
   d) Compare your system's approach to conceptual blending with human cognitive processes.

5. Applications and Implications (150-200 words):
   a) Propose two potential applications of your conceptual blend and metaphor generation system.
   b) Discuss the implications of such a system for fields like education, creative writing, or artificial creativity.
   c) Address any ethical considerations related to AI-generated conceptual blends and metaphors.

6. Evaluation and Future Directions (150-200 words):
   a) Suggest methods for evaluating the novelty, coherence, and usefulness of your system's outputs.
   b) Propose two potential improvements or extensions to your system.
   c) Discuss how this approach could contribute to our understanding of human cognition and creativity.

Ensure your response demonstrates a deep understanding of cognitive linguistics, artificial intelligence, and the specified domains. Use appropriate terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1200-1500 words. Include a word count at the end of your response."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response effectively integrates concepts from {t['domain1']} and {t['domain2']} in the conceptual blend and metaphor, providing concrete examples for each.",
            f"The generated blend and metaphor creatively explore the concept of {t['concept']}, with clear explanations of their real-world applications.",
            "The system architecture and generation process are clearly explained, scientifically plausible, and demonstrate a deep understanding of cognitive linguistics and AI techniques.",
            "The cognitive and linguistic analysis demonstrates comprehensive understanding of relevant theories and concepts, including a comparison with human cognitive processes.",
            "The response addresses all required sections and adheres to the specified word count range."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
