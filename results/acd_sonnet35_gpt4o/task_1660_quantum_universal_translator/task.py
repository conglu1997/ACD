import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        language_pairs = [
            ("Mandarin Chinese", "English"),
            ("Arabic", "Spanish")
        ]
        linguistic_phenomena = [
            "idiomatic expressions",
            "context-dependent meanings"
        ]
        return {
            str(i+1): {
                'source_language': pair[0],
                'target_language': pair[1],
                'linguistic_phenomenon': phenomenon
            } for i, (pair, phenomenon) in enumerate(zip(language_pairs, linguistic_phenomena))
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum-inspired AI system for real-time universal translation between {t['source_language']} and {t['target_language']}, with a focus on accurately handling {t['linguistic_phenomenon']}. Your response should include:

1. Quantum-Linguistic Architecture (300-350 words):
   a) Describe the key components of your quantum-inspired translation system.
   b) Explain how quantum principles (e.g., entanglement, superposition) are incorporated into your design.
   c) Detail how your system addresses the challenge of {t['linguistic_phenomenon']}.
   d) Include a simple diagram or schematic of your architecture using ASCII characters within your response.

2. Quantum-Enhanced Translation Process (250-300 words):
   a) Outline the step-by-step process of how your system translates from {t['source_language']} to {t['target_language']}.
   b) Explain how quantum computations are used in this process.
   c) Describe how your system maintains coherence and manages decoherence in the translation process.

3. Handling Linguistic Complexities (200-250 words):
   a) Discuss how your system specifically addresses {t['linguistic_phenomenon']} between {t['source_language']} and {t['target_language']}.
   b) Provide an example of a challenging {t['linguistic_phenomenon']} and how your system would handle it.
   c) Explain how your quantum approach offers advantages over classical methods for this challenge.

4. Training and Optimization (200-250 words):
   a) Describe how you would train your quantum-inspired translation system.
   b) Discuss any unique challenges in optimizing quantum-linguistic models and how you'd address them.
   c) Explain how your system could adapt to new linguistic data or evolving language use.

5. Performance Evaluation (150-200 words):
   a) Propose metrics to evaluate your system's translation quality and quantum advantage.
   b) Describe an experiment to compare your system's performance against state-of-the-art classical translation systems.
   c) Discuss potential limitations of your approach and how they might be addressed in future iterations.

6. Ethical and Societal Implications (150-200 words):
   a) Analyze potential impacts of a quantum-enhanced universal translator on global communication and culture.
   b) Discuss ethical considerations, including privacy concerns and potential misuse.
   c) Propose guidelines for responsible development and deployment of such technology.

7. Specific Translation Example (100-150 words):
   Provide a specific example of how your system would translate a complex phrase or sentence from {t['source_language']} to {t['target_language']}, highlighting how it handles {t['linguistic_phenomenon']}. Explain the quantum processes involved in this specific translation.

Ensure your response demonstrates a deep understanding of quantum computing, linguistics, and AI. Be creative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section. Your total response should be between 1350-1700 words. Include a word count at the end of your submission."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of quantum computing principles and their potential application to language translation",
            "The proposed system shows creative and plausible integration of quantum concepts with linguistic processing",
            f"The design effectively addresses the challenge of handling {t['linguistic_phenomenon']} between {t['source_language']} and {t['target_language']}",
            "The response includes a clear and logical explanation of the translation process, training methodology, and performance evaluation",
            "The submission thoughtfully considers ethical implications and societal impacts of the technology",
            "The specific translation example effectively illustrates the system's approach to handling complex linguistic phenomena",
            "The response adheres to the specified word count and formatting requirements"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
