import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_effects = [
            "quantum tunneling",
            "quantum coherence",
            "quantum entanglement",
            "superposition"
        ]
        biological_systems = [
            "photosynthesis",
            "magnetoreception",
            "olfaction",
            "enzyme catalysis"
        ]
        information_processes = [
            "genetic encoding",
            "neural signaling",
            "protein folding",
            "cellular communication"
        ]
        return {
            "1": {
                "quantum_effect": random.choice(quantum_effects),
                "biological_system": random.choice(biological_systems),
                "information_process": random.choice(information_processes)
            },
            "2": {
                "quantum_effect": random.choice(quantum_effects),
                "biological_system": random.choice(biological_systems),
                "information_process": random.choice(information_processes)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a theoretical framework that explains how the quantum effect of {t['quantum_effect']} in the biological system of {t['biological_system']} could have influenced the evolution of {t['information_process']} in living organisms. Your response should include:

Executive Summary (100-150 words):
Provide a concise overview of your theoretical framework, highlighting the key aspects of how {t['quantum_effect']} in {t['biological_system']} influences the evolution of {t['information_process']}.

1. Quantum-Biological Mechanism (300-350 words):
   a) Explain the fundamental principles of {t['quantum_effect']} and how it manifests in {t['biological_system']}.
   b) Describe the potential advantages this quantum effect could provide in terms of information processing.
   c) Propose a detailed mechanism by which this quantum effect could enhance or modify {t['information_process']}.
   d) Include at least one equation or formal representation of a key aspect of your proposed mechanism.

2. Evolutionary Trajectory (250-300 words):
   a) Outline a hypothetical evolutionary pathway for the development of quantum-enhanced {t['information_process']}.
   b) Discuss potential selective pressures that could have favored the integration of quantum effects.
   c) Address how this quantum-enhanced process could have led to increased fitness or survival advantage.
   d) Propose a timeline for when this quantum-enhanced process might have emerged in evolutionary history.

3. Information Theoretic Analysis (250-300 words):
   a) Apply principles of information theory to quantify the potential benefits of quantum-enhanced {t['information_process']}.
   b) Compare the information processing capabilities of classical vs. quantum-enhanced biological systems.
   c) Discuss how this quantum enhancement might affect the overall information capacity or efficiency of the organism.
   d) Provide a mathematical expression or model that captures a key information theoretic aspect of your framework.

4. Experimental Predictions (200-250 words):
   a) Propose three testable predictions that would support your theoretical framework.
   b) Describe potential experiments or observations that could validate these predictions.
   c) Discuss any technological or methodological challenges in testing your theory.

5. Implications and Future Directions (200-250 words):
   a) Explore the broader implications of your framework for our understanding of life and evolution.
   b) Discuss how this theory might influence approaches in fields such as synthetic biology or artificial life.
   c) Propose two potential applications that could arise from a deeper understanding of quantum effects in biological information processing.
   d) Suggest future research directions to further develop or validate your theoretical framework.

Ensure your response demonstrates a deep understanding of quantum mechanics, evolutionary biology, and information theory. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility and rigor.

Cite relevant research or theoretical work throughout your response to support your ideas and demonstrate knowledge of current literature in the field. Include 5-7 citations, providing a brief (1-2 sentence) explanation of how each cited work relates to your framework.

Format your response with clear headings for each section and subsections labeled a, b, c, d as appropriate. Your total response should be between 1300-1600 words.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of {t['quantum_effect']}, {t['biological_system']}, and {t['information_process']}, and their potential interactions.",
            "The proposed quantum-biological mechanism is innovative, well-explained, and scientifically plausible.",
            "The evolutionary trajectory is logically sound and considers relevant selective pressures.",
            "The information theoretic analysis is rigorous and applies appropriate mathematical concepts.",
            "The experimental predictions are testable and directly related to the proposed framework.",
            "The implications and future directions show critical thinking about the broader impact of the theory.",
            "The response includes relevant equations, models, or formal representations where appropriate.",
            "The writing is clear, well-structured, and uses appropriate scientific terminology throughout.",
            "The response cites 5-7 relevant research works, providing brief explanations of their relevance to the framework.",
            "The executive summary effectively captures the key aspects of the theoretical framework."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
