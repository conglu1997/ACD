import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "language_pair": "English-French",
                "quantum_concept": "superposition",
                "linguistic_phenomenon": "polysemy",
                "example_phrase": "bank",
                "contexts": ["financial institution", "river edge"]
            },
            {
                "language_pair": "Mandarin-Spanish",
                "quantum_concept": "entanglement",
                "linguistic_phenomenon": "semantic ambiguity",
                "example_phrase": "春天 (chūntiān)",
                "contexts": ["spring season", "springtime of life"]
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum-inspired language model that can capture and process semantic ambiguity in natural language, focusing on the {t['language_pair']} language pair. Your model should incorporate the quantum concept of {t['quantum_concept']} to address the linguistic phenomenon of {t['linguistic_phenomenon']}. Use the example phrase "{t['example_phrase']}" with contexts {t['contexts']} to illustrate your model's capabilities.

Your response must follow this structure:

1. Theoretical Framework (250-300 words):
   a) Explain how you apply {t['quantum_concept']} to model {t['linguistic_phenomenon']} in natural language.
   b) Describe the key components of your quantum-inspired language model.
   c) Discuss how your model differs from classical approaches to handling {t['linguistic_phenomenon']}.

2. Mathematical Formulation (250-300 words):
   a) Provide a detailed mathematical representation of your model, using quantum mechanical notation.
   b) Explain each component of your equations and their linguistic interpretations.
   c) Describe how your model computes semantic representations and handles ambiguity.
   d) Include at least one complex equation that combines quantum mechanics with linguistic features, ensuring it's directly relevant to your model's core functionality.

3. Quantum-Linguistic Mapping (200-250 words):
   a) Detail how you map linguistic features to quantum states or operators.
   b) Explain how your model represents and manipulates semantic meaning in a quantum framework.
   c) Provide a step-by-step example of how "{t['example_phrase']}" would be represented and processed in your model, considering the given contexts.

4. Cross-lingual Adaptation (150-200 words):
   a) Explain how your model handles translation between {t['language_pair']}.
   b) Discuss any language-specific challenges and how your quantum approach addresses them.
   c) Describe how your model preserves semantic nuances across languages.

5. Implementation Considerations (150-200 words):
   a) Discuss the computational requirements for implementing your model.
   b) Address potential limitations or challenges in realizing your model with current technology.
   c) Propose a method for training and optimizing your quantum-inspired language model.

6. Evaluation and Benchmarking (150-200 words):
   a) Suggest specific metrics for evaluating your model's performance in handling {t['linguistic_phenomenon']}.
   b) Propose a detailed experiment to compare your quantum-inspired model with at least two state-of-the-art classical NLP approaches.
   c) Discuss potential real-world applications of your model, with at least one novel use case.

Ensure your response demonstrates a deep understanding of both quantum mechanics and computational linguistics. Use appropriate technical terminology and provide clear explanations where necessary. Be innovative in your approach while maintaining scientific plausibility.

Your total response should be between 1150-1450 words. Use LaTeX notation for mathematical equations, enclosing them in dollar signs (e.g., $E = mc^2$). For non-ASCII characters, use Unicode representations."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of both quantum mechanics and computational linguistics, with correct use of technical terminology from both fields.",
            "The proposed model innovatively applies the specified quantum concept to natural language processing, clearly differentiating it from classical approaches.",
            "The mathematical formulation is sound, detailed, and clearly explained, including at least one complex equation that is directly relevant to the model's core functionality.",
            "The model effectively addresses the specified linguistic phenomenon and language pair, with a clear step-by-step example using the given phrase and contexts.",
            "The response considers practical implementation challenges, proposes specific evaluation metrics, and suggests a novel real-world application.",
            "The response adheres to the required structure and word count, with appropriate use of LaTeX notation for equations."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
