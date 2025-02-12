import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "interface_type": "Thought-to-Language",
                "consciousness_aspect": "Qualia",
                "linguistic_focus": "Semantic Representation"
            },
            {
                "interface_type": "Language-to-Thought",
                "consciousness_aspect": "Self-awareness",
                "linguistic_focus": "Pragmatics"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""
        Design a hypothetical neural interface system that translates between human conscious experience and a universal language of thought. Your system should focus on {t['interface_type']} translation, with particular emphasis on the consciousness aspect of {t['consciousness_aspect']} and the linguistic focus of {t['linguistic_focus']}. Your response should include:

        1. System Architecture (250-300 words):
           a) Describe the key components of your neural interface system.
           b) Explain how these components interact to facilitate the translation between conscious experience and language.
           c) Detail how your system incorporates current understanding of neural correlates of consciousness and language processing.

        2. Translation Mechanism (200-250 words):
           a) Explain the process of translating between conscious experience and the universal language of thought.
           b) Describe how your system handles the specific consciousness aspect and linguistic focus mentioned.
           c) Discuss any novel algorithms or data structures required for this translation.

        3. Consciousness-Language Mapping (200-250 words):
           a) Propose a framework for mapping between elements of conscious experience and linguistic structures.
           b) Explain how your system addresses the hard problem of consciousness in this mapping.
           c) Discuss how your approach might provide insights into the nature of consciousness and language.

        4. AI Integration (150-200 words):
           a) Describe how artificial intelligence is utilized in your system.
           b) Explain the role of machine learning in improving translation accuracy over time.
           c) Discuss any potential for emergent behaviors or understanding in the AI component.

        5. Ethical and Philosophical Implications (200-250 words):
           a) Analyze the ethical considerations of a system that can interface directly with consciousness.
           b) Discuss the philosophical implications of a universal language of thought.
           c) Consider potential societal impacts of this technology, both positive and negative.

        6. Limitations and Future Directions (100-150 words):
           a) Identify potential limitations or challenges in implementing your system.
           b) Propose future research directions to overcome these limitations.
           c) Speculate on how this technology might evolve in the next 50 years.

        Ensure your response demonstrates a deep understanding of neuroscience, linguistics, artificial intelligence, and philosophy of mind. Be innovative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.

        Format your response with clear headings for each section, numbered as above. Your total response should be between 1100-1400 words.
        """

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response accurately addresses the {t['interface_type']} translation, with emphasis on {t['consciousness_aspect']} and {t['linguistic_focus']}.",
            "The system architecture and translation mechanism are innovative yet scientifically plausible.",
            "The consciousness-language mapping demonstrates a deep understanding of the hard problem of consciousness.",
            "The AI integration is well-explained and considers potential emergent behaviors.",
            "The ethical and philosophical implications are thoroughly analyzed.",
            "The response shows a high level of interdisciplinary knowledge integration and creative problem-solving."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
