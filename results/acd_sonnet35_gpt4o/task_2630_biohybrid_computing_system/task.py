import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        neural_components = [
            {
                "name": "Hippocampal neurons",
                "function": "Memory formation and spatial navigation"
            },
            {
                "name": "Cortical neurons",
                "function": "Higher-order cognitive processing"
            }
        ]
        artificial_components = [
            {
                "name": "Quantum dots",
                "function": "Nanoscale light emission and sensing"
            },
            {
                "name": "DNA-based logic gates",
                "function": "Molecular-scale information processing"
            }
        ]
        return {
            "1": {
                "neural": random.choice(neural_components),
                "artificial": random.choice(artificial_components)
            },
            "2": {
                "neural": random.choice(neural_components),
                "artificial": random.choice(artificial_components)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a hypothetical biohybrid computing system that integrates {t['neural']['name']} with {t['artificial']['name']}. Your task is to create an innovative and scientifically plausible design that leverages the unique properties of both biological and artificial components. Your response should include:

1. System Architecture (250-300 words):
   Describe the overall structure and key components of your biohybrid computing system. Explain how {t['neural']['name']} and {t['artificial']['name']} are integrated and how they interact. Include a diagram or schematic representation of your system (describe it textually).

2. Functional Integration (200-250 words):
   Explain how the biological function of {t['neural']['name']} ({t['neural']['function']}) is leveraged in your system. Describe how this is enhanced or complemented by the artificial function of {t['artificial']['name']} ({t['artificial']['function']}). Discuss any novel emergent properties that might arise from this integration.

3. Information Processing (200-250 words):
   Detail how information is encoded, processed, and transmitted within your biohybrid system. Compare and contrast this with traditional computing paradigms. Explain any unique advantages or challenges in information processing that arise from the biological-artificial integration.

4. Fabrication and Maintenance (150-200 words):
   Propose methods for fabricating your biohybrid system, addressing challenges in interfacing living and non-living components. Discuss how the system would be maintained, including energy requirements and potential degradation issues.

5. Potential Applications (200-250 words):
   Suggest three potential applications of your biohybrid computing system in fields such as medicine, environmental monitoring, or advanced AI. For each application, explain how the unique properties of your system provide advantages over existing technologies.

6. Ethical and Safety Considerations (150-200 words):
   Discuss the ethical implications of creating biohybrid systems that integrate living neural components. Address potential safety concerns and propose guidelines for responsible development and use of such technology.

7. Future Directions and Challenges (150-200 words):
   Identify potential limitations of your current design and suggest avenues for future research and development. Discuss how advances in neuroscience, nanotechnology, or synthetic biology might impact the evolution of biohybrid computing systems.

Ensure your response demonstrates a deep understanding of neuroscience, computer science, and synthetic biology. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative and innovative in your approach while maintaining scientific plausibility.

Format your response using clear headings for each section. Your total response should be between 1300-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a thorough understanding of both the biological and artificial components specified in the task.",
            "The system architecture is innovative, detailed, and scientifically plausible, with clear explanations of how the components are integrated.",
            "The functional integration section provides a logical and creative explanation of how the biological and artificial components complement each other.",
            "The information processing section offers a clear comparison with traditional computing paradigms and identifies unique aspects of the biohybrid system.",
            "Fabrication and maintenance challenges are addressed with plausible solutions.",
            "The potential applications are innovative and well-explained, showcasing the unique advantages of the biohybrid system.",
            "Ethical and safety considerations are thoughtfully addressed.",
            "Future directions and challenges are identified, with reasonable suggestions for further development.",
            "The response shows strong interdisciplinary reasoning, combining insights from neuroscience, computer science, and synthetic biology.",
            "The writing is clear, well-structured, and adheres to the specified word limits for each section."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
