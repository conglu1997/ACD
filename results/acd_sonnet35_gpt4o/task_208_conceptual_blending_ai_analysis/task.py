import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        ai_concepts = [
            {
                "name": "Neural Networks",
                "description": "Computational models inspired by biological neural networks",
                "key_feature": "Interconnected nodes that process and transmit information"
            },
            {
                "name": "Genetic Algorithms",
                "description": "Optimization technique based on principles of natural selection",
                "key_feature": "Evolution of solutions through mutation and crossover"
            },
            {
                "name": "Reinforcement Learning",
                "description": "Learning approach based on reward and punishment",
                "key_feature": "Agents learn optimal behavior through trial and error"
            },
            {
                "name": "Expert Systems",
                "description": "AI systems that emulate the decision-making ability of human experts",
                "key_feature": "Knowledge base and inference engine to solve complex problems"
            }
        ]
        return {
            "1": random.choice(ai_concepts),
            "2": random.choice(ai_concepts)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Apply conceptual blending theory to create a novel AI concept by blending {t['name']} with a non-AI domain of your choice. Then, analyze the implications of your conceptual blend. Complete the following steps:

1. Conceptual Blend Creation (100-150 words):
   a) Briefly describe {t['name']} and its key feature: {t['key_feature']}.
   b) Choose a non-AI domain (e.g., biology, architecture, music) and describe a key concept from that domain.
   c) Create a novel AI concept by blending {t['name']} with your chosen non-AI concept. Explain how the two input spaces are integrated in your blend.

2. Structural Analysis (100-150 words):
   a) Identify the shared conceptual structure between the two input spaces.
   b) Describe any emergent structure in your blend that isn't present in either input space.
   c) Explain how the blend preserves or modifies the key feature of {t['name']}.

3. Implications and Applications (150-200 words):
   a) Discuss potential applications of your blended AI concept in the field of artificial intelligence.
   b) Analyze how this conceptual blend might influence or change our understanding of AI systems.
   c) Identify any ethical considerations or challenges that might arise from implementing or researching this blended concept.

4. Cognitive Science Perspective (100-150 words):
   a) Explain how your conceptual blend reflects or challenges current theories of human cognition.
   b) Discuss how studying this AI blend might contribute to our understanding of human conceptual integration processes.

5. Future Research Directions (50-100 words):
   Propose two potential research questions or experiments that could further explore the implications of your blended AI concept.

Ensure your response demonstrates a deep understanding of conceptual blending theory, artificial intelligence concepts, and their potential implications for both AI development and cognitive science.

Please adhere to the word limits specified for each section. Your entire response should not exceed 750 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a clear understanding of conceptual blending theory and its application to AI concepts.",
            "The created conceptual blend is novel, well-defined, and shows a clear integration of the AI concept with a non-AI domain.",
            "The structural analysis is thorough and identifies both shared and emergent structures in the blend.",
            "The discussion of implications and applications is insightful and considers both practical and ethical aspects.",
            "The cognitive science perspective demonstrates an understanding of how the blend relates to human cognition and conceptual integration.",
            "The proposed future research directions are relevant and have the potential to advance understanding in AI and cognitive science.",
            "The overall response is coherent, well-structured, and demonstrates strong interdisciplinary reasoning.",
            "The response adheres to the specified word limits for each section and does not exceed 750 words in total."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
