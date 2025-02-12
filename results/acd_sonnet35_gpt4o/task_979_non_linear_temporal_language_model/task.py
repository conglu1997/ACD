import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        temporal_structures = [
            {
                "structure": "circular time",
                "example": "In a world where yesterday is tomorrow and tomorrow is yesterday"
            },
            {
                "structure": "branching time",
                "example": "As the timeline split into multiple possibilities"
            }
        ]
        return {
            "1": random.choice(temporal_structures),
            "2": random.choice(temporal_structures)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a language model that incorporates non-linear time perception, specifically {t['structure']}, and use it to generate and analyze text with complex temporal structures. Your response should include:

1. Model Design (250-300 words):
   a) Describe the key components of your language model that enable it to handle {t['structure']}.
   b) Explain how your model represents and processes temporal information differently from traditional linear models.
   c) Discuss any novel algorithms or data structures you've incorporated to achieve this non-linear temporal reasoning.

2. Implementation Details (200-250 words):
   a) Provide a high-level overview of how you would implement this model using existing NLP frameworks or techniques.
   b) Describe any modifications needed to standard language model architectures (e.g., transformers) to accommodate non-linear time.
   c) Discuss potential challenges in training this model and how you would address them.

3. Text Generation (200-250 words):
   a) Use your model to generate a short passage (50-75 words) that demonstrates {t['structure']}. Start with the prompt: "{t['example']}".
   b) Explain how the generated text showcases the model's understanding of non-linear time.
   c) Analyze any interesting patterns or structures in the generated text that reflect the {t['structure']}.

4. Comparative Analysis (200-250 words):
   a) Compare your model's approach to handling temporal information with that of traditional linear language models.
   b) Discuss potential advantages and limitations of your non-linear temporal model in various NLP tasks (e.g., translation, summarization, question-answering).
   c) Propose an experiment to quantitatively compare the performance of your model against a traditional model on a specific NLP task involving complex temporal reasoning.

5. Cognitive and Linguistic Implications (150-200 words):
   a) Discuss how your model's approach to non-linear time might relate to human cognition and perception of time.
   b) Explore potential applications of this model in studying or simulating non-linear temporal concepts in various cultures or in speculative fiction.
   c) Consider ethical implications of developing AI systems with non-linear temporal reasoning capabilities.

Ensure your response demonstrates a deep understanding of natural language processing, cognitive science, and computer science. Be innovative in your approach while maintaining scientific plausibility and addressing the complexities of non-linear temporal reasoning."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of language models and non-linear temporal reasoning.",
            "The model design is innovative and well-explained, addressing the complexities of the given temporal structure.",
            "The generated text clearly demonstrates the non-linear temporal structure specified.",
            "The comparative analysis is thorough and insightful.",
            "The discussion of cognitive and linguistic implications is well-reasoned and considers ethical aspects."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
