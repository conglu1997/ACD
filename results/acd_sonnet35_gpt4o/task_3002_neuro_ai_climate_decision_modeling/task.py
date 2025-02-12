import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "decision_context": "Personal transportation choices",
                "brain_region": "Prefrontal cortex",
                "environmental_factor": "Urban air quality",
                "ai_technique": "Reinforcement learning"
            },
            {
                "decision_context": "Corporate sustainability policies",
                "brain_region": "Insular cortex",
                "environmental_factor": "Deforestation rates",
                "ai_technique": "Graph neural networks"
            }
        ]
        return {
            "1": random.choice(scenarios),
            "2": random.choice(scenarios)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design and analyze an AI system that models human decision-making processes related to climate change, incorporating principles from neuroscience, artificial intelligence, and environmental science. Focus on the following scenario:\n\nDecision Context: {t['decision_context']}\nBrain Region: {t['brain_region']}\nEnvironmental Factor: {t['environmental_factor']}\nAI Technique: {t['ai_technique']}\n\nYour response should include the following sections:\n\n1. Neuroscientific Basis (250-300 words):\n   a) Explain the role of the specified brain region in decision-making processes.\n   b) Discuss how this region might influence decisions related to climate change.\n   c) Propose a hypothesis about how environmental factors might affect neural activity in this region.\n\n2. AI System Architecture (300-350 words):\n   a) Design an AI system that models the decision-making process for the given context.\n   b) Explain how your system incorporates the specified AI technique.\n   c) Describe how your model simulates the relevant brain region's function.\n   d) Discuss how environmental data is integrated into your system.\n\n3. Decision Simulation (200-250 words):\n   a) Provide a specific example of how your system would simulate a decision in the given context.\n   b) Explain how the environmental factor influences the simulated decision.\n   c) Compare the AI's decision process to what we know about human decision-making in similar contexts.\n\n4. Ethical Implications (150-200 words):\n   a) Discuss potential ethical concerns related to using AI to model and potentially influence human decision-making about climate change.\n   b) Propose guidelines for the responsible development and use of such systems.\n\n5. Potential Applications (200-250 words):\n   a) Suggest two potential applications of your AI system in addressing climate change challenges.\n   b) Explain how these applications could contribute to climate change mitigation or adaptation strategies.\n   c) Discuss any limitations or potential negative consequences of these applications.\n\n6. Future Research Directions (150-200 words):\n   a) Propose two ways your system could be extended or improved in future research.\n   b) Suggest an experiment that could validate your system's accuracy in modeling human decision-making.\n\nEnsure your response demonstrates a deep understanding of neuroscience, artificial intelligence, and environmental science. Use appropriate technical terminology and provide clear explanations where necessary. Be innovative in your approach while maintaining scientific plausibility.\n\nFormat your response with clear headings for each section, numbered as above. Your total response should be between 1250-1550 words."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of the specified brain region and its role in decision-making.",
            "The AI system architecture effectively incorporates the given AI technique and simulates the relevant brain function.",
            "The decision simulation provides a clear and plausible example of how the system would work in the given context.",
            "The ethical implications are thoughtfully considered, with relevant guidelines proposed.",
            "The potential applications are innovative and clearly related to addressing climate change challenges.",
            "The future research directions are well-reasoned and include a valid experimental proposal.",
            "The overall response shows a strong integration of concepts from neuroscience, AI, and environmental science."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
