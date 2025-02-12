import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cultures = [
            "Japanese",
            "Nigerian (Yoruba)",
            "Mexican",
            "Russian",
            "Indian (Hindi)"
        ]
        metaphor_types = [
            "time",
            "emotions",
            "success/failure",
            "relationships",
            "life/death"
        ]
        return {
            "1": {"culture": random.choice(cultures), "metaphor_type": random.choice(metaphor_types)},
            "2": {"culture": random.choice(cultures), "metaphor_type": random.choice(metaphor_types)}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system to translate and interpret culturally-specific metaphors and idioms for the {t['culture']} culture, focusing on metaphors related to {t['metaphor_type']}. Your response should include:

1. System Design (250-300 words):
   a) Describe the key components of your AI system for metaphor translation and interpretation.
   b) Explain how the system would learn and understand cultural context.
   c) Detail the process of translating a metaphor from the specified culture to a universally understandable concept.

2. Cultural Analysis (200-250 words):
   a) Provide three examples of {t['culture']} metaphors or idioms related to {t['metaphor_type']}.
   b) Explain their cultural significance and how they differ from Western equivalents.
   c) Discuss challenges in translating these metaphors for a global audience.

3. AI Learning Process (200-250 words):
   a) Describe how your AI system would learn new metaphors and cultural contexts.
   b) Explain potential biases that might emerge in the learning process.
   c) Propose methods to mitigate these biases and ensure cultural sensitivity.

4. Ethical Considerations (150-200 words):
   a) Discuss ethical implications of using AI for cultural translation and interpretation.
   b) Address potential issues of cultural appropriation or misrepresentation.
   c) Propose guidelines for responsible development and use of such AI systems.

5. Practical Application (150-200 words):
   a) Describe a real-world scenario where your AI system could be applied.
   b) Explain potential benefits and challenges of using the system in this context.
   c) Discuss how the system might impact cross-cultural communication and understanding.

Ensure your response is creative, well-reasoned, and grounded in linguistic and cultural knowledge. Use clear headings for each section and number your points where appropriate."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of {t['culture']} culture and its metaphors related to {t['metaphor_type']}.",
            "The AI system design is innovative and addresses the complexities of cultural metaphor translation.",
            "The analysis of the AI learning process and potential biases is thorough and insightful.",
            "Ethical considerations are well-thought-out and address relevant issues in cultural AI applications.",
            "The practical application scenario is realistic and well-explained."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
