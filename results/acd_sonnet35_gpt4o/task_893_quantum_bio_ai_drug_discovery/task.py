import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'quantum_principle': 'Quantum annealing',
                'ai_technique': 'Reinforcement learning',
                'biological_target': 'Protein folding',
                'constraint': 'Must process at least 10^6 potential drug candidates per second'
            },
            {
                'quantum_principle': 'Quantum entanglement',
                'ai_technique': 'Generative adversarial networks',
                'biological_target': 'Gene expression regulation',
                'constraint': 'Must achieve 99.9% accuracy in predicting drug-target interactions'
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a hypothetical drug discovery system that integrates quantum computing, artificial intelligence, and synthetic biology principles. Your system should utilize the quantum principle of {t['quantum_principle']}, the AI technique of {t['ai_technique']}, and target the biological process of {t['biological_target']}. Additionally, your system {t['constraint']}.

Provide your response in the following format, using clear headings for each section:

1. System Architecture (250-300 words):
   a) Describe the main components of your drug discovery system.
   b) Explain how quantum computing, AI, and synthetic biology are integrated.
   c) Provide a detailed flowchart of your system's architecture, including at least 5 major components and their interactions.

2. Quantum Computing Integration (200-250 words):
   a) Explain how {t['quantum_principle']} is utilized in your system.
   b) Describe the advantages this quantum approach offers over classical methods.
   c) Discuss any challenges in implementing this quantum technique and how you address them.
   d) Include at least one quantum algorithm or mathematical formulation.

3. AI Implementation (200-250 words):
   a) Detail how {t['ai_technique']} is applied in your drug discovery process.
   b) Explain how this AI technique complements the quantum and biological aspects.
   c) Describe the data requirements and training process for your AI component.
   d) Provide a specific example of how the AI makes decisions in the drug discovery pipeline.

4. Biological Target Analysis (200-250 words):
   a) Analyze how your system approaches the {t['biological_target']} process.
   b) Explain how quantum computing and AI synergize to address this biological target.
   c) Discuss potential breakthroughs your system might achieve in this area.
   d) Include a specific example of how your system would handle a challenging aspect of this biological process.

5. Drug Candidate Evaluation (150-200 words):
   a) Describe how your system evaluates and ranks potential drug candidates.
   b) Explain any novel metrics or criteria used in this evaluation process.
   c) Discuss how your system balances computational predictions with biological relevance.
   d) Provide a hypothetical scoring system for drug candidates, including at least three criteria.

6. Ethical Considerations and Limitations (150-200 words):
   a) Identify potential ethical issues arising from your proposed system.
   b) Discuss limitations of your approach and areas for future improvement.
   c) Propose guidelines for responsible use of this technology in drug discovery.
   d) Suggest a specific safeguard or protocol to address one of the ethical concerns you've identified.

7. Interdisciplinary Implications (100-150 words):
   a) Discuss how your system might impact fields beyond drug discovery.
   b) Propose a potential application of your system in a different scientific domain.
   c) Briefly describe how your system could be adapted for this new application.

Ensure your response demonstrates a deep understanding of quantum computing, artificial intelligence, and molecular biology. Use appropriate scientific terminology and provide explanations where necessary. Be innovative in your approach while maintaining scientific plausibility. Your total response should be between 1250-1600 words.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of quantum computing, artificial intelligence, and molecular biology.",
            "The system architecture is well-designed, clearly integrates quantum computing, AI, and synthetic biology, and includes a detailed flowchart with at least 5 major components.",
            "The quantum computing integration is well-explained, justified, and includes at least one quantum algorithm or mathematical formulation.",
            "The AI implementation is appropriate, well-integrated with other components, and includes a specific example of AI decision-making in the drug discovery pipeline.",
            "The biological target analysis is thorough, demonstrates understanding of the relevant processes, and includes a specific example of handling a challenging aspect.",
            "The drug candidate evaluation process is logical, well-explained, and includes a hypothetical scoring system with at least three criteria.",
            "Ethical considerations and limitations are thoughtfully discussed, with a specific safeguard or protocol proposed.",
            "Interdisciplinary implications are insightful, well-reasoned, and include a brief description of adapting the system for a new application.",
            "The response is creative and innovative while maintaining scientific plausibility.",
            "The response adheres to the specified format with clear headings for each section.",
            "The total word count is between 1250-1600 words.",
            f"The proposed system addresses the given constraint: {t['constraint']}."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
