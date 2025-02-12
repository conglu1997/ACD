import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        domains = [
            'ethical decision making',
            'scientific discovery'
        ]
        quantum_principles = [
            'quantum entanglement',
            'quantum superposition'
        ]
        tasks = [
            {
                'domain': domain,
                'quantum_principle': principle
            }
            for domain, principle in zip(domains, quantum_principles)
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a theoretical quantum computing system capable of simulating artificial general intelligence (AGI), then use it to explore the implications of quantum-enhanced AGI on {t['domain']}. Your system should incorporate the quantum principle of {t['quantum_principle']}. Provide your response in the following format:

1. Quantum AGI Architecture (300-350 words):
   a) Describe the overall structure of your quantum AGI system.
   b) Explain how it incorporates {t['quantum_principle']} in its design.
   c) Detail how the system achieves general intelligence capabilities.
   d) Discuss any novel quantum operations or gates you've designed for AGI processing.

2. Quantum-Classical Integration (200-250 words):
   a) Explain how quantum and classical components interact in your architecture.
   b) Discuss any challenges in interfacing quantum AGI with classical systems and how you address them.
   c) Describe how your system maintains coherence and manages decoherence.

3. AGI Capabilities and Learning (250-300 words):
   a) Outline the key cognitive capabilities of your quantum AGI system.
   b) Explain how quantum principles enhance the AGI's learning and reasoning processes.
   c) Describe any unique advantages your quantum AGI might have over classical AGI systems.

4. Application to {t['domain']} (250-300 words):
   a) Explain how your quantum AGI system would approach problems in {t['domain']}.
   b) Provide a specific example of how it might outperform classical systems in this domain.
   c) Discuss any ethical considerations or potential risks in applying quantum AGI to this area.

5. Implications and Future Directions (200-250 words):
   a) Discuss the broader implications of quantum-enhanced AGI for society and technology.
   b) Propose two potential future advancements that could result from your quantum AGI system.
   c) Suggest safeguards or guidelines for the responsible development of quantum AGI.

Ensure your response demonstrates a deep understanding of both quantum computing principles and artificial general intelligence concepts. Be innovative in your approach while maintaining scientific plausibility. Avoid purely speculative or fantastical ideas that have no basis in current scientific understanding. Use appropriate technical terminology and provide clear explanations where necessary.

Format your response with clear headings for each section. Your total response should be between 1200-1450 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of both quantum computing and artificial general intelligence.",
            "The quantum AGI architecture is innovative, coherent, and scientifically plausible.",
            "The application to the specified domain is well-reasoned and highlights unique advantages of quantum AGI.",
            "The implications and future directions are insightful and consider both potential benefits and risks.",
            "The response uses appropriate technical terminology and provides clear explanations of complex concepts."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
