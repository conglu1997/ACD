import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        domains = [
            {
                "source_domain": "Fluid dynamics",
                "target_domain": "Economic systems",
                "problem": "Predicting market volatility"
            },
            {
                "source_domain": "Quantum entanglement",
                "target_domain": "Social networks",
                "problem": "Modeling information spread in online communities"
            }
        ]
        return {
            "1": random.choice(domains),
            "2": random.choice(domains)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system capable of generating and interpreting complex metaphors, and apply it to solve an abstract problem using metaphorical reasoning. Your task is to use {t['source_domain']} as a source domain to generate metaphors for {t['target_domain']}, and then apply this metaphorical framework to address the problem of {t['problem']}.

Your response should include the following sections:

1. Metaphorical AI System Design (300-350 words):
   a) Describe the key components of your AI system for metaphor generation and interpretation.
   b) Explain how your system integrates concepts from cognitive linguistics, particularly Conceptual Metaphor Theory.
   c) Detail the mechanisms your system uses to map concepts between domains and generate novel metaphors.
   d) Discuss how your system evaluates the relevance and effectiveness of generated metaphors.

2. Metaphor Generation (250-300 words):
   a) Generate at least three novel metaphors mapping concepts from {t['source_domain']} to {t['target_domain']}.
   b) Explain the reasoning behind each metaphor, highlighting the shared structural or functional similarities between the domains.
   c) Discuss how these metaphors provide new insights or perspectives on {t['target_domain']}.

3. Problem-Solving Application (300-350 words):
   a) Apply your metaphorical framework to address the problem of {t['problem']}.
   b) Explain how the generated metaphors inform your approach to the problem.
   c) Propose a specific solution or strategy based on your metaphorical reasoning.
   d) Discuss potential advantages and limitations of using this metaphorical approach to problem-solving.

4. Cognitive and AI Implications (200-250 words):
   a) Analyze how your metaphorical AI system's approach compares to human cognitive processes in metaphor creation and interpretation.
   b) Discuss potential implications of your system for advancing AI reasoning capabilities.
   c) Explore how this approach might contribute to our understanding of human cognition and creativity.

5. Ethical Considerations and Limitations (150-200 words):
   a) Identify potential ethical concerns or implications of using metaphorical AI systems for problem-solving.
   b) Discuss limitations of your approach and potential biases that might arise from metaphorical reasoning.
   c) Propose guidelines for the responsible development and use of metaphorical AI systems.

6. Future Directions (150-200 words):
   a) Suggest two potential enhancements or extensions to your metaphorical AI system.
   b) Propose a novel application of your system in a different field or domain.
   c) Discuss how emerging technologies or research in cognitive science might further improve metaphorical AI reasoning.

Ensure your response demonstrates a deep understanding of metaphor theory, artificial intelligence, and the specific domains involved. Be creative in your approach while maintaining scientific plausibility. Use appropriate terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section. Your total response should be between 1350-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response includes a detailed design of an AI system for metaphor generation and interpretation, with clear integration of concepts from cognitive linguistics.",
            f"At least three novel and insightful metaphors are generated, mapping concepts from {t['source_domain']} to {t['target_domain']}.",
            f"The metaphorical framework is effectively applied to address the problem of {t['problem']}, with a specific solution or strategy proposed.",
            "The response demonstrates a deep understanding of metaphor theory, artificial intelligence, and the specific domains involved.",
            "Ethical considerations and limitations of metaphorical AI systems are thoroughly discussed.",
            "The overall response is creative, scientifically plausible, and demonstrates strong interdisciplinary knowledge integration."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
