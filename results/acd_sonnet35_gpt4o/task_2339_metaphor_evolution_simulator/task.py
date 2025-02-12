import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        domains = [
            "Mathematics",
            "Politics",
            "Emotional Intelligence",
            "Environmental Science",
            "Quantum Physics",
            "Art History",
            "Artificial Intelligence"
        ]
        cognitive_mechanisms = [
            "Analogical Reasoning",
            "Conceptual Blending",
            "Image Schema Formation",
            "Embodied Simulation",
            "Metaphorical Mapping",
            "Cognitive Categorization",
            "Mental Space Integration"
        ]
        return {
            "1": {
                "domain": random.choice(domains),
                "cognitive_mechanism": random.choice(cognitive_mechanisms)
            },
            "2": {
                "domain": random.choice(domains),
                "cognitive_mechanism": random.choice(cognitive_mechanisms)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that simulates the evolution of metaphorical thinking in human cognition, then use it to analyze the development of abstract reasoning in the domain of {t['domain']}, focusing on the cognitive mechanism of {t['cognitive_mechanism']}.

Key terms:
- Conceptual Blending: The cognitive process of combining two or more mental spaces to create new conceptual structures.
- Image Schema Formation: The development of abstract patterns in our understanding based on bodily experiences.
- Embodied Simulation: The process of understanding concepts by mentally simulating related physical experiences.
- Metaphorical Mapping: The systematic correspondence between two conceptual domains in metaphorical thinking.
- Cognitive Categorization: The mental process of grouping items based on shared characteristics.
- Mental Space Integration: The blending of different conceptual scenarios in cognitive processing.

Your response should include:

1. System Architecture (300-400 words):
   a) Describe the key components of your AI system for simulating metaphor evolution.
   b) Explain how your system models the cognitive process of metaphor creation and comprehension.
   c) Detail how the system incorporates principles from evolutionary psychology and cognitive linguistics.
   d) Include a diagram or flowchart of your system architecture using ASCII art or Unicode characters.

2. Metaphor Evolution Model (250-350 words):
   a) Explain the mechanisms your system uses to simulate the evolution of metaphorical thinking.
   b) Describe how your model accounts for cultural and environmental factors in metaphor evolution.
   c) Discuss how your system handles the emergence and propagation of new metaphors.

3. Implementation for {t['domain']} (250-350 words):
   a) Describe how you would apply your system to analyze the development of abstract reasoning in {t['domain']}.
   b) Explain how the cognitive mechanism of {t['cognitive_mechanism']} is incorporated into this analysis.
   c) Provide an example of how your system might trace the evolution of a specific metaphor in this domain.

4. Simulation and Analysis (200-300 words):
   a) Describe the data inputs your system would require for this simulation.
   b) Explain how you would validate the output of your simulation against real-world data or theories.
   c) Discuss potential insights your system might provide about the role of metaphor in the development of abstract reasoning in {t['domain']}.

5. Ethical Considerations (150-250 words):
   a) Discuss potential ethical implications of simulating cognitive evolution and metaphorical thinking.
   b) Address concerns about cultural bias in your system and how you might mitigate them.
   c) Consider the potential impact of this technology on our understanding of human cognition and its applications.

6. Limitations and Future Directions (150-250 words):
   a) Identify key limitations of your proposed system.
   b) Suggest potential improvements or extensions to address these limitations.
   c) Propose a research direction that could further advance our understanding of metaphor evolution and abstract reasoning.

Ensure your response demonstrates a deep understanding of cognitive linguistics, evolutionary psychology, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative and innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1300-1900 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of cognitive linguistics, evolutionary psychology, and AI system design.",
            f"The system architecture and metaphor evolution model are well-explained and incorporate principles from the relevant fields.",
            f"The implementation for {t['domain']} is thoughtfully described, with a clear explanation of how {t['cognitive_mechanism']} is incorporated.",
            "The simulation and analysis section provides a plausible approach to validating the system and deriving insights.",
            "Ethical considerations are thoroughly addressed, including potential biases and impacts.",
            "Limitations are realistically assessed, and future directions are insightfully proposed.",
            "The response shows creativity and innovation while maintaining scientific plausibility."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
