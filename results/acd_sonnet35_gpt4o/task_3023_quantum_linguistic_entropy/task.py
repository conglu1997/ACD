import random
import math

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_concepts = ['superposition', 'entanglement', 'quantum tunneling']
        linguistic_features = ['syntax', 'semantics', 'pragmatics']
        entropy_levels = ['low (0.1-0.3)', 'medium (0.4-0.6)', 'high (0.7-0.9)']
        
        tasks = [
            {
                'quantum_concept': random.choice(quantum_concepts),
                'linguistic_feature': random.choice(linguistic_features),
                'target_entropy': random.choice(entropy_levels),
                'text_type': 'poetry'
            },
            {
                'quantum_concept': random.choice(quantum_concepts),
                'linguistic_feature': random.choice(linguistic_features),
                'target_entropy': random.choice(entropy_levels),
                'text_type': 'prose'
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum-inspired language model that incorporates principles of information theory, focusing on the quantum concept of {t['quantum_concept']} and the linguistic feature of {t['linguistic_feature']}. Then, use your model to analyze and generate {t['text_type']} with {t['target_entropy']} entropy characteristics. Your response should include:

1. Model Architecture (300-350 words):
   a) Explain how your language model incorporates the specified quantum concept.
   b) Describe how it integrates information theory principles, particularly entropy.
   c) Detail how the model addresses the given linguistic feature.
   d) Provide a mathematical formulation of your model, including at least two equations using LaTeX notation.

2. Quantum-Linguistic Integration (250-300 words):
   a) Analyze how the quantum concept influences or enhances the modeling of the linguistic feature.
   b) Discuss any novel emergent properties or capabilities arising from this integration.
   c) Explain how your model calculates or estimates textual entropy, providing a specific formula.

3. Text Generation (200-250 words):
   a) Use your model to generate a short piece of {t['text_type']} (about 50-100 words) with {t['target_entropy']} entropy.
   b) Explain how your model achieved the target entropy level, showing your calculations.
   c) Analyze the generated text in terms of its quantum and linguistic properties.

4. Comparative Analysis (200-250 words):
   a) Compare your quantum-inspired model to a classical language model, providing specific examples of how they would differ in processing the same input.
   b) Discuss potential advantages and limitations of your approach, with quantitative estimates where possible.
   c) Propose a method to empirically evaluate your model against classical alternatives, including a detailed experimental design.

5. Implications and Applications (150-200 words):
   a) Explore potential applications of your model in fields such as cryptography, AI safety, or cognitive science, providing concrete examples.
   b) Discuss how your model might inform our understanding of human language processing or quantum cognition, proposing a specific hypothesis.
   c) Propose a novel research question that arises from your model and outline a potential study to address it.

6. Ethical Considerations (100-150 words):
   a) Identify potential ethical issues or concerns raised by your proposed model, considering both short-term and long-term implications.
   b) Suggest specific guidelines for the responsible development and use of quantum-inspired language models.

Ensure your response demonstrates a deep understanding of quantum mechanics, linguistics, and information theory. Use appropriate technical terminology and provide clear explanations where necessary. Be innovative in your approach while maintaining scientific plausibility. Your total response should be between 1200-1500 words.

Your response will be evaluated based on the following criteria:
1. Accuracy and depth of interdisciplinary knowledge integration.
2. Novelty and plausibility of the proposed quantum-linguistic model.
3. Rigorous mathematical formulation and appropriate use of equations.
4. Quality and entropy-accuracy of the generated text sample.
5. Thoroughness of comparative analysis and experimental design.
6. Insightfulness of proposed applications, implications, and ethical considerations.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response follows the structure specified in the instructions.",
            "The model architecture is well-explained with a rigorous mathematical formulation, including at least two relevant equations using LaTeX notation.",
            "The quantum-linguistic integration is thoroughly analyzed and justified, with a specific formula for calculating textual entropy.",
            "A text sample is generated and analyzed according to the specified parameters, with calculations shown for the target entropy level.",
            "The comparative analysis with classical models includes specific examples and quantitative estimates.",
            "A detailed experimental design is provided for empirically evaluating the model.",
            "Potential implications, applications, and ethical considerations are thoughtfully discussed with concrete examples and a proposed research study.",
            "The response demonstrates a deep understanding of quantum mechanics, linguistics, and information theory, using appropriate technical terminology.",
            "The proposed model is innovative while maintaining scientific plausibility.",
            "The response adheres to the specified word limits and fully addresses all required components."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
