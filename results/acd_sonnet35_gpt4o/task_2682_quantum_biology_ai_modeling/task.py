import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_effects = ['quantum tunneling', 'quantum coherence', 'quantum entanglement', 'zero-point energy', 'quantum superposition', 'quantum decoherence', 'quantum discord']
        biological_processes = ['photosynthesis', 'enzyme catalysis', 'DNA mutation', 'magnetoreception', 'olfaction', 'protein folding', 'cellular signaling']
        ai_techniques = ['quantum neural networks', 'quantum-inspired algorithms', 'hybrid quantum-classical models', 'quantum annealing', 'variational quantum circuits', 'quantum reservoir computing', 'quantum Boltzmann machines']
        
        return {
            "1": {
                "quantum_effect": random.choice(quantum_effects),
                "biological_process": random.choice(biological_processes),
                "ai_technique": random.choice(ai_techniques)
            },
            "2": {
                "quantum_effect": random.choice(quantum_effects),
                "biological_process": random.choice(biological_processes),
                "ai_technique": random.choice(ai_techniques)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that models quantum effects in biological processes, apply it to solve a complex biological problem, critically analyze its limitations and alternatives, and discuss its societal impacts. Your system should focus on the quantum effect of {t['quantum_effect']} in the biological process of {t['biological_process']}, using the AI technique of {t['ai_technique']}. Your response should include:

1. Quantum Biology Framework (250-300 words):
   a) Explain the chosen quantum effect and its relevance to the biological process.
   b) Describe current scientific understanding of this quantum biological phenomenon.
   c) Discuss challenges in studying and modeling this quantum biological system.

2. AI System Design (300-350 words):
   a) Outline the architecture of your AI system for modeling quantum biological effects.
   b) Explain how you integrate {t['ai_technique']} into your system.
   c) Describe how your system represents and simulates quantum and biological components.
   d) Discuss any novel algorithms or techniques you've developed for this integration.

3. Problem Application (250-300 words):
   a) Present a specific, complex biological problem that your system could address.
   b) Explain how your AI system would approach and potentially solve this problem.
   c) Provide a detailed case study or example of your system applied to this problem.
   d) Describe expected outputs or insights from your system.
   e) Discuss how these results could advance our understanding of quantum biology.

4. Validation and Verification (200-250 words):
   a) Propose methods to validate your AI system's predictions or outputs.
   b) Discuss potential experiments to verify the quantum biological effects modeled by your system.
   c) Address challenges in empirically testing quantum effects in biological systems.

5. Critical Analysis (200-250 words):
   a) Discuss potential limitations or drawbacks of your proposed system.
   b) Compare your approach with a hypothetical alternative that uses a different quantum effect or AI technique.
   c) Analyze the trade-offs between your approach and the alternative.

6. Societal and Ethical Implications (200-250 words):
   a) Analyze potential societal impacts of your system, both positive and negative.
   b) Discuss ethical considerations in developing AI systems that model fundamental biological processes.
   c) Propose guidelines for responsible development and use of quantum biology AI systems.

7. Future Directions (100-150 words):
   a) Propose future research directions or extensions of your system.
   b) Discuss potential interdisciplinary collaborations that could further this field.

Ensure your response demonstrates a deep understanding of quantum physics, biology, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific accuracy and plausibility. Support your ideas with references to current research where applicable.

Format your response with clear headings for each section. Your total response should be between 1500-1850 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a clear understanding of {t['quantum_effect']} and its potential role in {t['biological_process']}.",
            f"The AI system design effectively integrates {t['ai_technique']} for modeling quantum biological effects.",
            "The approach to solving a complex biological problem using the designed system is well-explained, with a concrete case study or example provided.",
            "The proposed validation and verification methods are appropriate and comprehensive.",
            "The critical analysis demonstrates a thorough understanding of the system's limitations and provides a meaningful comparison with an alternative approach.",
            "The discussion of societal and ethical implications shows deep consideration of the broader impacts of the proposed system.",
            "The response is well-structured, coherent, and adheres to the specified word limits.",
            "The response demonstrates scientific accuracy and innovation, supported by references to current research where applicable.",
            "The proposed future directions and potential collaborations are insightful and relevant to advancing the field."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
