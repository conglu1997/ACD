import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "quantum_property": "Entanglement",
                "biological_info": "Genetic code",
                "cosmic_environment": "Interstellar radiation"
            },
            {
                "quantum_property": "Superposition",
                "biological_info": "Protein folding patterns",
                "cosmic_environment": "Extreme temperature variations"
            }
        ]
        return {
            "1": random.choice(scenarios),
            "2": random.choice(scenarios)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design a theoretical system for encoding and preserving complex biological information in quantum states for interstellar panspermia, and analyze its implications for the search for extraterrestrial life. Focus on the following scenario:\n\nQuantum property: {t['quantum_property']}\nBiological information: {t['biological_info']}\nCosmic environment: {t['cosmic_environment']}\n\nYour response should include the following sections:\n\n1. Quantum Encoding Mechanism (250-300 words):\n   a) Describe how you would use the specified quantum property to encode the given biological information.\n   b) Explain the advantages of using this quantum approach over classical methods.\n   c) Discuss any theoretical limitations or challenges in implementing this encoding.\n\n2. Preservation and Error Correction (200-250 words):\n   a) Propose a method for preserving the quantum-encoded information over long periods and vast distances.\n   b) Describe how your system would handle error correction in the specified cosmic environment.\n   c) Discuss the theoretical maximum duration and distance for which the information could be preserved.\n\n3. Decoding and Expression (200-250 words):\n   a) Explain how the quantum-encoded information could be decoded upon reaching a suitable environment.\n   b) Describe the process by which the decoded information could lead to the expression of biological traits.\n   c) Discuss any potential unintended consequences of this decoding and expression process.\n\n4. Implications for Astrobiology (200-250 words):\n   a) Analyze how your quantum panspermia system could influence our search for extraterrestrial life.\n   b) Propose a novel biosignature that could result from your system.\n   c) Discuss the implications of your system for the diversity of life in the universe.\n\n5. Ethical Considerations and Future Research (150-200 words):\n   a) Address the ethical implications of potentially spreading earth-based life to other planets.\n   b) Suggest three potential areas for future research based on your quantum panspermia system.\n   c) Discuss how this technology could advance our understanding of the origin and evolution of life.\n\nEnsure your response demonstrates a deep understanding of quantum mechanics, biology, information theory, and cosmology. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.\n\nFormat your response with clear headings for each section. Your total response should be between 1000-1250 words."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of quantum mechanics, biology, information theory, and cosmology.",
            "The quantum encoding mechanism effectively utilizes the specified quantum property for the given biological information.",
            "The preservation and error correction methods are well-reasoned and address the specified cosmic environment.",
            "The implications for astrobiology are thoughtfully analyzed and include a novel biosignature proposal.",
            "The response is innovative while maintaining scientific plausibility.",
            "Ethical considerations are addressed, and future research directions are proposed.",
            "The response is well-structured, clear, and within the specified word count range."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
