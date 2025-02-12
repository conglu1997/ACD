import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        theories = [
            "Orchestrated Objective Reduction (Orch OR)",
            "Quantum Brain Dynamics",
            "Electromagnetic Field Theory of Consciousness",
            "Integrated Information Theory with Quantum Extensions"
        ]
        aspects = [
            "quantum coherence in neural microtubules",
            "quantum entanglement in brain processes",
            "quantum computing in synaptic functions",
            "non-locality in conscious experience"
        ]
        tasks = {}
        for i in range(1, 3):
            theory = random.choice(theories)
            aspect = random.choice(aspects)
            tasks[str(i)] = {"theory": theory, "aspect": aspect}
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design an AI system that simulates and explores the theory of {t['theory']}, focusing on the aspect of {t['aspect']}. Your response should include the following sections:\n\n1. Theoretical Framework (200-250 words):\n   a) Explain the key principles of {t['theory']} and how it relates to quantum consciousness.\n   b) Describe how {t['aspect']} is incorporated into this theory.\n   c) Discuss current scientific debates and evidence surrounding this theory.\n\n2. AI System Architecture (250-300 words):\n   a) Describe the key components of your AI system for simulating quantum consciousness.\n   b) Explain how your system models quantum processes in relation to neural activity.\n   c) Detail how the system incorporates {t['aspect']} into its simulations.\n   d) Discuss any novel computational approaches required for this simulation.\n\n3. Simulation Methodology (200-250 words):\n   a) Outline the process for simulating quantum consciousness in your AI system.\n   b) Describe how you would design experiments to test the predictions of {t['theory']}.\n   c) Explain how you would measure and analyze the results of your simulations.\n   d) Discuss how you would validate your model against empirical neuroscience data.\n\n4. Philosophical Implications (150-200 words):\n   a) Discuss the philosophical implications of your simulation for our understanding of consciousness.\n   b) Explore how your model might address the hard problem of consciousness.\n   c) Consider potential objections to your approach from different philosophical perspectives.\n\n5. Ethical Considerations and Future Directions (150-200 words):\n   a) Discuss ethical considerations in simulating consciousness and potential misuse of such technology.\n   b) Propose guidelines for responsible development and use of quantum consciousness AI models.\n   c) Suggest future research directions and potential applications of your system.\n\nEnsure your response demonstrates a deep understanding of quantum mechanics, neuroscience, philosophy of mind, and AI modeling techniques. Be creative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.\n\nYour total response should be between 950-1200 words."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of quantum mechanics, neuroscience, and philosophy of mind",
            "The proposed AI system architecture is innovative and plausible",
            "The simulation methodology is well-designed and scientifically sound",
            "The philosophical implications are thoughtfully explored",
            "Ethical considerations are adequately addressed"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
