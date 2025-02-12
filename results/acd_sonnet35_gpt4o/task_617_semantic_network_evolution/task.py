import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cognitive_principles = [
            "Hebbian learning",
            "Spreading activation"
        ]
        linguistic_theories = [
            "Construction grammar",
            "Cognitive metaphor theory"
        ]
        return {
            str(i+1): {
                'cognitive_principle': random.choice(cognitive_principles),
                'linguistic_theory': random.choice(linguistic_theories)
            } for i in range(2)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design and analyze an evolving semantic network for AI language understanding, incorporating the cognitive principle of {t['cognitive_principle']} and the linguistic theory of {t['linguistic_theory']}. Your response should include:

1. Semantic Network Design (200-250 words):
   a) Describe the basic structure and components of your semantic network.
   b) Explain how you incorporate the given cognitive principle and linguistic theory into your network design.
   c) Provide a simple visual representation or description of a small section of your network.

2. Evolution Mechanism (150-200 words):
   a) Explain how your semantic network evolves over time as it processes new information.
   b) Describe specific mechanisms or algorithms that drive this evolution, relating them to the given cognitive principle.
   c) Discuss how this evolution reflects or simulates aspects of human language acquisition.

3. Language Understanding Application (200-250 words):
   a) Describe how your evolving semantic network would process and understand a complex linguistic input (e.g., a metaphorical expression or an ambiguous sentence).
   b) Explain how the network's structure and evolution contribute to this understanding.
   c) Compare this process to human language comprehension, highlighting similarities and differences.

4. AI Implications (150-200 words):
   a) Discuss the potential advantages of your approach for AI language understanding compared to current methods.
   b) Identify challenges or limitations of implementing this system in real-world AI applications.
   c) Propose one specific area of AI where your approach could lead to significant improvements.

5. Cognitive Science Insights (150-200 words):
   a) Explain how your model might contribute to our understanding of human semantic memory and language processing.
   b) Propose a hypothesis about human cognition that could be tested using your model.
   c) Describe an experiment to test this hypothesis, including methodology and expected outcomes.

6. Ethical Considerations (100-150 words):
   a) Discuss potential ethical implications of implementing evolving semantic networks in AI systems.
   b) Address concerns related to bias, privacy, or transparency that might arise from your approach.

7. Future Directions (100-150 words):
   a) Suggest two potential extensions or modifications to your model for future research.
   b) Explain how these extensions might further bridge the gap between AI and human-like language understanding.

Ensure your response demonstrates a deep understanding of semantic networks, the specified cognitive principle and linguistic theory, and their applications in AI. Be creative in your approach while maintaining scientific plausibility and logical consistency. Use appropriate terminology from cognitive science, linguistics, and AI throughout your response.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of semantic networks, the specified cognitive principle, and linguistic theory",
            "The semantic network design and evolution mechanism are clearly explained and logically incorporate the given principles",
            "The language understanding application is well-described and compared thoughtfully to human comprehension",
            "The AI implications, cognitive science insights, and ethical considerations are thoroughly explored",
            "The response shows creativity and speculative thinking while maintaining scientific plausibility"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
