import random
import networkx as nx

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = {
            'social': 'A social media platform during a viral misinformation campaign',
            'biological': 'A cellular signaling network responding to a new pathogen',
            'technological': 'A smart city\'s interconnected infrastructure during a natural disaster',
            'economic': 'A global supply chain network facing trade restrictions',
            'ecological': 'A forest ecosystem affected by climate change'
        }
        objectives = ['increase_resilience', 'optimize_information_flow', 'reduce_cascading_failures', 'enhance_adaptability', 'maximize_efficiency']
        constraints = ['limited_resources', 'ethical_considerations', 'time_sensitivity', 'regulatory_restrictions', 'environmental_impact']
        
        tasks = [
            {
                'network_type': random.choice(list(scenarios.keys())),
                'scenario': scenarios[random.choice(list(scenarios.keys()))],
                'objective': random.choice(objectives),
                'constraint': random.choice(constraints),
                'nodes': random.randint(50, 200),
                'edge_probability': round(random.uniform(0.05, 0.2), 2)
            } for _ in range(2)
        ]
        
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Analyze and modify a complex adaptive {t['network_type']} network to {t['objective']}, while considering {t['constraint']}. The network has {t['nodes']} nodes with an edge probability of {t['edge_probability']}. The specific scenario is: {t['scenario']}.

A complex adaptive network is a system of interconnected components that can adapt and evolve in response to changes in their environment. These networks exhibit emergent behaviors that arise from the interactions of their components.

Provide your response in the following format:

1. Network Analysis (250-300 words):
   a) Describe the key characteristics and potential emergent behaviors of the given network type in the specified scenario.
   b) Explain how the network's structure might influence its behavior related to the given objective.
   c) Identify potential challenges or opportunities presented by the network's properties.
   d) Discuss potential trade-offs between different network properties (e.g., efficiency vs. resilience) relevant to the scenario.
   e) Provide a simple diagram or text-based visualization of the network structure.

2. Intervention Strategy (300-350 words):
   a) Propose three distinct interventions to achieve the specified objective.
   b) For each intervention, explain its mechanism of action and expected impact on the network.
   c) Discuss how each intervention addresses or is limited by the given constraint.
   d) Compare your proposed interventions with a baseline or alternative approach.
   e) Discuss the scalability of your interventions for larger or more complex networks.

3. Quantitative Assessment (200-250 words):
   a) Define two quantitative metrics to evaluate the success of your interventions.
   b) Explain how you would calculate these metrics using network properties or simulations.
   c) Describe the expected changes in these metrics after implementing your interventions.

4. Implementation Plan (200-250 words):
   a) Outline a step-by-step plan to implement your most promising intervention.
   b) Discuss potential risks or unintended consequences of your chosen intervention.
   c) Propose a monitoring strategy to track the network's response to the intervention.
   d) Explain how you would validate the effectiveness of your intervention in the given scenario.

5. Adaptive Management (200-250 words):
   a) Describe how you would adjust your intervention strategy based on the network's response.
   b) Explain how you would handle unexpected emergent behaviors or cascading effects.
   c) Propose a long-term strategy for maintaining the desired network state.
   d) Discuss how your adaptive management approach considers the specific challenges of the given scenario.

Ensure your response demonstrates a deep understanding of complex adaptive networks, systems thinking, and the specific domain of the given network type and scenario. Be creative in your approach while maintaining scientific plausibility and considering ethical implications.

Your total response should be between 1150-1400 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of {t['network_type']} networks and their emergent behaviors in the context of {t['scenario']}.",
            f"The proposed interventions are creative, well-reasoned, and directly address the objective to {t['objective']}.",
            f"The quantitative assessment metrics are appropriate and well-explained.",
            f"The implementation plan and adaptive management strategy adequately consider {t['constraint']} and the specific scenario.",
            "The response shows strong systems thinking and interdisciplinary problem-solving skills.",
            "A simple diagram or visualization of the network structure is provided and accurately represents the described network.",
            "The response includes a thoughtful discussion of trade-offs between network properties and compares proposed interventions with alternatives.",
            "The scalability of interventions and long-term adaptive management strategies are adequately addressed."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
