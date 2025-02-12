import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                'environment': 'Dynamic problem-solving in a simulated ecosystem',
                'constraint': 'Energy efficiency',
                'time_scale': '1000 generations'
            },
            {
                'environment': 'Pattern recognition in a noisy sensory landscape',
                'constraint': 'Minimal neural complexity',
                'time_scale': '500 generations'
            }
        ]
        
        tasks = [
            {'scenario': random.choice(scenarios)}
            for _ in range(2)
        ]
        
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design and analyze a hypothetical system for evolving artificial neural networks based on principles of neuroscience and evolutionary biology. Your task is to create a detailed proposal for an Artificial Neural Evolution (ANE) system that simulates the evolution of neural networks over time, incorporating both artificial intelligence and biological concepts.

Scenario:
Environment: {t['scenario']['environment']}
Constraint: {t['scenario']['constraint']}
Time Scale: {t['scenario']['time_scale']}

Your response should include the following sections:

1. System Architecture (300-350 words):
   a) Describe the key components of your ANE system.
   b) Explain how you integrate principles from neuroscience, AI, and evolutionary biology.
   c) Detail the mechanisms for neural network variation, selection, and reproduction.
   d) Discuss how your system addresses the given environmental challenge and constraint.

2. Evolutionary Process (250-300 words):
   a) Outline the steps in your evolutionary algorithm.
   b) Explain how you model neural plasticity and development in your evolving networks.
   c) Describe how you balance exploration (variation) and exploitation (selection) in your system.
   d) Discuss how you handle the specified time scale in your simulation.

3. Performance Metrics and Fitness Function (200-250 words):
   a) Define the key performance metrics for your evolving neural networks.
   b) Explain your fitness function and how it relates to the given environment and constraint.
   c) Describe how you measure and track evolutionary progress over time.

4. Predicted Outcomes and Analysis (250-300 words):
   a) Hypothesize the expected evolutionary trajectory of your neural networks.
   b) Predict potential emergent properties or unexpected adaptations.
   c) Compare your ANE system's potential capabilities to current state-of-the-art AI systems.
   d) Discuss the implications of your results for our understanding of biological neural evolution.

5. Ethical Considerations and Limitations (200-250 words):
   a) Identify potential ethical issues in developing and using ANE systems.
   b) Discuss the implications of creating artificially evolved intelligence.
   c) Propose guidelines for responsible development and use of ANE technology.
   d) Acknowledge limitations of your system and areas for future improvement.

Ensure your response demonstrates a deep understanding of neuroscience, artificial intelligence, and evolutionary biology. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1200-1450 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of neuroscience, AI, and evolutionary biology principles.",
            "The proposed ANE system is innovative, scientifically plausible, and addresses the given scenario appropriately.",
            "The evolutionary process and performance metrics are well-defined and justified.",
            "The analysis of predicted outcomes is insightful and considers emergent properties.",
            "Ethical considerations are thoroughly discussed with thoughtful guidelines proposed."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
