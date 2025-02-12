import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        environments = [
            {
                "type": "Aquatic",
                "features": ["bioluminescence", "echolocation", "pressure changes"],
                "communication_constraints": "limited visibility, sound propagation in water"
            },
            {
                "type": "Subterranean",
                "features": ["darkness", "limited space", "seismic activity"],
                "communication_constraints": "no light, vibrations through solid medium"
            }
        ]
        return {str(i+1): env for i, env in enumerate(random.sample(environments, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design an AI system that simulates the evolution of language using principles from evolutionary biology. Use this system to evolve a language for a species living in a {t['type']} environment with the following features: {', '.join(t['features'])}. Consider the communication constraints: {t['communication_constraints']}. Your response should include:\n\n1. AI System Architecture (250-300 words):\n   a) Describe the key components of your AI system for language evolution.\n   b) Explain how you incorporate evolutionary algorithms and linguistic principles.\n   c) Discuss how your system models the given environmental features and communication constraints.\n\n2. Language Evolution Process (200-250 words):\n   a) Outline the steps in your language evolution simulation.\n   b) Explain how environmental pressures influence language development in your model.\n   c) Describe how you measure and select for communicative fitness in the evolving language.\n\n3. Evolved Language Features (200-250 words):\n   a) Present 3-5 key features of the evolved language, explaining how they address the environmental context.\n   b) Provide examples of evolved words or phrases, including their meanings and etymologies.\n   c) Explain any novel grammatical structures that emerged during the evolution process.\n\n4. Comparative Analysis (150-200 words):\n   a) Compare your evolved language to existing natural languages from similar environments.\n   b) Discuss any surprising or counterintuitive features that emerged.\n   c) Analyze how closely the evolved language matches theoretical predictions about language evolution.\n\n5. Implications and Applications (200-250 words):\n   a) Discuss what your simulation reveals about the nature of language evolution.\n   b) Explore potential applications of your system in linguistics, AI, or other fields.\n   c) Consider ethical implications of simulating language evolution and potential misuse of such technology.\n\nEnsure your response demonstrates a deep understanding of evolutionary biology, linguistics, and AI principles. Use appropriate terminology and provide clear explanations for complex concepts. Be creative in your approach while maintaining scientific plausibility."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of evolutionary biology, linguistics, and AI principles.",
            "The AI system architecture is well-designed and incorporates both evolutionary algorithms and linguistic principles.",
            "The language evolution process is clearly explained and accounts for the given environmental features and communication constraints.",
            "The evolved language features are creative, plausible, and well-suited to the specified environment.",
            "The comparative analysis shows insight into both natural and evolved languages.",
            "The implications and applications section demonstrates critical thinking about the broader impacts of the work.",
            "The overall response is creative, scientifically plausible, and well-structured."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
