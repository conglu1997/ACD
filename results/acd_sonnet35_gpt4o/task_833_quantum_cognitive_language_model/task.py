import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cognitive_principles = [
            "embodied cognition",
            "conceptual metaphor theory",
            "frame semantics",
            "prototype theory",
            "cognitive grammar"
        ]
        quantum_concepts = [
            "superposition",
            "entanglement",
            "quantum interference",
            "quantum tunneling",
            "quantum annealing"
        ]
        language_tasks = [
            "metaphor generation",
            "semantic disambiguation",
            "contextual inference",
            "language translation",
            "sentiment analysis"
        ]
        return {
            "1": {
                "cognitive_principle": random.choice(cognitive_principles),
                "quantum_concept": random.choice(quantum_concepts),
                "language_task": random.choice(language_tasks)
            },
            "2": {
                "cognitive_principle": random.choice(cognitive_principles),
                "quantum_concept": random.choice(quantum_concepts),
                "language_task": random.choice(language_tasks)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum-based language model that incorporates the cognitive linguistic principle of {t['cognitive_principle']} and leverages the quantum computing concept of {t['quantum_concept']} to enhance the language task of {t['language_task']}. Your response should include:

1. Theoretical Framework (250-300 words):
   a) Explain the key aspects of {t['cognitive_principle']} and how it relates to language processing.
   b) Describe how {t['quantum_concept']} can be applied to computational linguistics.
   c) Discuss potential synergies between the cognitive principle and quantum concept.

2. Model Architecture (300-350 words):
   a) Outline the architecture of your quantum-cognitive language model.
   b) Explain how it integrates {t['cognitive_principle']} into its structure or algorithms.
   c) Describe how {t['quantum_concept']} is implemented in the model.
   d) Discuss any novel algorithms or approaches used in your design.

3. Task-Specific Implementation (250-300 words):
   a) Explain how your model would approach the task of {t['language_task']}.
   b) Provide a step-by-step description of how the model processes input and generates output for this task.
   c) Discuss potential advantages of your model over classical approaches for this specific task.

4. Performance Analysis (200-250 words):
   a) Propose metrics to evaluate your model's performance on {t['language_task']}.
   b) Discuss potential challenges in implementing or training your model.
   c) Compare the expected performance of your model to state-of-the-art classical models for this task.

5. Broader Implications (200-250 words):
   a) Discuss how your model could contribute to our understanding of human language processing.
   b) Explore potential applications of your model beyond {t['language_task']}.
   c) Address ethical considerations related to the development and use of quantum-cognitive language models.

6. Conclusion (50-100 words):
   Summarize the key innovations of your model and its potential impact on the field of quantum-cognitive linguistics.

Ensure your response demonstrates a deep understanding of cognitive linguistics, quantum computing, and natural language processing. Be innovative in your approach while maintaining scientific plausibility. Use appropriate terminology from all relevant fields and provide explanations where necessary.

Cite relevant research or sources throughout your response to support your ideas and demonstrate knowledge of current literature in the field.

Format your response with clear headings for each section and subsections labeled a, b, c, d as appropriate. Your total response should be between 1250-1550 words.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a clear understanding of {t['cognitive_principle']} and {t['quantum_concept']}, and their potential applications in language processing.",
            "The proposed model architecture is innovative, well-explained, and potentially implementable.",
            f"The implementation for {t['language_task']} is thoroughly described and leverages the unique aspects of the quantum-cognitive model.",
            "The performance analysis and broader implications sections show deep, critical thinking about the model's potential impact and limitations.",
            "The response maintains scientific plausibility while being creative and original in its approach.",
            "The response includes relevant citations and demonstrates knowledge of current literature in the field.",
            "The conclusion effectively summarizes the key innovations and potential impact of the proposed model."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
