import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        brain_structures = [
            {
                'structure': 'Hippocampus',
                'function': 'Memory formation and spatial navigation',
                'task': 'Episodic memory retrieval'
            },
            {
                'structure': 'Prefrontal cortex',
                'function': 'Executive functions and decision-making',
                'task': 'Multi-task learning and prioritization'
            },
            {
                'structure': 'Visual cortex',
                'function': 'Visual processing and object recognition',
                'task': 'Scene understanding and object relationships'
            },
            {
                'structure': 'Cerebellum',
                'function': 'Motor control and cognitive functions',
                'task': 'Predictive modeling in sensorimotor tasks'
            }
        ]
        return {str(i+1): structure for i, structure in enumerate(random.sample(brain_structures, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a novel neural network architecture inspired by the {t['structure']} and its function of {t['function']}, then apply it to the cognitive task of {t['task']}. Your response should include:

1. Architectural Design (250-300 words):
   a) Describe the key components of your neural network architecture.
   b) Explain how your design is inspired by the structure and function of the {t['structure']}.
   c) Discuss any novel features or mechanisms in your architecture.
   d) Provide a diagram or detailed description of the network's structure.

2. Neuroscientific Basis (200-250 words):
   a) Explain the current understanding of how the {t['structure']} performs its function of {t['function']}.
   b) Describe how you've translated specific neurobiological principles into your artificial neural network design.
   c) Discuss any simplifications or abstractions you've made in this translation.

3. Implementation for Cognitive Task (250-300 words):
   a) Explain how you would apply your neural network architecture to the task of {t['task']}.
   b) Describe the input and output representations for this task.
   c) Discuss any specific training procedures or learning algorithms you would use.
   d) Explain how the network's structure is particularly suited for this cognitive task.

4. Performance Analysis (200-250 words):
   a) Hypothesize how your network might perform on the {t['task']} compared to traditional neural networks.
   b) Discuss potential advantages and limitations of your approach.
   c) Propose a specific experiment to test your network's performance on this task.

5. Broader Implications (150-200 words):
   a) Discuss how your design might contribute to our understanding of brain function.
   b) Explore potential applications of your architecture beyond the specified cognitive task.
   c) Consider any ethical implications of developing more brain-like AI systems.

Ensure your response demonstrates a deep understanding of neuroscience, artificial neural networks, and cognitive science. Use technical terminology appropriately and provide explanations where necessary. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of the {t['structure']} and its function of {t['function']}.",
            "The proposed neural network architecture is innovative and clearly inspired by the specified brain structure.",
            f"The implementation for the cognitive task of {t['task']} is well-explained and plausible.",
            "The performance analysis and broader implications sections show critical thinking and insight.",
            "The response integrates knowledge from neuroscience, AI, and cognitive science effectively.",
            "The writing is clear, well-structured, and uses appropriate technical terminology."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
