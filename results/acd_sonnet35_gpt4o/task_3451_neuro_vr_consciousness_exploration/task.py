import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "altered_state": "Synesthesia",
                "brain_region": "Parietal lobe",
                "perceptual_modality": "Visual-auditory"
            },
            {
                "altered_state": "Out-of-body experience",
                "brain_region": "Temporoparietal junction",
                "perceptual_modality": "Proprioception"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design a virtual reality system that simulates the altered state of consciousness known as {t['altered_state']}, focusing on the {t['brain_region']} and the {t['perceptual_modality']} perceptual modality. Then, use this system to investigate the nature of subjective experience and perception. Your response should include:\n\n1. Neuroscientific Basis (250-300 words):\n   a) Explain the neural mechanisms underlying {t['altered_state']}.\n   b) Describe how the {t['brain_region']} is involved in this altered state.\n   c) Discuss current theories about how this state affects {t['perceptual_modality']} perception.\n\n2. VR System Design (300-350 words):\n   a) Describe the key components of your VR system for simulating {t['altered_state']}.\n   b) Explain how the system will manipulate sensory input to induce the altered state.\n   c) Detail any novel technologies or techniques used in your design.\n   d) Discuss how you ensure user safety and comfort during the experience.\n   e) Provide a brief textual description of a diagram representing your VR system architecture.\n\n3. Experimental Protocol (200-250 words):\n   a) Outline an experiment using your VR system to investigate subjective experience during {t['altered_state']}.\n   b) Describe the participants, procedures, and data collection methods.\n   c) Explain how you will measure and analyze changes in {t['perceptual_modality']} perception.\n\n4. Anticipated Results and Implications (200-250 words):\n   a) Predict potential findings from your experiment and their significance.\n   b) Discuss how these results might contribute to our understanding of consciousness and perception.\n   c) Explore possible implications for cognitive science and philosophy of mind.\n\n5. Ethical Considerations (150-200 words):\n   a) Identify potential ethical concerns related to inducing altered states of consciousness in VR.\n   b) Propose guidelines for responsible use of this technology in research and potential therapeutic applications.\n   c) Discuss the importance of informed consent and debriefing in these experiments.\n\n6. Future Directions (150-200 words):\n   a) Suggest two potential extensions or modifications to your VR system for exploring other aspects of consciousness.\n   b) Discuss how this technology might be applied in clinical settings or for cognitive enhancement.\n   c) Speculate on long-term implications of this research for our understanding of the mind and reality.\n\nEnsure your response demonstrates a deep understanding of neuroscience, virtual reality technology, and consciousness studies. Use appropriate technical terminology and provide clear explanations where necessary. Be innovative in your approach while maintaining scientific plausibility.\n\nFormat your response with clear headings for each section. Your total response should be between 1250-1550 words."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of neuroscience, virtual reality technology, and consciousness studies.",
            "The VR system design is innovative, coherent, and scientifically plausible.",
            "The experimental protocol is well-designed and appropriate for investigating the altered state of consciousness.",
            "The anticipated results and implications are thoughtfully explored and grounded in current scientific understanding.",
            "Ethical considerations are thoroughly addressed, with responsible guidelines proposed.",
            "The response is well-structured, within the specified word count, and uses appropriate technical terminology."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
