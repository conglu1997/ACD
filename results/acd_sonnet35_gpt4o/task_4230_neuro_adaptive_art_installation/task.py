import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        art_forms = [
            {
                "form": "Visual art",
                "brain_region": "Visual cortex",
                "emotional_focus": "Joy"
            },
            {
                "form": "Sound installation",
                "brain_region": "Auditory cortex",
                "emotional_focus": "Serenity"
            }
        ]
        return {
            "1": random.choice(art_forms),
            "2": random.choice(art_forms)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design a neuro-adaptive art installation that responds to viewers' brain activity, focusing on the {t['brain_region']} and the emotion of {t['emotional_focus']}, using the art form of {t['form']}. Your response should include:\n\n1. Conceptual Design (250-300 words):\n   a) Describe the overall concept and aesthetic of your neuro-adaptive art installation.\n   b) Explain how it incorporates real-time brain activity data from viewers.\n   c) Detail how the installation responds to and represents the specified brain region and emotional focus.\n   d) Discuss how the chosen art form enhances the viewer's experience and understanding of their own neural activity.\n\n2. Technical Implementation (250-300 words):\n   a) Describe the brain-computer interface technology you would use to collect neural data.\n   b) Explain how you would process and interpret the brain activity data in real-time.\n   c) Detail the algorithms or AI techniques used to translate neural data into artistic output.\n   d) Discuss any challenges in ensuring the system's responsiveness and accuracy.\n\n3. Neuroscientific Basis (200-250 words):\n   a) Explain the current scientific understanding of the specified brain region and its role in cognition or emotion.\n   b) Discuss how your installation might contribute to or challenge this understanding.\n   c) Describe how your design accounts for individual differences in brain activity.\n\n4. Artistic and Emotional Impact (200-250 words):\n   a) Analyze how your installation might influence the viewer's emotional state or self-awareness.\n   b) Discuss the potential for the installation to create a feedback loop between the viewer's brain activity and the artistic output.\n   c) Explain how your design balances scientific accuracy with artistic expression.\n\n5. Ethical Considerations (150-200 words):\n   a) Identify potential ethical concerns related to collecting and using viewers' brain data.\n   b) Discuss how you would address issues of privacy and informed consent.\n   c) Consider potential unintended consequences of exposing viewers to representations of their own neural activity.\n\n6. Future Implications and Extensions (150-200 words):\n   a) Speculate on how this type of neuro-adaptive art could evolve in the future.\n   b) Suggest two potential applications of this technology beyond the art world.\n   c) Discuss how this installation might contribute to public understanding of neuroscience.\n\nEnsure your response demonstrates a deep understanding of neuroscience, data visualization techniques, and interactive art. Use appropriate terminology from relevant fields, providing clear explanations where necessary. Be creative in your approach while maintaining scientific plausibility.\n\nFormat your response with clear headings for each section. Your total response should be between 1200-1500 words."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of neuroscience, data visualization, and interactive art.",
            f"The design effectively incorporates real-time brain activity data from the {t['brain_region']}.",
            f"The installation convincingly represents and responds to the emotion of {t['emotional_focus']}.",
            f"The chosen art form ({t['form']}) is creatively and effectively utilized in the design.",
            "The technical implementation is well-explained and plausible.",
            "Ethical considerations are thoroughly addressed.",
            "The response is creative and innovative while maintaining scientific plausibility."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
