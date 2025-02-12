import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        memory_systems = [
            {
                "memory_system": "episodic memory",
                "language_task": "contextual question answering"
            },
            {
                "memory_system": "semantic memory",
                "language_task": "knowledge integration and reasoning"
            }
        ]
        return {
            "1": random.choice(memory_systems),
            "2": random.choice(memory_systems)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a cognitive architecture inspired by the human {t['memory_system']} system and apply it to enhance an AI language model's capabilities in {t['language_task']}. Your response should include:

1. Cognitive Architecture Design (300-350 words):
   a) Describe the key components and processes of your cognitive architecture, explaining how it mimics the human {t['memory_system']} system.
   b) Explain how your architecture interfaces with and enhances a language model's existing capabilities.
   c) Discuss any novel approaches or mechanisms in your design that address limitations of current language models.
   d) Provide a high-level diagram of your cognitive architecture (describe it in words).

2. Implementation in Language Models (250-300 words):
   a) Explain how you would integrate your cognitive architecture into an existing language model architecture (e.g., transformer-based models).
   b) Describe any modifications needed to the language model's training process or inference pipeline.
   c) Discuss potential challenges in implementing your architecture and propose solutions.

3. Enhanced Capabilities for {t['language_task']} (250-300 words):
   a) Describe how your cognitive architecture enhances the language model's performance in {t['language_task']}.
   b) Provide specific examples of tasks or scenarios where your architecture would significantly improve over current language models.
   c) Explain how you would evaluate and measure the improvements brought by your architecture.

4. Ethical Considerations and Limitations (200-250 words):
   a) Discuss potential ethical implications of implementing more human-like cognitive architectures in AI systems.
   b) Address any limitations or potential biases in your approach.
   c) Propose guidelines for responsible development and use of cognitive architecture-enhanced language models.

5. Future Directions and Broader Impact (150-200 words):
   a) Suggest how your cognitive architecture could be extended to other aspects of language understanding or generation.
   b) Discuss the potential impact of your approach on the field of artificial general intelligence (AGI).
   c) Propose a research agenda for further developing and refining cognitive architectures for AI systems.

Ensure your response demonstrates a deep understanding of cognitive science, neuroscience, and artificial intelligence. Use technical terminology appropriately and provide explanations where necessary. Be creative in your approach while maintaining scientific plausibility and logical consistency.

Format your response using clear headings for each section. Your total response should be between 1150-1400 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of the specified human memory system and its application to language models.",
            "The cognitive architecture design is innovative, well-explained, and scientifically plausible.",
            "The implementation strategy for language models is detailed and addresses potential challenges.",
            "The explanation of enhanced capabilities for the specified language task is clear and convincing.",
            "Ethical considerations and limitations are thoughtfully addressed.",
            "The discussion of future directions and broader impact is insightful and demonstrates interdisciplinary thinking."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
