import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_principles = [
            "superposition",
            "entanglement",
            "quantum tunneling",
            "wave-particle duality"
        ]
        art_elements = [
            "color theory",
            "composition",
            "texture",
            "form"
        ]
        constraints = [
            "must be generatable in real-time",
            "must be interactive with viewer's quantum measurements",
            "must evolve over time like a quantum system"
        ]
        
        tasks = {}
        for i in range(1, 3):
            tasks[str(i)] = {
                "quantum_principle": random.choice(quantum_principles),
                "art_element": random.choice(art_elements),
                "constraint": random.choice(constraints)
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        quantum_principle_explanations = {
            "superposition": "the ability of a quantum system to exist in multiple states simultaneously",
            "entanglement": "a quantum phenomenon where particles become correlated and share properties regardless of distance",
            "quantum tunneling": "a quantum effect where particles can pass through barriers that classical physics would deem impossible",
            "wave-particle duality": "the concept that quantum entities can exhibit both wave-like and particle-like properties"
        }
        art_element_explanations = {
            "color theory": "the study of how colors interact and influence perception in art",
            "composition": "the arrangement of visual elements in an artwork",
            "texture": "the surface quality or feel of an artwork",
            "form": "the three-dimensional shape and structure of an artwork"
        }
        return f"""Design a quantum computing system that generates abstract visual art representations of quantum states. Your system should specifically incorporate the quantum principle of {t['quantum_principle']} ({quantum_principle_explanations[t['quantum_principle']]}), focus on the visual art element of {t['art_element']} ({art_element_explanations[t['art_element']]}), and operate under the constraint: {t['constraint']}.

Your response should include:

1. System Architecture (250-300 words):
   a) Describe the overall structure of your quantum art generation system.
   b) Explain how it incorporates the specified quantum principle in its design.
   c) Detail how the system will represent and manipulate the given visual art element.
   d) Address how the system design accommodates the given constraint.

2. Quantum-Visual Art Interface (200-250 words):
   a) Explain how your system translates quantum states into visual parameters.
   b) Describe how these parameters are then mapped to artistic expressions.
   c) Discuss any challenges in bridging quantum mechanics and visual arts, and how you address them.

3. Art Generation Algorithm (200-250 words):
   a) Propose a quantum algorithm for generating abstract visual art.
   b) Explain how this algorithm leverages the specified quantum principle.
   c) Describe how the algorithm ensures the output focuses on the given visual art element.
   d) Discuss how the algorithm incorporates principles from both quantum mechanics and art theory.

4. Example Output (150-200 words):
   a) Provide a detailed description of a potential visual art output from your system.
   b) Explain how this output reflects the quantum principle and visual art element.

5. Implications and Applications (200-250 words):
   a) Discuss the potential implications of your system for our understanding of quantum phenomena and visual perception.
   b) Propose two novel applications of your quantum visual art generation system outside of pure artistic creation.
   c) Speculate on how this technology might impact fields such as quantum visualization, art therapy, or quantum education.

6. Limitations and Future Work (100-150 words):
   a) Discuss potential limitations or challenges of your proposed system.
   b) Suggest areas for future research or improvements.

Ensure your response demonstrates a deep understanding of quantum computing principles and visual arts theory. Be innovative in your approach while maintaining scientific plausibility. Your total response should be between 1100-1400 words.

Please format your response with clear headings for each section and number your paragraphs within each section. Adhere to the word count guidelines for each section."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of both quantum mechanics and visual arts theory.",
            "The proposed system effectively incorporates the specified quantum principle and visual art element.",
            "The design is innovative and scientifically plausible.",
            "The response addresses all required sections thoroughly.",
            "The example output is described in detail and clearly reflects the quantum-visual art integration.",
            "The implications and applications discussed are insightful and well-reasoned.",
            f"The system design adequately addresses the given constraint: {t['constraint']}.",
            "The response adheres to the specified word count and formatting guidelines."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
