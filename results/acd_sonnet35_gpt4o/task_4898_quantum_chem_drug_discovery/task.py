import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "target": "SARS-CoV-2 main protease",
                "quantum_method": "Density Functional Theory (DFT)",
                "ml_technique": "Graph Neural Networks"
            },
            {
                "target": "Alzheimer's beta-amyloid proteins",
                "quantum_method": "Ab initio molecular dynamics",
                "ml_technique": "Reinforcement Learning"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum chemistry-based AI system for drug discovery, focusing on {t['target']} as the therapeutic target. Your system should utilize {t['quantum_method']} for molecular simulations and incorporate {t['ml_technique']} for data analysis and prediction. Your response should include:

1. Quantum Chemistry Framework (250-300 words):
   a) Explain how {t['quantum_method']} can be applied to simulate molecular interactions with {t['target']}.
   b) Describe the key quantum mechanical principles your system will leverage for accurate molecular modeling.
   c) Discuss any approximations or assumptions in your quantum chemical approach and their potential impacts.

2. AI System Architecture (250-300 words):
   a) Outline the main components of your AI system, integrating quantum chemistry simulations with {t['ml_technique']}.
   b) Explain how your system will process quantum chemical data to inform drug candidate selection.
   c) Describe how {t['ml_technique']} will be used to enhance the efficiency and accuracy of your drug discovery process.

3. Drug-Target Interaction Modeling (200-250 words):
   a) Detail how your system will model the interaction between potential drug candidates and {t['target']}.
   b) Explain how quantum effects will be accounted for in predicting drug efficacy and side effects.
   c) Discuss any novel approaches in your system for improving the accuracy of drug-target interaction predictions.

4. Data Management and Visualization (200-250 words):
   a) Describe how your system will handle the large datasets generated from quantum chemical simulations.
   b) Propose an innovative method for visualizing complex quantum chemical data to aid in drug candidate selection.
   c) Explain how your data management approach will ensure reproducibility and interpretability of results.

5. Computational Efficiency and Scaling (150-200 words):
   a) Discuss strategies for optimizing the computational efficiency of your quantum chemistry simulations.
   b) Explain how your system could be scaled to screen large libraries of potential drug candidates.
   c) Address any potential bottlenecks in your system and propose solutions.

6. Ethical Considerations and Practical Implementation (150-200 words):
   a) Discuss ethical implications of using AI and quantum chemistry in drug discovery, particularly for {t['target']}.
   b) Propose guidelines for ensuring the responsible development and use of your system.
   c) Describe how your system could be integrated into existing drug discovery pipelines in the pharmaceutical industry.

Ensure your response demonstrates a deep understanding of quantum chemistry, artificial intelligence, and pharmaceutical science. Use appropriate scientific terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1200-1500 words. Include a word count at the end of your response."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of {t['quantum_method']} and its application to drug discovery for {t['target']}.",
            f"The AI system architecture effectively integrates quantum chemistry simulations with {t['ml_technique']}.",
            "The approach to modeling drug-target interactions using quantum effects is well-explained and scientifically plausible.",
            "The data management and visualization strategies are innovative and appropriate for complex quantum chemical data.",
            "The response addresses computational efficiency and scaling challenges in a thoughtful manner.",
            "Ethical considerations and practical implementation aspects are thoroughly discussed.",
            "The response maintains coherence, relevance, and demonstrates creativity throughout all sections.",
            "The response meets the required word count (1200-1500 words) and includes a word count at the end."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
