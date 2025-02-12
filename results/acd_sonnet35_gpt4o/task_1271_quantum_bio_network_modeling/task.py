class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "biological_network": "Gene regulatory networks",
                "quantum_algorithm": "Quantum annealing",
                "analysis_goal": "Identify key regulatory hubs and potential drug targets"
            },
            "2": {
                "biological_network": "Protein-protein interaction networks",
                "quantum_algorithm": "Quantum walk",
                "analysis_goal": "Predict protein complex formation and functional modules"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum-inspired system for modeling and analyzing complex biological networks, integrating principles from quantum computing, systems biology, and information theory. Your task focuses on {t['biological_network']}, using the quantum-inspired algorithm {t['quantum_algorithm']} to {t['analysis_goal']}.

Provide your response in the following format:

1. Quantum-Biological Interface (250-300 words):
   a) Explain how you will represent {t['biological_network']} using quantum-inspired data structures.
   b) Describe how {t['quantum_algorithm']} can be adapted to process this biological data.
   c) Discuss any challenges in mapping biological concepts to quantum-inspired algorithms and how you address them.

2. System Architecture (200-250 words):
   a) Outline the key components of your quantum-inspired biological network modeling system.
   b) Explain how these components interact to process the network data and achieve the analysis goal.
   c) Describe any novel techniques or algorithms you would employ in your system.

3. Analysis and Interpretation (250-300 words):
   a) Detail the process by which your system would {t['analysis_goal']}.
   b) Explain how quantum-inspired computations enhance this analysis compared to classical approaches.
   c) Describe how you would validate the results of your quantum-inspired analysis.

4. Biological Insights (200-250 words):
   a) Discuss the potential biological insights that could be gained from your quantum-inspired approach.
   b) Explain how these insights might contribute to our understanding of {t['biological_network']}.
   c) Propose a hypothesis that could be tested using the results of your analysis.

5. Limitations and Future Directions (150-200 words):
   a) Identify potential limitations of your quantum-inspired approach to biological network analysis.
   b) Suggest ways to address these limitations in future iterations of your system.
   c) Propose one potential application of your system beyond the current analysis goal.

Ensure your response demonstrates a deep understanding of quantum computing principles, systems biology, and information theory. Be innovative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations where necessary.

Your total response should be between 1050-1300 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response addresses all required sections with appropriate word counts.",
            "The proposed system demonstrates a clear understanding of quantum computing, systems biology, and information theory.",
            "The approach is innovative and scientifically plausible.",
            "The quantum-inspired algorithms and biological network representations are well-explained and appropriate for the given scenario.",
            "The potential biological insights and future directions are thoughtfully addressed."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
