import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_effects = [
            "quantum coherence",
            "quantum entanglement",
            "quantum tunneling",
            "superposition",
            "zero-point energy",
            "quantum beating"
        ]
        photosynthetic_processes = [
            "light harvesting",
            "energy transfer",
            "charge separation",
            "water oxidation",
            "carbon fixation",
            "electron transport"
        ]
        return {
            "1": {
                "quantum_effect": random.choice(quantum_effects),
                "photosynthetic_process": random.choice(photosynthetic_processes)
            },
            "2": {
                "quantum_effect": random.choice(quantum_effects),
                "photosynthetic_process": random.choice(photosynthetic_processes)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design and analyze a hypothetical quantum biological mechanism that could enhance the efficiency of photosynthesis, focusing on the quantum effect of {t['quantum_effect']} in the photosynthetic process of {t['photosynthetic_process']}. Then, propose an experimental setup to test this mechanism. Your response should include:

1. Quantum Biological Mechanism (300-350 words):
   a) Describe your hypothetical quantum biological mechanism and how it incorporates {t['quantum_effect']}.
   b) Explain how this mechanism could enhance the efficiency of {t['photosynthetic_process']}.
   c) Discuss the potential advantages of this mechanism over classical biological processes.
   d) Address any challenges or limitations in the realization of this mechanism in biological systems.

2. Theoretical Framework (250-300 words):
   a) Provide a mathematical or physical model that describes your proposed quantum biological mechanism.
   b) Explain how this model integrates principles from quantum mechanics and biology.
   c) Discuss any assumptions or approximations made in your theoretical framework.

3. Biological Implementation (200-250 words):
   a) Describe how your proposed mechanism could be implemented in a photosynthetic organism.
   b) Discuss any necessary modifications to existing biological structures or processes.
   c) Address potential evolutionary implications of such a mechanism.

4. Experimental Design (250-300 words):
   a) Propose an experimental setup to test your hypothetical quantum biological mechanism.
   b) Describe the equipment, techniques, and methodologies you would use.
   c) Explain how you would isolate and measure the quantum effect in the biological system.
   d) Discuss potential challenges in conducting such an experiment and how you would address them.

5. Predicted Results and Implications (200-250 words):
   a) Describe the expected results if your hypothesis is correct.
   b) Explain how these results would support the presence of your proposed quantum biological mechanism.
   c) Discuss the broader implications of your findings for the field of quantum biology and our understanding of photosynthesis.

6. Future Research Directions (150-200 words):
   a) Suggest two potential applications of your quantum biological mechanism in artificial photosynthesis or other technologies.
   b) Propose two future research directions that could build upon your work.
   c) Discuss any ethical considerations related to the development and application of quantum biological technologies.

Ensure your response demonstrates a deep understanding of quantum mechanics, molecular biology, and biochemistry. Use appropriate scientific terminology and provide clear explanations for complex concepts. Be creative and speculative in your approach while maintaining scientific plausibility and accuracy.

Format your response with clear headings for each section, numbered as above. Use subheadings where appropriate. Your total response should be between 1350-1650 words. Include a word count at the end of your response.

Your response will be evaluated based on scientific accuracy, creativity, coherence, and adherence to the specified format and word count."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response includes a detailed description of a hypothetical quantum biological mechanism incorporating {t['quantum_effect']} in the process of {t['photosynthetic_process']}.",
            "The theoretical framework provides a clear mathematical or physical model of the proposed mechanism.",
            "The biological implementation is plausible and addresses potential evolutionary implications.",
            "The experimental design is well-thought-out and addresses the challenges of isolating quantum effects in biological systems.",
            "The predicted results and implications are logically consistent with the proposed mechanism and experiment.",
            "The response demonstrates creativity and speculation while maintaining scientific plausibility and accuracy.",
            "The overall response showcases a deep understanding of quantum mechanics, molecular biology, and biochemistry within the given word limit.",
            "The response adheres to the specified format and word count requirements."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
