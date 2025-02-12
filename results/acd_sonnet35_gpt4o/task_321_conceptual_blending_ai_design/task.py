import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "input_concepts": ["Time", "Money"],
                "target_domain": "Business Communication"
            },
            {
                "input_concepts": ["Light", "Information"],
                "target_domain": "Education"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that can understand and generate language based on conceptual blending theory, focusing on blending the concepts of {t['input_concepts'][0]} and {t['input_concepts'][1]} in the domain of {t['target_domain']}. Your response should include:

1. Conceptual Blending Overview (100-150 words):
   Briefly explain conceptual blending theory and how it relates to language understanding and generation.

2. AI System Design (250-300 words):
   a) Describe the architecture of your AI system, including its main components and how they interact.
   b) Explain how your system implements conceptual blending, particularly for the given input concepts.
   c) Discuss any novel approaches or techniques you've incorporated to handle conceptual blending.
   d) Provide a specific example of a blended concept your system might generate using {t['input_concepts'][0]} and {t['input_concepts'][1]}.

3. Language Processing Example (150-200 words):
   Provide an example of how your AI system would process and generate language that blends the concepts of {t['input_concepts'][0]} and {t['input_concepts'][1]} in the context of {t['target_domain']}. Include both the input and output, and explain the blending process.

4. Potential Applications (100-150 words):
   Discuss potential applications of your AI system in the {t['target_domain']} domain and beyond. How might it enhance current language models or contribute to other fields?

5. Limitations, Biases, and Ethical Considerations (200-250 words):
   a) Identify potential limitations or challenges of your system.
   b) Discuss any potential biases that might arise in your AI system and how they could be mitigated.
   c) Analyze the ethical implications of using such an AI system, particularly in the context of {t['target_domain']}.

6. Future Developments (100-150 words):
   Propose one or two potential future developments or research directions that could enhance your AI system's conceptual blending capabilities.

Ensure your response demonstrates a deep understanding of conceptual blending theory, AI system design, and the practical applications of cognitive linguistics in artificial intelligence. Be creative in your approach while maintaining scientific and technical validity. Stay within the specified word limits for each section."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a clear understanding of conceptual blending theory and its application to AI.",
            "The AI system design is coherent, innovative, and properly incorporates conceptual blending mechanisms.",
            f"The language processing example effectively blends the concepts of {t['input_concepts'][0]} and {t['input_concepts'][1]} in the context of {t['target_domain']}.",
            "Potential applications are relevant and demonstrate creative thinking about the system's capabilities.",
            "Limitations, biases, ethical considerations, and future developments are thoughtfully discussed and relevant to the proposed system.",
            "The response adheres to the specified word limits for each section."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
