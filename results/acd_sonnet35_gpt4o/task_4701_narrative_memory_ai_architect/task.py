import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        narrative_types = [
            "Personal episodic memory",
            "Historical event reconstruction",
            "Fictional story analysis",
            "Cultural myth interpretation"
        ]
        cognitive_aspects = [
            "Temporal sequencing",
            "Emotional valence",
            "Spatial context",
            "Causal reasoning"
        ]
        return {
            "1": {"narrative": random.choice(narrative_types), "aspect": random.choice(cognitive_aspects)},
            "2": {"narrative": random.choice(narrative_types), "aspect": random.choice(cognitive_aspects)}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system for narrative memory reconstruction and analysis, focusing on {t['narrative']} and emphasizing the cognitive aspect of {t['aspect']}. Your response should address the following:

1. System Architecture (250-300 words):
   a) Describe the key components of your AI system for narrative memory reconstruction and analysis.
   b) Explain how it integrates principles from cognitive science, linguistics, and AI.
   c) Detail how your system handles the specific narrative type and cognitive aspect.
   d) Discuss any novel technologies or theoretical concepts your system employs.

2. Narrative Processing Mechanism (200-250 words):
   a) Explain how your system processes and reconstructs narratives.
   b) Describe how it handles the complexity of {t['aspect']} in this context.
   c) Discuss how your system addresses challenges specific to {t['narrative']}.

3. Concrete Example (150-200 words):
   Provide a specific example of how your system would operate in a given scenario, demonstrating its narrative reconstruction and analysis capabilities.

4. Linguistic and Cognitive Principles (200-250 words):
   a) Discuss the linguistic theories and cognitive models your system is based on.
   b) Explain how these principles are implemented in your AI architecture.
   c) Analyze potential limitations of current theories and how your system addresses them.

5. Evaluation and Validation (150-200 words):
   a) Propose methods to evaluate the accuracy and effectiveness of your system's narrative reconstructions.
   b) Suggest experiments to validate your system's performance in analyzing {t['aspect']}.
   c) Discuss potential challenges in verifying the authenticity of AI-generated narrative analyses.

6. Ethical and Societal Implications (200-250 words):
   a) Discuss the ethical implications of creating AI systems capable of narrative memory reconstruction and analysis.
   b) Analyze potential impacts on concepts of memory, identity, and historical truth.
   c) Propose guidelines for responsible development and use of narrative memory AI systems.

7. Potential Applications (150-200 words):
   a) Describe at least two potential applications of your system in fields such as psychology, history, or literature.
   b) Explain the benefits and challenges of using your AI system in these contexts.
   c) Discuss any necessary modifications to adapt your system for these applications.

Ensure your response demonstrates a deep understanding of cognitive science, linguistics, and AI principles. Be creative in your approach while maintaining scientific plausibility throughout. Use appropriate technical terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section. Your total response should be between 1300-1650 words.

Note: Your response will be evaluated based on the depth of understanding, innovation, scientific plausibility, and adherence to the task requirements. A successful response will thoroughly address all aspects of the task while maintaining consistency and scientific rigor."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of cognitive science, linguistics, and AI principles.",
            "The proposed system architecture is innovative and integrates principles from multiple disciplines.",
            "The narrative processing mechanism is well-explained and addresses the specific narrative type and cognitive aspect.",
            "The concrete example effectively illustrates the system's capabilities.",
            "The discussion of linguistic and cognitive principles is thorough and scientifically grounded.",
            "The evaluation and validation methods proposed are appropriate and comprehensive.",
            "The ethical and societal implications are thoughtfully analyzed.",
            "The potential applications are creative and well-reasoned.",
            "The response is well-structured, clear, and within the specified word count.",
            "The response maintains scientific plausibility throughout."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
