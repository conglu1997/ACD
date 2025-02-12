import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        vr_environments = [
            "Space exploration simulation",
            "Historical reenactment scenario",
            "Abstract conceptual landscape",
            "Underwater ecosystem"
        ]
        cognitive_principles = [
            "Embodied metaphor theory",
            "Situated cognition",
            "Enactivism",
            "Predictive processing"
        ]
        nlp_challenges = [
            "Multimodal context understanding",
            "Gesture-speech integration",
            "Spatial language processing",
            "Emotional state inference"
        ]
        
        return {
            "1": {
                "environment": random.choice(vr_environments),
                "principle": random.choice(cognitive_principles),
                "challenge": random.choice(nlp_challenges)
            },
            "2": {
                "environment": random.choice(vr_environments),
                "principle": random.choice(cognitive_principles),
                "challenge": random.choice(nlp_challenges)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design a natural language processing system for a virtual reality environment that incorporates principles of embodied cognition. Your task has the following parameters:\n\nVR Environment: {t['environment']}\nCognitive Principle: {t['principle']}\nNLP Challenge: {t['challenge']}\n\nYour response should include the following sections:\n\n1. System Overview (250-300 words):\n   a) Provide a high-level description of your NLP system for the given VR environment.\n   b) Explain how it incorporates the specified cognitive principle.\n   c) Discuss how your system addresses the given NLP challenge.\n   d) Include a simple ASCII diagram illustrating the system's architecture.\n\n2. Embodied Cognition Integration (200-250 words):\n   a) Explain in detail how your system leverages the specified cognitive principle.\n   b) Discuss how this integration enhances language processing in the VR environment.\n   c) Provide an example scenario demonstrating this integration in action.\n\n3. NLP Techniques and Algorithms (200-250 words):\n   a) Describe the core NLP techniques and algorithms used in your system.\n   b) Explain how these techniques are adapted for the VR environment.\n   c) Discuss any novel approaches you've developed to address the given NLP challenge.\n\n4. User Interaction Design (150-200 words):\n   a) Describe how users would interact with your NLP system in the VR environment.\n   b) Explain how the interaction design supports embodied cognition principles.\n   c) Discuss potential challenges users might face and how you'd address them.\n\n5. Technical Implementation (200-250 words):\n   a) Outline the key components needed to implement your system.\n   b) Discuss any specific VR technologies or platforms required.\n   c) Explain how you would handle real-time processing and latency issues.\n\n6. Ethical Considerations and Limitations (150-200 words):\n   a) Discuss potential ethical implications of your system.\n   b) Address privacy concerns related to processing user interactions in VR.\n   c) Identify limitations of your approach and areas for future improvement.\n\n7. Evaluation Methodology (150-200 words):\n   a) Propose a method to evaluate the effectiveness of your system.\n   b) Describe specific metrics you would use to assess performance.\n   c) Suggest an experiment design to compare your system against a baseline.\n\nEnsure your response demonstrates a deep understanding of natural language processing, embodied cognition, and virtual reality technologies. Be innovative in your approach while maintaining scientific and technical plausibility. Use appropriate terminology from all relevant fields and provide explanations where necessary.\n\nFormat your response with clear headings for each section. Your total response should be between 1300-1650 words.\n\nIMPORTANT: Your response should be complete and coherent. Do not include any placeholder text or incomplete sections."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of the specified cognitive principle and its application in the VR environment.",
            "The NLP system design effectively addresses the given NLP challenge in the context of the VR environment.",
            "The proposed system integrates embodied cognition principles in a novel and meaningful way.",
            "The technical implementation is well-thought-out and addresses real-time processing concerns in VR.",
            "The response includes innovative NLP techniques adapted for the VR environment.",
            "Ethical considerations and limitations are thoroughly discussed.",
            "The evaluation methodology is well-designed and includes specific, relevant metrics."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
