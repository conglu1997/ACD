import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        domains = [
            {
                "name": "Emotions",
                "key_concepts": ["joy", "anger", "fear", "sadness", "surprise", "disgust", "love", "hate", "anxiety", "contentment"]
            },
            {
                "name": "Quantum Physics",
                "key_concepts": ["superposition", "entanglement", "wave function", "uncertainty", "quantum field", "decoherence", "tunneling", "spin", "qubit", "measurement"]
            }
        ]
        return {str(i+1): domain for i, domain in enumerate(random.sample(domains, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a method to map and visualize the semantic space of the domain '{t['name']}', comparing human cognition to AI language models. Your task involves the following steps:

1. Semantic Space Framework (250-300 words):
   a) Propose a framework for representing the semantic space of {t['name']}.
   b) Explain how this framework captures relationships between concepts.
   c) Describe how your framework could be applied to both human cognition and AI language models.

2. Visualization Method (200-250 words):
   a) Design a creative method to visualize your semantic space framework.
   b) Explain how your visualization represents semantic relationships and distances.
   c) Describe how your visualization could highlight differences between human and AI semantic spaces.

3. Key Concept Analysis (200-250 words):
   Analyze the following key concepts within your semantic space framework:
   {', '.join(t['key_concepts'])}
   a) Explain the position of each concept in your semantic space.
   b) Describe potential differences in how humans and AI models might represent these concepts.

4. Cognitive Science Integration (150-200 words):
   a) Discuss how your semantic space framework relates to theories of human cognitive semantics.
   b) Explain how empirical cognitive science methods could be used to validate your framework.

5. AI Model Comparison (150-200 words):
   a) Propose a method to extract and compare the semantic space of an AI language model to your framework.
   b) Discuss potential insights this comparison could provide about AI language understanding.

6. Limitations and Extensions (100-150 words):
   a) Identify potential limitations of your semantic space framework and visualization method.
   b) Propose one extension or application of your framework to another area of cognitive science or AI research.

Ensure your response demonstrates a deep understanding of semantics, cognitive science, and AI language models. Use appropriate terminology and provide explanations where necessary. Be creative in your framework design and visualization method while maintaining scientific plausibility."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of semantics, cognitive science, and AI language models in the context of the '{t['name']}' domain.",
            "The proposed semantic space framework is creative, well-explained, and plausibly applicable to both human cognition and AI language models.",
            "The visualization method is innovative and effectively represents semantic relationships and distances.",
            f"The analysis of key concepts ({', '.join(t['key_concepts'])}) is thorough and insightful, considering both human and AI perspectives.",
            "The integration with cognitive science theories and empirical methods is well-reasoned and demonstrates interdisciplinary knowledge.",
            "The proposed method for comparing AI language models to the framework is feasible and potentially insightful.",
            "Limitations are honestly addressed, and the proposed extension demonstrates creative thinking about future applications."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
