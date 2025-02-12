import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "name": "Alien Contact Language Development",
                "agents": ["Human Linguists", "AI Language Models", "Alien Species"],
                "linguistic_features": ["Phonology", "Syntax", "Semantics", "Pragmatics"],
                "cognitive_constraints": ["Working Memory Limitations", "Pattern Recognition Biases", "Social Learning Mechanisms"],
                "environmental_factors": ["Limited Communication Channels", "Time Pressure", "Cultural Misunderstandings"],
                "goal": "Develop a functional intergalactic communication system"
            },
            {
                "name": "Post-Apocalyptic Language Reconstruction",
                "agents": ["AI Language Preservers", "Human Survivors", "Emergent Subcultures"],
                "linguistic_features": ["Lexicon", "Grammar", "Orthography", "Discourse"],
                "cognitive_constraints": ["Memory Degradation", "Cognitive Load", "Emotional Trauma"],
                "environmental_factors": ["Limited Resources", "Geographical Isolation", "Technological Regression"],
                "goal": "Reconstruct and adapt language for post-apocalyptic society"
            }
        ]
        return {
            "1": random.choice(scenarios),
            "2": random.choice(scenarios)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design and analyze an AI-driven simulation of language evolution based on the following scenario:\n\nScenario: {t['name']}\n\nAgents: {', '.join(t['agents'])}\nLinguistic Features: {', '.join(t['linguistic_features'])}\nCognitive Constraints: {', '.join(t['cognitive_constraints'])}\nEnvironmental Factors: {', '.join(t['environmental_factors'])}\nGoal: {t['goal']}\n\nYour task:\n\n1. Simulation Design (250-300 words):\n   Describe the key components and mechanics of your language evolution simulation. Explain how the agents interact, how linguistic features are modeled and evolve, and how cognitive constraints and environmental factors influence the system. Include at least one innovative feature that makes your simulation unique.\n\n2. AI Language Learning Model (200-250 words):\n   Propose an AI model for language learning and adaptation within your simulation. Explain its architecture, learning mechanisms, and how it interacts with the evolving language system. Discuss how this model differs from traditional natural language processing approaches.\n\n3. Linguistic Theory Application (200-250 words):\n   Analyze how your simulation incorporates and tests specific linguistic theories or hypotheses about language evolution. Discuss at least two competing theories and how your simulation might provide insights into their validity.\n\n4. Emergent Phenomena (150-200 words):\n   Predict and explain two emergent linguistic phenomena that might arise in your simulation. Discuss how these phenomena relate to real-world language evolution and acquisition processes.\n\n5. Evaluation Metrics (150-200 words):\n   Design a set of quantitative and qualitative metrics to evaluate the success of your simulation in achieving the specified goal. Explain how these metrics capture the complexity of language evolution and the effectiveness of the developed communication system.\n\n6. Ethical and Societal Implications (150-200 words):\n   Discuss the potential ethical considerations and societal impacts of your language evolution simulation. Consider issues such as linguistic diversity, AI influence on human language, and potential applications or misuse of the technology.\n\n7. Future Research Directions (100-150 words):\n   Propose two ways your simulation could be extended or improved in future research. Consider both technological advancements and potential new discoveries in linguistics or cognitive science.\n\nEnsure your response demonstrates a deep understanding of linguistics, cognitive science, and artificial intelligence. Use technical terminology appropriately and provide explanations where necessary. Be creative in your approach while maintaining scientific plausibility.\n\nFormat your response using clear headings for each section, exactly as numbered above. Your total response should be between 1200-1550 words.\n"

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The simulation design is comprehensive, innovative, and integrates linguistic features, cognitive constraints, and environmental factors effectively.",
            "The proposed AI language learning model demonstrates a clear understanding of both AI and linguistic principles.",
            "The application of linguistic theories is well-reasoned and demonstrates a deep understanding of language evolution concepts.",
            "The predicted emergent phenomena are plausible and insightfully connected to real-world language processes.",
            "The evaluation metrics are appropriate and well-designed for assessing the simulation's success and the evolved communication system.",
            "The discussion of ethical and societal implications shows depth of thought and awareness of potential consequences.",
            "The proposed future research directions are innovative and well-grounded in the field.",
            "The overall response demonstrates a strong grasp of linguistics, cognitive science, and artificial intelligence, with creative yet scientifically plausible ideas."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
