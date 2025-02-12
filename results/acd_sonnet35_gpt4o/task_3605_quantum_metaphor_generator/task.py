import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_concepts = [
            {
                "concept": "superposition",
                "linguistic_feature": "polysemy",
                "target_domain": "decision-making",
                "input_phrase": "The cat is both curious and cautious."
            },
            {
                "concept": "entanglement",
                "linguistic_feature": "semantic dependency",
                "target_domain": "social relationships",
                "input_phrase": "Their fates were intertwined from the moment they met."
            }
        ]
        return {str(i+1): concept for i, concept in enumerate(quantum_concepts)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum-inspired language model for analyzing and generating metaphors, then use it to explore connections between quantum mechanics and linguistic theory. Your task involves the following steps:

1. Model Architecture (250-300 words):
   a) Design a language model architecture that incorporates principles from quantum mechanics, focusing on the concept of {t['concept']}.
   b) Explain how your model represents and processes the linguistic feature of {t['linguistic_feature']}.
   c) Describe how quantum principles enhance the model's ability to generate and analyze metaphors.
   d) Provide a high-level text-based diagram or pseudo-code illustrating the key components of your model.

2. Quantum-Linguistic Mapping (200-250 words):
   a) Establish a clear mapping between {t['concept']} and {t['linguistic_feature']}.
   b) Explain how this mapping contributes to metaphor generation and analysis.
   c) Discuss any challenges in implementing this mapping and how you addressed them.

3. Metaphor Generation and Analysis (250-300 words):
   a) Describe the process by which your model generates metaphors.
   b) Provide an example of a metaphor your model might generate, relating {t['concept']} to {t['target_domain']}.
   c) Analyze the generated metaphor, explaining how it reflects both quantum and linguistic principles.
   d) Demonstrate how your model would process and analyze the input phrase: "{t['input_phrase']}"

4. Theoretical Implications (200-250 words):
   a) Discuss how your model's performance might provide insights into the nature of metaphor and language.
   b) Explore potential connections between quantum mechanics and linguistic theory revealed by your model.
   c) Propose a novel hypothesis about language or cognition based on these connections.

5. Evaluation and Limitations (150-200 words):
   a) Propose methods to evaluate the quality and coherence of the generated metaphors.
   b) Discuss potential limitations of your quantum-inspired approach to language modeling.
   c) Suggest ways to address these limitations in future iterations of the model.

6. Ethical Considerations and Applications (150-200 words):
   a) Discuss ethical implications of using quantum-inspired AI models for language tasks.
   b) Propose two potential applications of your model outside of linguistics and physics.
   c) Address any concerns about the interpretability of quantum-inspired language models.

Ensure your response demonstrates a deep understanding of both quantum mechanics and linguistics. Use appropriate terminology from both fields and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section and number your paragraphs within each section. Adhere strictly to the word counts specified for each section. Your total response should be between 1200-1500 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The Model Architecture section must clearly explain how the quantum concept of {t['concept']} is incorporated into the language model.",
            f"The Quantum-Linguistic Mapping section should establish a clear and plausible connection between {t['concept']} and {t['linguistic_feature']}.",
            f"The Metaphor Generation and Analysis section must provide a coherent example of a metaphor relating {t['concept']} to {t['target_domain']}, and demonstrate how the model processes the given input phrase.",
            "The Theoretical Implications section should propose a novel and well-reasoned hypothesis about language or cognition based on the quantum-linguistic connections.",
            "The response must adhere to the specified word counts for each section, with a total word count between 1200-1500 words.",
            "The overall response must demonstrate interdisciplinary knowledge, creativity, and critical thinking in the domains of quantum mechanics, linguistics, and artificial intelligence."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
