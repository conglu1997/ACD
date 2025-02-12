import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        biological_phenomena = [
            "Photosynthesis",
            "Magnetoreception in birds",
            "Olfaction (sense of smell)",
            "Enzyme catalysis",
            "DNA mutation repair"
        ]
        quantum_principles = [
            "Quantum tunneling",
            "Quantum coherence",
            "Quantum entanglement",
            "Zero-point energy",
            "Quantum superposition"
        ]
        technology_applications = [
            "Energy harvesting",
            "Quantum sensing",
            "Molecular computing",
            "Quantum cryptography",
            "Nanoscale imaging"
        ]
        
        tasks = [
            {
                "biological_phenomenon": phenom,
                "quantum_principle": principle,
                "technology_application": app
            }
            for phenom in biological_phenomena
            for principle in quantum_principles
            for app in technology_applications
        ]
        
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Develop a theoretical framework explaining {t['biological_phenomenon']} using the quantum mechanics principle of {t['quantum_principle']}, then design a bio-inspired quantum technology for {t['technology_application']} based on this framework. Your response should include the following sections:

1. Quantum Biology Framework (300-350 words):
   a) Explain the current understanding of {t['biological_phenomenon']} in classical biology.
   b) Describe how {t['quantum_principle']} could potentially play a role in this phenomenon.
   c) Develop a theoretical framework that integrates quantum mechanics into the explanation of {t['biological_phenomenon']}.
   d) Discuss any existing evidence or experiments that support or challenge your framework.

2. Experimental Proposal (200-250 words):
   a) Design an experiment to test a key aspect of your quantum biology framework.
   b) Describe the experimental setup, methodology, and expected results.
   c) Discuss potential challenges in conducting this experiment and how they might be overcome.

3. Bio-inspired Quantum Technology (300-350 words):
   a) Based on your framework, propose a novel quantum technology for {t['technology_application']}.
   b) Explain how your technology mimics or draws inspiration from {t['biological_phenomenon']}.
   c) Describe the potential advantages of your bio-inspired approach over existing technologies.
   d) Discuss any challenges in implementing your proposed technology and potential solutions.

4. Interdisciplinary Implications (200-250 words):
   a) Analyze how your framework and proposed technology might impact other scientific fields.
   b) Discuss potential applications of your ideas in medicine, environmental science, or information technology.
   c) Explore how your work might contribute to our understanding of the intersection between quantum mechanics and biology.

5. Ethical Considerations and Societal Impact (150-200 words):
   a) Identify potential ethical issues related to your proposed technology or experimental approach.
   b) Discuss the broader societal implications of advancing our understanding of quantum biology.
   c) Propose guidelines for responsible development and application of quantum biology technologies.

Ensure your response demonstrates a deep understanding of both quantum mechanics and biology. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1150-1400 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a comprehensive understanding of both quantum mechanics and biology, particularly in relation to the specified biological phenomenon and quantum principle.",
            "The proposed quantum biology framework is innovative, scientifically plausible, and well-explained.",
            "The experimental proposal is well-designed and directly tests a key aspect of the proposed framework.",
            "The bio-inspired quantum technology for the specified application is creative, feasible, and clearly linked to the biological phenomenon and quantum principle.",
            "The interdisciplinary implications and ethical considerations are thoughtfully analyzed and discussed.",
            "The overall response is well-structured, clear, and demonstrates strong interdisciplinary knowledge integration and creative problem-solving skills."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0