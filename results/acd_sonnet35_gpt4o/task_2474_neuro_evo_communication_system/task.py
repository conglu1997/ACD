import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "environment": "Deep sea",
                "constraints": "High pressure, limited visibility, need for long-range communication",
                "inspiration": "Bioluminescence and electrical signaling in marine organisms"
            },
            {
                "environment": "Dense urban area",
                "constraints": "Electromagnetic interference, privacy concerns, high information density",
                "inspiration": "Swarm intelligence and stigmergy in social insects"
            }
        ]
        
        task = {"scenario": random.choice(scenarios)}
        return {"1": task, "2": task}

    @staticmethod
    def get_instructions(t: dict) -> str:
        scenario = t["scenario"]
        return f"Design a novel communication system inspired by neuroscience, information theory, and evolutionary biology principles for the following scenario: {scenario['environment']}. Your system should address the given constraints: {scenario['constraints']}. Draw inspiration from {scenario['inspiration']}. Ensure that your design integrates concepts from all three fields: neuroscience, information theory, and evolutionary biology.\n\nYour response should include the following sections:\n\n" \
               f"1. System Architecture (300-350 words):\n" \
               f"   a) Describe the overall structure and components of your communication system.\n" \
               f"   b) Explain how your design incorporates principles from neuroscience, information theory, and evolutionary biology.\n" \
               f"   c) Detail how your system addresses the given constraints and utilizes the inspirational elements.\n" \
               f"   d) Provide a diagram or schematic representation of your system (describe it in words).\n\n" \
               f"2. Information Encoding and Transmission (250-300 words):\n" \
               f"   a) Explain the method of encoding information in your system, drawing parallels to neural coding.\n" \
               f"   b) Describe the transmission mechanism and how it optimizes information flow.\n" \
               f"   c) Discuss how your system handles noise and ensures reliable communication.\n\n" \
               f"3. Adaptive and Evolutionary Features (200-250 words):\n" \
               f"   a) Describe how your system can adapt to changing environmental conditions.\n" \
               f"   b) Explain any self-organizing or emergent properties of your communication network.\n" \
               f"   c) Discuss how your system might evolve over time to improve its efficiency or capabilities.\n\n" \
               f"4. Performance Analysis (200-250 words):\n" \
               f"   a) Propose metrics to evaluate the performance of your communication system.\n" \
               f"   b) Compare your system's theoretical performance to existing communication technologies.\n" \
               f"   c) Identify potential limitations or trade-offs in your design.\n\n" \
               f"5. Practical Applications and Implications (200-250 words):\n" \
               f"   a) Suggest three potential applications of your communication system beyond the given scenario.\n" \
               f"   b) Discuss the ethical implications of implementing such a system.\n" \
               f"   c) Explore how this technology might impact society or scientific understanding.\n\n" \
               f"Ensure your response demonstrates a deep understanding of neuroscience, information theory, and evolutionary biology. Use appropriate technical terminology and provide clear explanations. Be innovative in your approach while maintaining scientific plausibility.\n\n" \
               f"Format your response with clear headings for each section. Use numbered lists or bullet points where appropriate. Cite relevant scientific principles or theories to support your design choices. Your total response should be between 1150-1400 words."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of neuroscience, information theory, and evolutionary biology, with specific references to relevant concepts and principles from all three fields.",
            "The communication system design is innovative, scientifically plausible, and effectively addresses the given constraints and inspirational elements of the specific scenario.",
            "The information encoding and transmission methods are well-explained, draw clear parallels to neural coding, and utilize information theory principles to optimize communication.",
            "The system's adaptive and evolutionary features are thoughtfully designed and explained, showcasing emergent properties and potential for improvement over time in response to environmental changes.",
            "The performance analysis includes relevant and specific metrics, a reasonable comparison to existing technologies, and a critical assessment of limitations and trade-offs.",
            "The practical applications and implications section provides creative yet plausible ideas beyond the given scenario and thoughtfully considers ethical and societal impacts.",
            "The response is well-structured, follows the given format, uses appropriate technical terminology, and adheres to the word count guidelines."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
