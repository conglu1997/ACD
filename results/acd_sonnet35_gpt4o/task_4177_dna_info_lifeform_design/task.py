import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        info_processes = [
            "error correction",
            "data compression",
            "encryption",
            "signal amplification"
        ]
        bio_inspirations = [
            "bacterial quorum sensing",
            "neural signaling",
            "plant hormone signaling",
            "immune system communication"
        ]
        environments = [
            "aquatic",
            "terrestrial",
            "aerial",
            "extreme (e.g., high temperature, high pressure)"
        ]
        return {
            "1": {
                "info_process": random.choice(info_processes),
                "bio_inspiration": random.choice(bio_inspirations),
                "environment": random.choice(environments)
            },
            "2": {
                "info_process": random.choice(info_processes),
                "bio_inspiration": random.choice(bio_inspirations),
                "environment": random.choice(environments)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design a theoretical synthetic organism that uses DNA-based computation to process and transmit complex information, inspired by both biological systems and information theory principles. Your organism should implement the information process of {t['info_process']}, draw inspiration from {t['bio_inspiration']}, and be adapted to an {t['environment']} environment. Your response should include:\n\n1. Organism Design (300-350 words):\n   a) Describe the overall structure and function of your synthetic organism.\n   b) Explain how DNA-based computation is implemented within the organism.\n   c) Detail how the organism performs the specified information process.\n   d) Discuss how the organism is inspired by the given biological system.\n   e) Explain how the organism is adapted to the specified environment.\n\n2. DNA Computation Mechanism (250-300 words):\n   a) Provide a detailed explanation of the DNA-based computation mechanism.\n   b) Describe how information is encoded, processed, and transmitted using DNA.\n   c) Explain how your design incorporates principles from information theory.\n   d) Discuss any novel DNA manipulation techniques your organism employs.\n\n3. Information Processing Capabilities (250-300 words):\n   a) Analyze the information processing capabilities of your synthetic organism.\n   b) Compare its performance to traditional computing systems and natural biological systems.\n   c) Discuss any emergent properties or behaviors that arise from the DNA-based computation.\n   d) Explain how the organism's capabilities are particularly suited to its environment.\n\n4. Replication and Evolution (200-250 words):\n   a) Describe how your synthetic organism replicates and passes on its DNA-based computational system.\n   b) Explain how errors or mutations in the DNA might affect the organism's information processing.\n   c) Discuss the potential for evolution of the information processing capabilities over generations.\n\n5. Ethical Considerations and Potential Applications (200-250 words):\n   a) Discuss ethical implications of creating such synthetic organisms.\n   b) Propose two potential applications of your organism in fields such as medicine, environmental monitoring, or information technology.\n   c) Address any biosafety concerns and propose containment strategies.\n\n6. Experimental Validation (150-200 words):\n   a) Propose an experimental setup to test and validate your synthetic organism's capabilities.\n   b) Describe key measurements or observations that would confirm its function.\n   c) Discuss potential challenges in implementing and testing such a system.\n\n7. Visual Representation (Not included in word count):\n   Provide a detailed diagram or schematic representation of your synthetic organism, clearly labeling key components and illustrating how DNA-based computation is integrated into its structure.\n\nEnsure your response demonstrates a deep understanding of synthetic biology, information theory, and complex systems. Be innovative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.\n\nFormat your response with clear headings for each section, numbered as above. Your total response should be between 1350-1650 words, excluding the diagram description. Include a word count at the end of your response.\n\nNote: You may use hypothetical citations to support your ideas, but this is not required. Focus on presenting a coherent and well-reasoned design and analysis."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of synthetic biology, information theory, and complex systems, integrating these disciplines effectively.",
            "The proposed synthetic organism design is innovative, scientifically plausible, and clearly explained, with a logical integration of DNA-based computation and biological processes.",
            "The submission addresses all required sections comprehensively, providing insightful analysis of the organism's capabilities, potential applications, and ethical implications.",
            "The response shows strong interdisciplinary knowledge integration, combining concepts from multiple scientific fields to address a complex bioengineering challenge.",
            "The writing is clear, well-structured, and uses appropriate technical terminology throughout, with adequate explanations for complex concepts.",
            "The visual representation (diagram or schematic) effectively illustrates the organism's structure and DNA-based computation integration.",
            "The response stays within the specified word count range and includes all required sections."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
