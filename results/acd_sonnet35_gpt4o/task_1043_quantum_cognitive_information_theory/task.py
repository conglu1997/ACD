import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_principles = ['Superposition', 'Entanglement', 'Quantum tunneling']
        cognitive_processes = ['Memory formation', 'Decision making', 'Attention']
        information_concepts = ['Shannon entropy', 'Kolmogorov complexity', 'Fisher information']
        
        tasks = [
            {
                'quantum_principle': random.choice(quantum_principles),
                'cognitive_process': random.choice(cognitive_processes),
                'information_concept': random.choice(information_concepts)
            },
            {
                'quantum_principle': random.choice(quantum_principles),
                'cognitive_process': random.choice(cognitive_processes),
                'information_concept': random.choice(information_concepts)
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a theoretical framework that integrates quantum mechanics, cognitive science, and information theory to explain consciousness and information processing in the brain. Your framework should focus on the quantum principle of {t['quantum_principle']}, the cognitive process of {t['cognitive_process']}, and the information theory concept of {t['information_concept']}. Provide your response in the following format:

1. Theoretical Framework (300-350 words):
   a) Describe the key components of your framework and how they integrate the three specified concepts.
   b) Explain how your framework accounts for the emergence of consciousness from underlying neural processes.
   c) Discuss how the specified quantum principle might influence or explain the given cognitive process.
   d) Describe how the information theory concept relates to both the quantum and cognitive aspects of your framework.

2. Mathematical Formulation (200-250 words):
   a) Provide a mathematical representation of a key aspect of your framework.
   b) Explain the variables and equations used in your formulation.
   c) Discuss how this mathematical model captures the integration of quantum, cognitive, and information theory principles.

3. Experimental Predictions (200-250 words):
   a) Propose two testable predictions that your framework makes about brain function or conscious experience.
   b) Describe potential experiments or observations that could validate these predictions.
   c) Discuss any technical challenges in testing these predictions and how they might be overcome.

4. Philosophical Implications (150-200 words):
   a) Analyze how your framework addresses the hard problem of consciousness.
   b) Discuss any implications your theory has for our understanding of free will and decision-making.
   c) Consider how your framework might impact our conception of the relationship between mind and matter.

5. Interdisciplinary Connections (150-200 words):
   a) Explain how your framework could influence or be influenced by at least two other scientific disciplines.
   b) Propose a novel research question at the intersection of your framework and another field of your choice.

Ensure your response demonstrates a deep understanding of quantum mechanics, cognitive science, and information theory. Use appropriate technical terminology and provide clear explanations where necessary. Be creative and speculative in your approach while maintaining scientific plausibility and coherence across all sections of your response.

Format your response with clear headings for each section. Your total response should be between 1000-1250 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of the specified quantum principle, cognitive process, and information theory concept.",
            "The theoretical framework is innovative, coherent, and integrates all three specified concepts.",
            "The mathematical formulation is relevant and accurately represents a key aspect of the framework.",
            "The experimental predictions are testable and logically derived from the framework.",
            "The philosophical implications are well-reasoned and address key questions in consciousness studies.",
            "The interdisciplinary connections are insightful and demonstrate broad scientific understanding.",
            "The overall response shows strong integration of knowledge from quantum mechanics, cognitive science, and information theory.",
            "The response is creative and speculative while maintaining scientific plausibility.",
            "The response adheres to the specified word limits for each section."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
