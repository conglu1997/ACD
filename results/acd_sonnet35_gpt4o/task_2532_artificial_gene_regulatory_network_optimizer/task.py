import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        network_types = ['feed-forward', 'feedback', 'oscillatory']
        optimization_goals = ['robustness', 'adaptability', 'efficiency']
        environmental_factors = ['temperature fluctuations', 'nutrient availability', 'chemical gradients']
        
        tasks = {
            "1": {
                "network_type": random.choice(network_types),
                "optimization_goal": random.choice(optimization_goals),
                "environmental_factor": random.choice(environmental_factors),
                "num_genes": random.randint(5, 15),
                "num_interactions": random.randint(10, 30)
            },
            "2": {
                "network_type": random.choice(network_types),
                "optimization_goal": random.choice(optimization_goals),
                "environmental_factor": random.choice(environmental_factors),
                "num_genes": random.randint(5, 15),
                "num_interactions": random.randint(10, 30)
            }
        }
        
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that simulates and optimizes artificial gene regulatory networks, incorporating principles from systems biology, evolutionary algorithms, and machine learning. Your system should focus on a {t['network_type']} network type with {t['num_genes']} genes and approximately {t['num_interactions']} interactions, with the primary optimization goal of {t['optimization_goal']}, while considering the environmental factor of {t['environmental_factor']}.

Provide your response in the following format:

1. System Architecture (250-300 words):
   a) Describe the main components of your AI system for simulating and optimizing gene regulatory networks.
   b) Explain how your system integrates principles from systems biology, evolutionary algorithms, and machine learning.
   c) Discuss any novel computational approaches or algorithms you would employ.

2. Gene Regulatory Network Model (200-250 words):
   a) Describe how your system models the {t['network_type']} gene regulatory network with {t['num_genes']} genes and {t['num_interactions']} interactions.
   b) Explain the key parameters and variables in your model.
   c) Discuss how your model incorporates the environmental factor of {t['environmental_factor']}.

3. Optimization Strategy (200-250 words):
   a) Detail your approach to optimizing the network for {t['optimization_goal']}.
   b) Explain how your system balances exploration and exploitation in the optimization process.
   c) Describe how you handle constraints and trade-offs in the optimization.

4. Machine Learning Integration (200-250 words):
   a) Explain how machine learning is used in your system to enhance simulation or optimization.
   b) Describe any specific ML algorithms or techniques you employ and why.
   c) Discuss how your system learns and adapts from simulated data.

5. Performance Evaluation (150-200 words):
   a) Propose methods to evaluate your system's performance in optimizing for {t['optimization_goal']}.
   b) Suggest benchmarks to compare your system against existing approaches in the field.
   c) Discuss the limitations of your approach and potential areas for improvement.

6. Biological Insights and Applications (150-200 words):
   a) Discuss how your system could contribute to our understanding of real biological gene regulatory networks.
   b) Propose potential applications of your system in synthetic biology or medical research.
   c) Speculate on how improved optimization of gene regulatory networks might impact future biotechnology.

7. Ethical Considerations (100-150 words):
   a) Discuss potential ethical implications of using AI to optimize gene regulatory networks.
   b) Address concerns about the impact of such systems on biological research and potential misuse.
   c) Propose guidelines for responsible development and use of this technology.

Ensure your response demonstrates a deep understanding of systems biology, evolutionary algorithms, and machine learning. Be innovative in your approach while maintaining scientific plausibility. Provide specific examples or hypothetical scenarios where appropriate. Your total response should be between 1250-1600 words.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of gene regulatory networks, evolutionary algorithms, and machine learning.",
            f"The system architecture effectively integrates principles from systems biology, evolutionary algorithms, and machine learning for a {t['network_type']} network with {t['num_genes']} genes and approximately {t['num_interactions']} interactions.",
            f"The gene regulatory network model appropriately incorporates the environmental factor of {t['environmental_factor']}.",
            f"The optimization strategy is well-designed for achieving {t['optimization_goal']}.",
            "The machine learning integration is innovative and enhances the system's capabilities.",
            "The performance evaluation methods and benchmarks are appropriate and comprehensive.",
            "The discussion of biological insights and applications is insightful and demonstrates interdisciplinary thinking.",
            "The ethical considerations are thoughtfully addressed and guidelines for responsible development are proposed.",
            "The response is creative and original while maintaining scientific plausibility.",
            "The writing is clear, well-structured, and adheres to the specified word counts and format.",
            "Specific examples or hypothetical scenarios are provided where appropriate."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
