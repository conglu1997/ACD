import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        concepts = [
            {
                "concept": "quantum entanglement",
                "source_domain": "social relationships",
                "target_domain": "particle physics"
            },
            {
                "concept": "neural plasticity",
                "source_domain": "architecture",
                "target_domain": "neuroscience"
            }
        ]
        return {
            "1": random.choice(concepts),
            "2": random.choice(concepts)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that generates and manipulates conceptual metaphors across different domains of knowledge. Then, use your system to create novel metaphors for the abstract scientific concept of {t['concept']}, drawing from the source domain of {t['source_domain']} and applying it to the target domain of {t['target_domain']}. Your response should include:

1. System Architecture (250-300 words):
   a) Describe the key components of your metaphor generation AI system.
   b) Explain how your system represents and processes knowledge from different domains.
   c) Detail the mechanisms for identifying potential metaphorical mappings between domains.
   d) Discuss how your system evaluates and refines generated metaphors.

2. Cognitive Model (200-250 words):
   a) Explain how your system models the cognitive processes involved in metaphor comprehension and generation.
   b) Describe how it accounts for cultural and contextual factors in metaphor interpretation.
   c) Discuss any novel computational or AI techniques your system employs to mimic human-like metaphorical thinking.

3. Metaphor Generation (250-300 words):
   a) Provide a step-by-step explanation of how your system would generate metaphors for {t['concept']}.
   b) Present at least three novel metaphors created by your system, explaining the mapping between {t['source_domain']} and {t['target_domain']}.
   c) Analyze the strengths and potential limitations of each generated metaphor.

4. Evaluation and Applications (200-250 words):
   a) Propose metrics or methods to evaluate the quality and effectiveness of the generated metaphors.
   b) Discuss potential applications of your system in fields such as science education, creative writing, or scientific discovery.
   c) Explore how this system might enhance our understanding of human cognition and creativity.

5. Ethical Considerations and Future Directions (150-200 words):
   a) Discuss any ethical implications of using AI-generated metaphors in scientific communication or education.
   b) Address potential risks or limitations of relying on machine-generated conceptual metaphors.
   c) Suggest future research directions to expand or improve your system.

Ensure your response demonstrates a deep understanding of cognitive linguistics, metaphor theory, and artificial intelligence. Be creative in your system design and metaphor generation while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex ideas.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1050-1300 words, not including the headings."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response includes a detailed system architecture for generating metaphors between {t['source_domain']} and {t['target_domain']}.",
            f"The system generates at least three novel metaphors for {t['concept']}.",
            "The response demonstrates a deep understanding of cognitive linguistics and metaphor theory.",
            "The proposed evaluation metrics and applications are well-reasoned and innovative.",
            "The ethical considerations and future directions are thoughtfully addressed."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
