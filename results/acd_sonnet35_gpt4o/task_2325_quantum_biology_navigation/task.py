import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                'bird_species': 'European robin',
                'magnetic_field_strength': '50 microTesla',
                'application_domain': 'quantum sensing'
            },
            {
                'bird_species': 'Garden warbler',
                'magnetic_field_strength': '30 microTesla',
                'application_domain': 'quantum computing'
            },
            {
                'bird_species': 'Homing pigeon',
                'magnetic_field_strength': '40 microTesla',
                'application_domain': 'quantum cryptography'
            },
            {
                'bird_species': 'Arctic tern',
                'magnetic_field_strength': '20 microTesla',
                'application_domain': 'quantum metrology'
            }
        ]
        return {str(i+1): scenario for i, scenario in enumerate(random.sample(scenarios, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Analyze the quantum mechanics behind bird navigation in the {t['bird_species']}, design experiments to test the radical pair mechanism, and propose novel applications inspired by this biological quantum phenomenon in the field of {t['application_domain']}. Your response should include:

1. Quantum Biology Analysis (250-300 words):
   a) Explain the radical pair mechanism and its role in avian magnetoreception.
   b) Describe how quantum coherence and entanglement might be involved in this process.
   c) Discuss the challenges of maintaining quantum effects in biological systems.
   d) Analyze how the {t['bird_species']} might use this mechanism for navigation.

2. Experimental Design (300-350 words):
   a) Propose an experiment to test the radical pair mechanism in the {t['bird_species']}.
   b) Describe the methodology, including control groups and variables to be measured.
   c) Explain how you would simulate different magnetic field strengths, including the specified {t['magnetic_field_strength']}.
   d) Discuss potential confounding factors and how you would address them.
   e) Suggest how you would analyze the data to confirm or refute the involvement of quantum effects.

3. Novel Application Proposal (250-300 words):
   a) Based on the radical pair mechanism, propose a novel application in the field of {t['application_domain']}.
   b) Explain how this bio-inspired application would work, drawing clear parallels to avian magnetoreception.
   c) Discuss the potential advantages of this approach over current technologies in the field.
   d) Address any challenges in implementing this application and suggest possible solutions.

4. Quantum-Classical Interface Analysis (200-250 words):
   a) Analyze how the quantum effects in bird navigation interface with classical sensory and neural systems.
   b) Discuss the implications of this interface for our understanding of quantum effects in biological systems.
   c) Propose a theoretical model for how quantum information might be transduced into classical neural signals in birds.

5. Future Research Directions (200-250 words):
   a) Suggest two potential research directions that could further our understanding of quantum biology in avian navigation.
   b) Discuss how advances in this field might impact our broader understanding of quantum effects in biological systems.
   c) Speculate on other biological systems that might employ similar quantum mechanisms.

Ensure your response demonstrates a deep understanding of quantum mechanics, biology, and experimental design. Use appropriate scientific terminology and provide clear explanations for complex concepts. Be creative in your application proposal while maintaining scientific plausibility.

Format your response using clear headings for each section. Your total response should be between 1200-1450 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a clear understanding of the radical pair mechanism and its potential role in {t['bird_species']} navigation.",
            "The experimental design is well-thought-out, addressing potential confounding factors and including appropriate controls.",
            f"The proposed novel application in {t['application_domain']} is creative, feasible, and clearly inspired by avian magnetoreception.",
            "The analysis of the quantum-classical interface in bird navigation is insightful and scientifically sound.",
            "The suggested future research directions are promising and well-justified.",
            "The response balances technical accuracy with clear explanations accessible to a scientifically literate audience.",
            "The response follows the specified format and word count guidelines.",
            f"The experimental design appropriately incorporates the specified magnetic field strength of {t['magnetic_field_strength']} and explains its relevance."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
