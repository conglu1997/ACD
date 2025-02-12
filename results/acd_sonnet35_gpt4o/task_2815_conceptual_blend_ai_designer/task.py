import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        domains = [
            "politics and cuisine",
            "quantum physics and mythology",
            "music theory and evolutionary biology",
            "architecture and neuroscience",
            "economics and ecology"
        ]
        blend_types = [
            "mirror network",
            "single-scope network",
            "double-scope network",
            "simplex network"
        ]
        return {
            "1": {
                "domain": random.choice(domains),
                "blend_type": random.choice(blend_types)
            },
            "2": {
                "domain": random.choice(domains),
                "blend_type": random.choice(blend_types)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system capable of understanding and generating conceptual blends, then use it to create a novel blend in the domain of {t['domain']} using a {t['blend_type']}. Your response should include:

1. System Architecture (250-300 words):
   a) Describe the overall structure of your AI system for conceptual blending.
   b) Explain how your system integrates knowledge representation, reasoning, and natural language processing.
   c) Detail the key components that enable the system to understand and generate conceptual blends.
   d) Discuss any novel algorithms or techniques specific to conceptual blending.

2. Conceptual Blending Process (200-250 words):
   a) Explain how your system identifies and selects input spaces for blending.
   b) Describe the process of mapping between input spaces and creating the blended space.
   c) Discuss how your system handles emergent structure in the blended space.
   d) Explain how the system ensures the coherence and meaningfulness of the generated blends.

3. Domain-Specific Adaptation (150-200 words):
   a) Describe how your system is adapted to work with the given domain of {t['domain']}.
   b) Explain any domain-specific knowledge or heuristics incorporated into the system.
   c) Discuss potential challenges in applying conceptual blending to this domain and how your system addresses them.

4. Generated Conceptual Blend (250-300 words):
   a) Present a detailed description of a novel conceptual blend your system would generate in the domain of {t['domain']}.
   b) Explain how this blend exemplifies a {t['blend_type']}.
   c) Analyze the input spaces, cross-space mappings, and emergent structure in your generated blend.
   d) Discuss the potential implications or applications of this novel blend.

5. Evaluation and Interpretation (200-250 words):
   a) Propose methods to evaluate the creativity and coherence of the generated conceptual blends.
   b) Describe how you would validate the system's output against human-created conceptual blends.
   c) Discuss potential applications of this technology in fields such as innovation, problem-solving, or artistic creation.

6. Ethical and Cognitive Implications (150-200 words):
   a) Discuss the potential impact of AI-generated conceptual blends on human cognition and creativity.
   b) Address any ethical considerations related to AI systems creating novel concepts or ideas.
   c) Explore how this technology might influence our understanding of human creativity and conceptual thinking.

7. Limitations and Future Directions (150-200 words):
   a) Identify potential limitations or challenges in your AI conceptual blending system.
   b) Propose two ways to extend or improve your system in future research.
   c) Suggest a specific experiment to further explore the relationship between AI, conceptual blending, and human cognition.

Ensure your response demonstrates a deep understanding of cognitive science, linguistics, and artificial intelligence. Be creative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.

Format your response using clear headings for each section, numbered as above. Your total response should be between 1350-1700 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response should describe a plausible AI system for conceptual blending, adapted to the domain of {t['domain']}.",
            f"The generated conceptual blend should be novel, coherent, and exemplify a {t['blend_type']}.",
            "The explanation should demonstrate a deep understanding of cognitive science, linguistics, and artificial intelligence.",
            "The response should address all required sections with appropriate depth and creativity.",
            "The proposed evaluation methods, ethical considerations, and future directions should be thoughtful and well-reasoned."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
