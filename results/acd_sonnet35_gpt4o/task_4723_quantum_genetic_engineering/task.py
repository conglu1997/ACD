import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'quantum_effect': 'Quantum tunneling',
                'genetic_process': 'DNA repair',
                'application_field': 'Cancer treatment'
            },
            {
                'quantum_effect': 'Quantum coherence',
                'genetic_process': 'Gene expression',
                'application_field': 'Crop yield optimization'
            },
            {
                'quantum_effect': 'Quantum entanglement',
                'genetic_process': 'Protein folding',
                'application_field': 'Drug design'
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a theoretical framework for quantum-assisted genetic engineering, focusing on the quantum effect of {t['quantum_effect']} in the genetic process of {t['genetic_process']}. Analyze its potential applications in {t['application_field']} and discuss the ethical implications. Your response should include:

1. Theoretical Framework (300-350 words):
   a) Explain how {t['quantum_effect']} could influence or be utilized in {t['genetic_process']}.
   b) Describe the key components and mechanisms of your quantum-assisted genetic engineering approach.
   c) Discuss any existing research or theories that support or inspire your framework.
   d) Propose a novel hypothesis about how quantum effects could enhance or alter traditional genetic engineering techniques.

2. Methodology and Implementation (250-300 words):
   a) Outline a detailed experimental setup to test your hypothesis.
   b) Describe the equipment, techniques, and methodologies you would use.
   c) Explain how you would measure and control quantum effects in a biological system.
   d) Discuss potential challenges in implementing your approach and how you would address them.

3. Potential Applications (200-250 words):
   a) Analyze how your quantum-assisted genetic engineering framework could be applied in {t['application_field']}.
   b) Describe specific scenarios or use cases where your approach might offer advantages over classical genetic engineering techniques.
   c) Discuss any limitations or constraints of your approach in this application field.

4. Ethical Implications (200-250 words):
   a) Identify and analyze potential ethical issues arising from the use of quantum-assisted genetic engineering in {t['application_field']}.
   b) Discuss how these ethical concerns might differ from those associated with classical genetic engineering.
   c) Propose guidelines or safeguards for the responsible development and use of this technology.

5. Future Research Directions (150-200 words):
   a) Suggest areas for future research to enhance or validate your quantum-assisted genetic engineering framework.
   b) Discuss how advancements in quantum technologies or genetic engineering might impact the future of this field.
   c) Propose a novel research question that could further explore the intersection of quantum mechanics and genetic engineering.

Ensure your response demonstrates a deep understanding of quantum mechanics, molecular biology, genetic engineering, and ethical reasoning in advanced scientific research. Use appropriate technical terminology and provide clear explanations where necessary. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1100-1350 words.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of quantum mechanics, molecular biology, and genetic engineering.",
            "The theoretical framework is well-developed and clearly integrates quantum effects with genetic processes.",
            "The methodology and implementation section provides a plausible experimental approach.",
            "The potential applications are thoughtfully discussed and relevant to the given field.",
            "The ethical implications are thoroughly analyzed, with consideration of unique issues arising from quantum-assisted genetic engineering.",
            "The response shows innovative thinking and proposes novel ideas while maintaining scientific plausibility.",
            "The writing is clear, well-organized, and uses appropriate scientific terminology.",
            "The response adheres to the specified format and word count requirements."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
