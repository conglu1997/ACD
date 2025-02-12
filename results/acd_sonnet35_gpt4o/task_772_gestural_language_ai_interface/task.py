import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "context": "Space exploration",
                "constraint": "Limited visibility due to spacesuit helmets",
                "key_concepts": ["navigation", "danger", "resource management"]
            },
            {
                "context": "Underwater research",
                "constraint": "Limited auditory communication due to water pressure",
                "key_concepts": ["data collection", "equipment status", "team coordination"]
            }
        ]
        return {
            "1": random.choice(scenarios),
            "2": random.choice(scenarios)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system capable of interpreting and generating a novel gestural language for human-AI interaction in a {t['context']} scenario. Your system should address the constraint of {t['constraint']} and be able to communicate key concepts including {', '.join(t['key_concepts'])}. Your response should include the following sections:

1. Gestural Language Design (200-250 words):
   a) Describe the core principles of your gestural language, explaining how it addresses the given constraint.
   b) Detail the basic vocabulary and syntax of your language, with examples for each key concept.
   c) Explain how your language maintains clarity and avoids ambiguity in the given context.

2. AI System Architecture (200-250 words):
   a) Describe the key components of your AI system for interpreting and generating the gestural language.
   b) Explain how your system would process visual input to recognize gestures.
   c) Detail how your system would generate appropriate gestural responses.

3. Human-AI Interaction Scenario (150-200 words):
   a) Provide a specific example of a human-AI interaction using your gestural language in the given context.
   b) Describe how your AI system would interpret and respond to a complex message from a human.
   c) Explain how your system would handle potential misunderstandings or ambiguities.

4. Learning and Adaptation (150-200 words):
   a) Describe how your AI system would learn and improve its understanding of the gestural language over time.
   b) Explain how the system could adapt to individual user variations or new gestures.
   c) Discuss how the AI could potentially contribute to the evolution of the gestural language.

5. Ethical and Practical Considerations (100-150 words):
   a) Discuss potential ethical implications of using AI for gestural communication in the given context.
   b) Address any safety concerns and propose guidelines for responsible use of the system.
   c) Explain how your system would handle situations where clear communication is critical for safety or mission success.

Ensure your response demonstrates a deep understanding of non-verbal communication, embodied cognition, and AI systems. Be creative in your approach while maintaining scientific and technological plausibility. Use clear headings for each section in your response."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The gestural language design is creative, clear, and appropriate for the given context and constraints.",
            "The AI system architecture is well-thought-out and technically plausible.",
            "The human-AI interaction scenario effectively demonstrates the use of the gestural language and AI system.",
            "The learning and adaptation mechanisms are innovative and realistically applicable.",
            "Ethical and practical considerations are thoroughly addressed, with thoughtful solutions proposed.",
            "The response demonstrates a deep understanding of non-verbal communication, embodied cognition, and AI systems.",
            "The overall solution is creative while maintaining scientific and technological plausibility."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
