import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_effects = [
            {
                "effect": "quantum coherence",
                "biological_system": "photosynthesis",
                "cognitive_enhancement": "information processing speed"
            },
            {
                "effect": "quantum entanglement",
                "biological_system": "magnetoreception in birds",
                "cognitive_enhancement": "spatial awareness"
            }
        ]
        return {
            "1": random.choice(quantum_effects),
            "2": random.choice(quantum_effects)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that interfaces with and interprets quantum effects in biological systems, then apply it to enhance human cognitive abilities. Focus on the quantum effect of {t['effect']} in the biological system of {t['biological_system']}, with the goal of enhancing human {t['cognitive_enhancement']}. Your response should include the following sections:

1. Quantum-Biological Interface (250-300 words):
   a) Explain the quantum effect and its role in the specified biological system.
   b) Describe how your AI system would detect and interpret this quantum effect.
   c) Discuss any novel technologies or methods your system would employ to interface with biological quantum phenomena.

2. AI System Architecture (250-300 words):
   a) Outline the key components of your AI system for interpreting quantum biological data.
   b) Explain how your system integrates quantum information with classical computing methods.
   c) Describe any unique algorithms or data structures your system uses to process quantum biological information.
   d) Include a brief textual description of a diagram illustrating your system's architecture.

3. Cognitive Enhancement Application (200-250 words):
   a) Explain how your system would apply insights from the quantum biological process to enhance the specified cognitive ability.
   b) Describe the proposed mechanism for this enhancement (e.g., brain-computer interface, targeted neuroplasticity, etc.).
   c) Discuss potential limitations or side effects of this cognitive enhancement.

4. Ethical Considerations (150-200 words):
   a) Identify ethical concerns related to enhancing human cognitive abilities through quantum-biological AI interfaces.
   b) Discuss potential societal impacts of this technology, both positive and negative.
   c) Propose guidelines for the responsible development and use of quantum-biological cognitive enhancement.

5. Scientific Implications (150-200 words):
   a) Discuss how your system might contribute to our understanding of quantum effects in biology.
   b) Explain how this research could impact theories of consciousness or cognitive science.
   c) Propose two potential future research directions stemming from this work.

6. Experimental Validation (200-250 words):
   a) Design an experiment to test the efficacy and safety of your quantum-biological cognitive enhancement system.
   b) Describe the methodology, including control groups and measured outcomes.
   c) Discuss potential challenges in conducting such an experiment and how you would address them.

Ensure your response demonstrates a deep understanding of quantum mechanics, biology, neuroscience, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1200-1500 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response should clearly describe an AI system capable of interfacing with and interpreting the quantum effect of {t['effect']} in {t['biological_system']}.",
            f"The proposed cognitive enhancement application for {t['cognitive_enhancement']} should be logically explained and scientifically plausible.",
            "The response should demonstrate a deep understanding of quantum mechanics, biology, neuroscience, and artificial intelligence.",
            "The ethical considerations and experimental validation sections should be thoughtfully addressed.",
            "The response should use appropriate technical terminology and provide clear explanations for complex concepts.",
            "The proposed system and its applications should be innovative while maintaining scientific plausibility."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
