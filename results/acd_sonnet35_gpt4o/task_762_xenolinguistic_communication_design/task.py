import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "alien_type": "gaseous beings",
                "physical_constraint": "communicate through modulations of electromagnetic fields",
                "ethical_concern": "potential cultural misunderstandings"
            },
            {
                "alien_type": "crystalline entities",
                "physical_constraint": "perceive reality in four spatial dimensions",
                "ethical_concern": "unintended technological transfer"
            }
        ]
        return {
            "1": random.choice(scenarios),
            "2": random.choice(scenarios)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a speculative communication system for extraterrestrial intelligence, considering linguistic, physical, and ethical factors. The extraterrestrial species you are designing for are {t['alien_type']} who {t['physical_constraint']}. Your response should include:

1. Communication System Design (250-300 words):
   a) Describe the key components and principles of your communication system.
   b) Explain how your system accounts for the physical constraints of the alien species.
   c) Discuss how your design incorporates universal concepts (e.g., mathematics, physics) to establish common ground.

2. Linguistic Structure (200-250 words):
   a) Outline the basic linguistic elements of your communication system (e.g., syntax, semantics, pragmatics).
   b) Explain how these elements are adapted for the alien species' perception and cognition.
   c) Provide an example of how a simple message would be encoded and transmitted in your system.

3. Physical Implementation (200-250 words):
   a) Describe the physical mechanisms or technologies required to implement your communication system.
   b) Explain how your system overcomes challenges related to interstellar distances and potential signal degradation.
   c) Discuss any novel scientific principles or speculative technologies incorporated in your design.

4. Ethical Considerations (200-250 words):
   a) Analyze the ethical implications of establishing communication with this alien species, particularly focusing on {t['ethical_concern']}.
   b) Discuss potential risks and benefits of interstellar communication for both humanity and the alien species.
   c) Propose guidelines or safeguards to ensure responsible and mutually beneficial communication.

5. Cross-Cultural Communication (150-200 words):
   a) Explain how your system accounts for potential differences in cognitive processes, cultural values, or worldviews.
   b) Discuss strategies for avoiding or resolving misunderstandings that might arise from fundamentally different perspectives.

6. Adaptive Learning (150-200 words):
   a) Describe how your communication system could evolve and improve over time as both parties learn more about each other.
   b) Propose a method for incorporating feedback and adapting the system to increase communication efficiency and accuracy.

Ensure your response demonstrates a deep understanding of linguistics, physics, astrobiology, and ethics. Use appropriate technical terminology and provide explanations where necessary. Be creative in your approach while maintaining scientific plausibility and addressing the unique challenges of interstellar communication.

Your total response should be between 1150-1450 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of linguistics, physics, and ethics.",
            "The communication system design is innovative and well-explained.",
            "The solution addresses the specific physical constraints of the alien species.",
            "The ethical analysis is thorough and considers multiple perspectives.",
            "The response shows creativity while maintaining scientific plausibility."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
