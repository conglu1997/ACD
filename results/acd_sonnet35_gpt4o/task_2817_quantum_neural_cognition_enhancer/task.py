import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "cognitive_process": "working memory",
                "quantum_property": "superposition",
                "brain_region": "prefrontal cortex"
            },
            {
                "cognitive_process": "episodic memory retrieval",
                "quantum_property": "entanglement",
                "brain_region": "hippocampus"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a theoretical quantum computing system that models and potentially enhances human cognitive processes, focusing on {t['cognitive_process']} in the {t['brain_region']}. Your system should leverage the quantum property of {t['quantum_property']}. Your response should include the following sections:

1. Quantum-Neural Interface (250-300 words):
   a) Describe the key components of your quantum computing system and how it interfaces with neural processes.
   b) Explain how you utilize {t['quantum_property']} to model or enhance {t['cognitive_process']}.
   c) Discuss the theoretical basis for applying quantum principles to neural computation in the {t['brain_region']}.

2. System Architecture (200-250 words):
   a) Provide a high-level overview of your system's architecture.
   b) Explain how classical and quantum components interact in your design.
   c) Describe any novel algorithms or approaches used in your system.

3. Cognitive Enhancement Mechanism (200-250 words):
   a) Detail how your system could potentially enhance {t['cognitive_process']}.
   b) Explain the theoretical basis for this enhancement.
   c) Discuss potential limitations or risks associated with this approach.

4. Simulation and Validation (150-200 words):
   a) Propose a method to simulate and test your quantum-neural system.
   b) Describe how you would validate its effects on {t['cognitive_process']}.
   c) Discuss potential challenges in translating simulated results to biological systems.

5. Ethical Implications (150-200 words):
   a) Analyze the ethical considerations of enhancing human cognition through quantum computing.
   b) Discuss potential societal impacts of your technology.
   c) Propose guidelines for responsible development and use of quantum-neural cognitive enhancement.

6. Future Research Directions (150-200 words):
   a) Suggest three potential avenues for further research based on your system.
   b) Discuss how your approach might contribute to our understanding of consciousness or intelligence.
   c) Propose a related application of your quantum-neural system outside of cognitive enhancement.

Ensure your response demonstrates a deep understanding of quantum computing, neuroscience, and cognitive science. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1100-1400 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response effectively integrates quantum computing principles, particularly {t['quantum_property']}, with neuroscientific understanding of {t['cognitive_process']} in the {t['brain_region']}.",
            "The proposed system demonstrates a deep understanding of both quantum mechanics and cognitive neuroscience.",
            "The cognitive enhancement mechanism is innovative while maintaining scientific plausibility.",
            "The simulation and validation methods are well-thought-out and address the challenges of quantum-neural integration.",
            "The ethical analysis is thorough and considers multiple perspectives.",
            "The future research directions are insightful and build meaningfully on the proposed system.",
            "The response maintains coherence and logical consistency across all sections.",
            "The proposed quantum-neural system offers a significant theoretical advancement in cognitive modeling or enhancement."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
