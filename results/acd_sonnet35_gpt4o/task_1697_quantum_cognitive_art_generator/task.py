import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_principles = [
            "superposition",
            "entanglement",
            "quantum tunneling",
            "quantum interference"
        ]
        cognitive_processes = [
            "divergent thinking",
            "conceptual blending",
            "analogical reasoning",
            "insight problem solving"
        ]
        art_styles = [
            "abstract expressionism",
            "surrealism",
            "cubism",
            "minimalism"
        ]
        
        tasks = {
            "1": {
                "quantum_principle": random.choice(quantum_principles),
                "cognitive_process": random.choice(cognitive_processes),
                "art_style": random.choice(art_styles)
            },
            "2": {
                "quantum_principle": random.choice(quantum_principles),
                "cognitive_process": random.choice(cognitive_processes),
                "art_style": random.choice(art_styles)
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum computing system that simulates and enhances human creativity for abstract art generation. Your system should incorporate the quantum principle of {t['quantum_principle']}, the cognitive process of {t['cognitive_process']}, and generate art in the style of {t['art_style']}. Provide your response in the following format:

1. Quantum-Cognitive Framework (300-350 words):
   a) Explain how the specified quantum principle can be used to model the given cognitive process.
   b) Describe the quantum circuit or algorithm that would implement this model.
   c) Discuss how this quantum-cognitive model could enhance creative processes beyond classical computing approaches.

2. Art Generation System (250-300 words):
   a) Design a system that uses the quantum-cognitive model to generate abstract art.
   b) Explain how the system translates quantum states or measurements into artistic elements (e.g., shapes, colors, compositions).
   c) Describe how the system incorporates randomness and determinism to balance novelty and coherence in the generated art.

3. Artistic Style Integration (200-250 words):
   a) Explain how your system captures the essence of the specified art style.
   b) Discuss how the quantum-cognitive model might offer unique advantages in generating art in this style.
   c) Provide a hypothetical example of how a specific quantum state might be interpreted in the context of this art style.

4. Technical Implementation (200-250 words):
   a) Outline the key components needed to implement your system (e.g., quantum hardware, classical interfaces, output devices).
   b) Discuss any technical challenges in realizing this system and propose potential solutions.
   c) Suggest how existing quantum computing platforms might be adapted or extended for this purpose.

5. Cognitive and Artistic Implications (200-250 words):
   a) Analyze how this quantum-enhanced creative system might influence human artists and the creative process.
   b) Discuss the potential for this technology to provide new insights into human creativity and cognition.
   c) Explore the philosophical implications of using quantum processes to simulate or enhance human creativity.

6. Ethical Considerations and Future Directions (150-200 words):
   a) Discuss ethical considerations in developing and using quantum-enhanced creative systems.
   b) Propose guidelines for the responsible development and use of such technology in the art world.
   c) Suggest two potential future research directions or applications stemming from this work.

Ensure your response demonstrates a deep understanding of quantum computing principles, cognitive science, and artistic concepts. Be innovative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations where necessary.

Your total response should be between 1300-1600 words. Format your response with clear headings for each section."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of the quantum principle {t['quantum_principle']} and how it can be applied to model the cognitive process of {t['cognitive_process']}",
            f"The art generation system effectively incorporates the style of {t['art_style']} and explains how quantum processes contribute to this style",
            "The technical implementation is plausible and addresses real challenges in quantum computing and art generation",
            "The response shows creative and interdisciplinary thinking in combining quantum computing, cognitive science, and art",
            "The ethical considerations and future directions are thoughtfully explored and relevant to the proposed system"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
