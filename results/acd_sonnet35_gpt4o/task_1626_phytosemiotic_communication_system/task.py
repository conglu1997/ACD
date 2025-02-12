import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        environments = ['rainforest', 'desert', 'tundra', 'coral reef', 'urban ecosystem']
        challenges = ['climate change effects', 'biodiversity loss', 'pollution levels', 'invasive species spread', 'habitat fragmentation']
        
        return {
            "1": {
                "environment": random.choice(environments),
                "challenge": random.choice(challenges)
            },
            "2": {
                "environment": random.choice(environments),
                "challenge": random.choice(challenges)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a communication system inspired by plant signaling mechanisms (phytosemiotics), then apply it to solve a complex environmental monitoring challenge in a {t['environment']} ecosystem, focusing on {t['challenge']}.

Phytosemiotics is the study of sign processes in plants, including how plants communicate with each other and their environment through various chemical, electrical, and mechanical signals.

Your response should include:

1. Phytosemiotic System Design (300-350 words):
   a) Describe the key components and principles of your plant-inspired communication system.
   b) Explain how your system mimics at least three specific plant signaling mechanisms (e.g., volatile organic compounds, electrical signals, hydraulic waves).
   c) Discuss how your system adapts these mechanisms for use in non-plant contexts.
   d) Provide a simple example of how basic information would be encoded and transmitted in your system.

2. Information Theory Analysis (200-250 words):
   a) Analyze the information capacity and efficiency of your phytosemiotic system.
   b) Compare its performance to traditional electronic communication systems in terms of speed, range, and energy efficiency.
   c) Discuss any unique advantages or limitations of your system from an information theory perspective.

3. Environmental Monitoring Application (250-300 words):
   a) Explain how you would apply your phytosemiotic system to monitor {t['challenge']} in a {t['environment']} ecosystem.
   b) Describe the specific sensors or signal generation methods you would use.
   c) Discuss how your system would process and interpret the collected data.
   d) Address any challenges specific to the given environment and how your system overcomes them.

4. Network Architecture (200-250 words):
   a) Design a network architecture for deploying your phytosemiotic system across the {t['environment']} ecosystem.
   b) Explain how individual nodes in the network would communicate and coordinate.
   c) Discuss scalability and resilience features of your network design.

5. Biomimetic Technology Integration (150-200 words):
   a) Propose two novel biomimetic technologies that could enhance your phytosemiotic system.
   b) Explain how these technologies integrate principles from plant biology with modern engineering.
   c) Discuss any potential challenges in developing or implementing these technologies.

6. Ethical and Ecological Considerations (150-200 words):
   a) Analyze potential ecological impacts of deploying your system in the {t['environment']}.
   b) Discuss ethical considerations related to mimicking biological systems for technological purposes.
   c) Propose guidelines for responsible development and use of phytosemiotic technologies.

7. Summary (100-150 words):
   Provide a concise summary of your phytosemiotic communication system, highlighting its key features, advantages, and potential impact on environmental monitoring.

Ensure your response demonstrates a deep understanding of plant biology, information theory, and environmental science. Be innovative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section and number your paragraphs as outlined above. Adhere to the word count guidelines provided for each section. Your total response should be between 1350-1700 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of plant signaling mechanisms and how they can be adapted for a communication system.",
            "The phytosemiotic system design is innovative, well-explained, and scientifically plausible.",
            f"The application to monitoring {t['challenge']} in a {t['environment']} ecosystem is thorough and practical.",
            "The information theory analysis shows a clear understanding of communication system principles.",
            "The network architecture is well-designed and addresses the specific challenges of the given environment.",
            "The proposed biomimetic technologies are innovative and well-integrated with the overall system.",
            "Ethical and ecological considerations are thoughtfully addressed.",
            "The summary effectively synthesizes the key aspects of the proposed system.",
            "The response adheres to the specified format and word count guidelines."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
