import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        memory_processes = [
            "encoding",
            "consolidation",
            "retrieval"
        ]
        quantum_effects = [
            "superposition",
            "entanglement",
            "quantum tunneling"
        ]
        brain_regions = [
            "hippocampus",
            "prefrontal cortex",
            "amygdala"
        ]
        
        return {
            "1": {
                "memory_process": random.choice(memory_processes),
                "quantum_effect": random.choice(quantum_effects),
                "brain_region": random.choice(brain_regions)
            },
            "2": {
                "memory_process": random.choice(memory_processes),
                "quantum_effect": random.choice(quantum_effects),
                "brain_region": random.choice(brain_regions)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a computational model that simulates quantum effects in biological memory processes, focusing on {t['memory_process']} in the {t['brain_region']}, with emphasis on the role of {t['quantum_effect']}. Your task has the following parts:

1. Model Design (300-350 words):
   a) Describe the key components of your computational model, including how it represents the neural structures in the {t['brain_region']}.
   b) Explain how your model incorporates {t['quantum_effect']} into the {t['memory_process']} process.
   c) Outline the mathematical or computational techniques you would use to simulate these quantum effects in a biological context.

2. Quantum-Classical Interface (200-250 words):
   a) Discuss how your model bridges the quantum and classical regimes in neural information processing.
   b) Explain how your model accounts for decoherence effects in the warm, wet environment of the brain.
   c) Describe any novel emergent properties that arise from the quantum-classical interface in your model.

3. Predictions and Insights (200-250 words):
   a) Describe two specific predictions your model makes about {t['memory_process']} in the {t['brain_region']}.
   b) Explain how these predictions differ from classical neuroscience models.
   c) Discuss the potential implications of these predictions for our understanding of memory and consciousness.

4. Experimental Validation (250-300 words):
   a) Propose two experiments that could test the predictions of your quantum memory model.
   b) For each experiment, describe the methodology, expected results, and how they would support or refute your model.
   c) Discuss any technical challenges in performing these experiments and how they might be overcome.

5. Broader Implications (150-200 words):
   a) Speculate on how quantum effects in memory processes might influence other areas of cognitive science or neurobiology.
   b) Discuss potential applications of your model in fields such as artificial intelligence or neuromorphic computing.
   c) Address any ethical considerations related to the development and use of quantum models of memory and consciousness.

Ensure your response demonstrates a deep understanding of quantum mechanics, neuroscience, and computational modeling. Be creative in your approach while maintaining scientific rigor and plausibility. Use appropriate technical terminology and provide clear explanations for a scientifically literate audience.

Format your response using clear headings for each section. Your total response should be between 1100-1350 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response should clearly incorporate principles from quantum mechanics and neuroscience, specifically focusing on {t['quantum_effect']} in the context of {t['memory_process']} in the {t['brain_region']}.",
            "The proposed computational model should be novel and creative while remaining scientifically plausible.",
            "The response should demonstrate a deep understanding of quantum mechanics, neuroscience, and computational modeling techniques.",
            "All five requested sections should be present and adequately addressed.",
            "The predictions and proposed experiments should be logically consistent with the model design and current scientific knowledge.",
            "The response should show an understanding of the challenges in applying quantum effects to biological systems and propose plausible solutions."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
