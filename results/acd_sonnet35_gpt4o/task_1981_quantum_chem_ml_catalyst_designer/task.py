import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        applications = [
            "hydrogen production",
            "carbon dioxide reduction",
            "nitrogen fixation",
            "water splitting",
            "fuel cell optimization"
        ]
        catalyst_types = [
            "transition metal complexes",
            "metal-organic frameworks",
            "nanoparticles",
            "enzymes",
            "perovskites"
        ]
        ml_techniques = [
            "graph neural networks",
            "transformer architectures",
            "quantum machine learning",
            "reinforcement learning",
            "generative adversarial networks"
        ]
        quantum_chem_methods = [
            "density functional theory",
            "coupled cluster theory",
            "quantum Monte Carlo",
            "multi-reference methods",
            "ab initio molecular dynamics"
        ]
        
        return {
            "1": {
                "application": random.choice(applications),
                "catalyst_type": random.choice(catalyst_types),
                "ml_technique": random.choice(ml_techniques),
                "quantum_chem_method": random.choice(quantum_chem_methods)
            },
            "2": {
                "application": random.choice(applications),
                "catalyst_type": random.choice(catalyst_types),
                "ml_technique": random.choice(ml_techniques),
                "quantum_chem_method": random.choice(quantum_chem_methods)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design a machine learning system that leverages quantum chemistry principles to predict and optimize novel catalysts for {t['application']} using {t['catalyst_type']}. Your system should incorporate {t['ml_technique']} and {t['quantum_chem_method']}. Your response should include:\n\n1. System Architecture (250-300 words):\n   a) Describe the key components of your machine learning system.\n   b) Explain how it integrates quantum chemistry principles and data.\n   c) Detail how {t['ml_technique']} is implemented in your system.\n   d) Discuss any novel approaches or algorithms you've incorporated.\n\n2. Quantum Chemistry Integration (200-250 words):\n   a) Explain how {t['quantum_chem_method']} is used in your system.\n   b) Describe how quantum chemical data is processed and fed into the ML model.\n   c) Discuss any approximations or simplifications made in the quantum chemical calculations.\n\n3. Catalyst Optimization Process (250-300 words):\n   a) Detail how your system predicts and optimizes novel {t['catalyst_type']} for {t['application']}.\n   b) Explain the key features or descriptors used in your model.\n   c) Describe how your system handles the exploration-exploitation trade-off in catalyst design.\n\n4. Performance Evaluation (200-250 words):\n   a) Propose methods to validate your system's predictions.\n   b) Discuss how you would benchmark your system against existing catalyst design approaches.\n   c) Address potential limitations and propose strategies to overcome them.\n\n5. Practical Implementation and Scalability (150-200 words):\n   a) Discuss how your system could be implemented in a real-world research or industrial setting.\n   b) Address computational resource requirements and scalability issues.\n   c) Propose strategies for handling large-scale data and high-throughput experimentation.\n\n6. Ethical Considerations and Broader Impacts (150-200 words):\n   a) Discuss potential ethical issues related to using AI for catalyst design in sustainable energy applications.\n   b) Analyze the potential environmental and societal impacts of your system.\n   c) Propose guidelines for responsible development and use of AI in materials science and chemistry.\n\n7. Case Study (200-250 words):\n   Provide a specific example of how your system would be applied to design a novel catalyst for {t['application']}. Include details on the catalyst structure, predicted performance, and how it compares to existing catalysts in the field.\n\nEnsure your response demonstrates a deep understanding of quantum chemistry, machine learning, and catalysis. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.\n\nFormat your response with clear headings for each section, numbered as above (e.g., '1. System Architecture:'). Begin each subsection with the corresponding letter (e.g., 'a) Key components:'). Your total response should be between 1400-1750 words. Include a word count at the end of your response.\n\nSample response structure (do not copy the content, only the format):\n\n1. System Architecture:\n   a) Key components: [Your content here]\n   b) Integration of quantum chemistry: [Your content here]\n   c) Implementation of [ML technique]: [Your content here]\n   d) Novel approaches: [Your content here]\n\n[Continue with other sections...]\n\n7. Case Study:\n   [Your specific example here]\n\nWord count: [Your word count here]"

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of quantum chemistry, machine learning, and catalysis principles.",
            f"The machine learning system effectively integrates {t['ml_technique']} and {t['quantum_chem_method']}.",
            f"The system design is innovative and well-suited for optimizing {t['catalyst_type']} for {t['application']}.",
            "The response addresses all required sections comprehensively and coherently.",
            "The proposed system effectively balances theoretical rigor with practical applicability.",
            "Ethical considerations and broader impacts are thoughtfully analyzed.",
            "The response is well-structured, clear, and within the specified word count.",
            "The response follows the specified format with numbered sections and lettered subsections.",
            "The case study provides a concrete, plausible example of the system's application to catalyst design."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
