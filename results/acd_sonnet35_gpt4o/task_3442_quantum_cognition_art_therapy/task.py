import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cognitive_processes = [
            "Decision Making",
            "Memory Formation",
            "Emotional Regulation",
            "Attention"
        ]
        quantum_principles = [
            "Superposition",
            "Entanglement",
            "Interference",
            "Measurement"
        ]
        art_forms = [
            "Interactive Digital Painting",
            "Virtual Reality Sculpture",
            "Generative Music Composition",
            "Augmented Reality Performance"
        ]
        
        tasks = [
            {
                "cognitive_process": random.choice(cognitive_processes),
                "quantum_principle": random.choice(quantum_principles),
                "art_form": random.choice(art_forms)
            } for _ in range(2)
        ]
        
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum cognition-based art therapy system that uses the quantum principle of {t['quantum_principle']} to model and influence the cognitive process of {t['cognitive_process']} through an interactive {t['art_form']} experience. Your response should include:

1. Theoretical Framework (300-350 words):
   a) Explain how the chosen quantum principle can be applied to model the specified cognitive process.
   b) Describe how this quantum cognitive model differs from classical approaches to understanding {t['cognitive_process']}.
   c) Discuss potential benefits and limitations of using quantum cognition in therapeutic contexts.

2. Art Therapy System Design (350-400 words):
   a) Describe the key components and overall structure of your quantum cognition-based art therapy system.
   b) Explain how the {t['art_form']} experience is designed to interact with and influence the quantum cognitive model.
   c) Detail how the system measures or observes changes in the participant's cognitive state.
   d) Include a simple diagram or flowchart of your system (describe it textually).

3. Interaction Scenario (250-300 words):
   a) Provide a step-by-step description of a typical therapy session using your system.
   b) Explain how the participant's interactions with the {t['art_form']} are interpreted in terms of quantum cognitive states.
   c) Describe how the system provides feedback or adapts the artistic experience based on these interpretations.

4. Therapeutic Outcomes (200-250 words):
   a) Discuss the potential therapeutic benefits of your system for {t['cognitive_process']}.
   b) Explain how the quantum approach might lead to different or enhanced outcomes compared to traditional art therapy.
   c) Propose a method for evaluating the effectiveness of your system in clinical settings.

5. Ethical Considerations (150-200 words):
   a) Discuss potential ethical issues arising from the use of quantum cognition models in therapy.
   b) Address concerns about privacy, consent, and potential unintended consequences of influencing cognitive processes through art.
   c) Propose guidelines for the responsible development and use of quantum cognition-based art therapy systems.

6. Future Developments (150-200 words):
   a) Suggest potential expansions or modifications to your system to address other cognitive processes or incorporate different quantum principles.
   b) Discuss how advancements in quantum computing or neurotechnology might enhance your system in the future.
   c) Propose a novel research question that arises from the intersection of quantum cognition, art therapy, and {t['art_form']}.

Ensure your response demonstrates a deep understanding of quantum mechanics, cognitive science, and art therapy. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative and innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1400-1700 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response should address the specific quantum principle of {t['quantum_principle']}, cognitive process of {t['cognitive_process']}, and art form of {t['art_form']}",
            "The design should clearly integrate principles from quantum mechanics, cognitive science, and art therapy",
            "The response should include all required sections: Theoretical Framework, Art Therapy System Design, Interaction Scenario, Therapeutic Outcomes, Ethical Considerations, and Future Developments",
            "The proposed system should be innovative while maintaining scientific plausibility",
            "The response should demonstrate a deep understanding of quantum mechanics, cognitive science, and art therapy",
            "The discussion should be creative while addressing potential challenges and limitations"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
