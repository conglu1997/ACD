import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_principles = ['superposition', 'entanglement']
        linguistic_features = ['semantic ambiguity', 'syntactic recursion']
        tasks = [
            {
                'quantum_principle': random.choice(quantum_principles),
                'linguistic_feature': random.choice(linguistic_features),
                'cognitive_process': 'working memory'
            },
            {
                'quantum_principle': random.choice(quantum_principles),
                'linguistic_feature': random.choice(linguistic_features),
                'cognitive_process': 'attention'
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum-inspired model of language comprehension that integrates the quantum principle of {t['quantum_principle']}, the linguistic feature of {t['linguistic_feature']}, and the cognitive process of {t['cognitive_process']}. Your response should include:

1. Theoretical Framework (300-350 words):
   a) Explain how the specified quantum principle can be analogously applied to language processing.
   b) Describe how this quantum-inspired approach interacts with the given linguistic feature.
   c) Discuss how the cognitive process is incorporated into your model.
   d) Propose a novel hypothesis about language comprehension that emerges from this integration.

2. Model Architecture (250-300 words):
   a) Describe the key components of your quantum-inspired language comprehension model.
   b) Explain how information is represented and processed in your model.
   c) Detail how your model accounts for the specified linguistic feature and cognitive process.
   d) Discuss any novel computational or representational elements in your design.

3. Simulated Experiment (200-250 words):
   a) Propose an experiment to test your model's predictions about language comprehension.
   b) Describe the experimental setup, including stimuli and measurement techniques.
   c) Explain how the results would support or refute your model.
   d) Discuss potential challenges in implementing this experiment and how they might be addressed.

4. Neuroscientific Implications (200-250 words):
   a) Suggest how your model might relate to current understanding of brain function.
   b) Propose a neuroimaging study that could provide evidence for your model.
   c) Discuss potential implications of your model for theories of consciousness or cognitive architecture.

5. Computational Implementation (150-200 words):
   a) Outline an approach for implementing a simplified version of your model in a classical computing environment.
   b) Discuss the limitations of this implementation and how true quantum computing might overcome them.
   c) Propose a novel quantum algorithm or data structure inspired by your model.

6. Ethical Considerations and Future Directions (150-200 words):
   a) Discuss potential ethical implications of your model, if it were to accurately represent human language comprehension.
   b) Propose two future research directions that could further develop or test your model.
   c) Speculate on how your model might influence the development of AI language processing systems.

Ensure your response demonstrates a deep understanding of quantum mechanics, linguistics, cognitive science, and neuroscience. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1250-1550 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of quantum mechanics, linguistics, cognitive science, and neuroscience.",
            "The proposed model creatively and plausibly integrates the specified quantum principle, linguistic feature, and cognitive process.",
            "The theoretical framework presents a novel and well-reasoned hypothesis about language comprehension.",
            "The model architecture is clearly described and incorporates innovative elements.",
            "The simulated experiment is well-designed and directly tests the model's predictions.",
            "The neuroscientific implications are thoughtfully explored and connected to current research.",
            "The computational implementation approach is feasible and addresses limitations appropriately.",
            "Ethical considerations are thoroughly discussed, and future research directions are insightful.",
            "The response shows strong interdisciplinary integration and creative problem-solving.",
            "The writing is clear, well-structured, and adheres to the specified word limits."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
