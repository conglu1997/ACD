class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        import random

        environments = [
            {
                "planet_type": "Super-Earth",
                "atmosphere": "Hydrogen-rich",
                "temperature": "Extremely cold"
            },
            {
                "planet_type": "Ocean world",
                "atmosphere": "Dense, methane-based",
                "temperature": "Moderate"
            }
        ]

        communication_modes = [
            "Chemical signals",
            "Bioluminescent patterns",
            "Gravitational wave modulations",
            "Quantum entanglement"
        ]

        tasks = {
            "1": {
                "environment": random.choice(environments),
                "communication_mode": random.choice(communication_modes)
            },
            "2": {
                "environment": random.choice(environments),
                "communication_mode": random.choice(communication_modes)
            }
        }

        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design and analyze a hypothetical alien communication system for a civilization living in the following environment:

        Planet type: {t['environment']['planet_type']}
        Atmosphere: {t['environment']['atmosphere']}
        Temperature: {t['environment']['temperature']}
        Primary mode of communication: {t['communication_mode']}

        Your response should include:

        1. Biological Basis (200-250 words):
           a) Describe the hypothetical alien species' biology, considering the given environment.
           b) Explain how their biology enables or constrains their communication abilities.
           c) Discuss any unique adaptations that might influence their communication system.

        2. Communication System Design (250-300 words):
           a) Detail the structure and components of the alien communication system.
           b) Explain how it utilizes the specified primary mode of communication.
           c) Describe how the system is adapted to the planet's environmental conditions.
           d) Propose a basic 'grammar' or rule set for this communication system.

        3. Message Analysis (200-250 words):
           a) Provide an example 'message' in this alien communication system.
           b) Explain the hypothetical meaning or intent behind this message.
           c) Describe how the message's structure reflects the species' biology and environment.

        4. Decoding Methodology (200-250 words):
           a) Propose a scientific approach to decoding this alien communication system.
           b) Describe the technologies or techniques that might be needed.
           c) Discuss potential challenges in decoding and how they might be overcome.

        5. Response Strategy (150-200 words):
           a) Suggest a method for crafting a response in this alien communication system.
           b) Discuss the ethical considerations of attempting to communicate with this alien civilization.
           c) Propose safeguards to prevent potential misunderstandings or conflicts.

        Ensure your response demonstrates a deep understanding of astrobiology, linguistics, and communication theory. Be creative in your approach while maintaining scientific plausibility. Use clear headings for each section of your response.

        Your entire response should be between 1000-1250 words.
        """

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a clear understanding of astrobiological principles and their application to communication systems.",
            "The proposed alien biology and communication system are creative yet scientifically plausible given the specified environment.",
            "The communication system design is detailed, coherent, and reflects the species' biology and environment.",
            "The decoding methodology and response strategy are well-reasoned and consider potential challenges and ethical implications.",
            "The overall response shows interdisciplinary thinking, combining concepts from biology, physics, linguistics, and communication theory.",
            "The submission adheres to the specified structure and word count guidelines."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
