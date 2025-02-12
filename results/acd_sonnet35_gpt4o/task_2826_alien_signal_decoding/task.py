import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        alien_environments = [
            "Gas giant atmosphere",
            "Subsurface ocean of an icy moon",
            "Silicon-based desert planet",
            "Neutron star surface"
        ]
        signal_types = [
            "Gravitational waves",
            "Neutrino emissions",
            "Quantum entanglement patterns",
            "Modulated dark matter interactions"
        ]
        return {
            "1": {
                "environment": random.choice(alien_environments),
                "signal_type": random.choice(signal_types)
            },
            "2": {
                "environment": random.choice(alien_environments),
                "signal_type": random.choice(signal_types)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design a hypothetical alien signal detection and decoding system for a civilization evolved in a {t['environment']}, using {t['signal_type']} as their primary method of communication. Your response should include:\n\n1. Signal Characteristics (200-250 words):\n   a) Describe the unique properties of the {t['signal_type']} in the context of the {t['environment']}.\n   b) Explain how the alien civilization might have evolved to use this form of communication.\n   c) Discuss potential advantages and limitations of this communication method.\n\n2. Detection System Design (250-300 words):\n   a) Outline the key components of your detection system.\n   b) Explain how it would isolate and identify the alien signals from background noise.\n   c) Describe any novel technologies or principles your system employs.\n   d) Provide a simple diagram or flowchart of your detection system using ASCII characters.\n\n3. Decoding Methodology (250-300 words):\n   a) Propose a method for decoding the alien signals based on information theory principles.\n   b) Explain how your decoding system accounts for potential differences in alien logic or mathematics.\n   c) Describe the steps your system would take to extract meaning from the signals.\n   d) Discuss potential challenges in interpreting an entirely alien form of communication.\n\n4. Implications for SETI (200-250 words):\n   a) Analyze how your system could impact current SETI methodologies.\n   b) Discuss the potential consequences of detecting and decoding such alien signals.\n   c) Propose guidelines for responding to or handling the decoded information.\n\n5. Scientific Insights (150-200 words):\n   a) Explain how studying these alien signals could advance our understanding of astrobiology.\n   b) Discuss potential insights into fundamental physics that might be gained.\n   c) Propose a hypothesis about the nature of life and intelligence based on this scenario.\n\nEnsure your response demonstrates a deep understanding of astrobiology, information theory, and signal processing. Use appropriate scientific terminology and provide clear explanations for complex concepts. Be creative in your approach while maintaining scientific plausibility.\n\nFormat your response with clear headings for each section and number your paragraphs. Your total response should be between 1050-1300 words."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of astrobiology, information theory, and signal processing.",
            "The proposed detection and decoding systems are creative, scientifically plausible, and well-explained.",
            "The analysis of implications for SETI and potential scientific insights is thoughtful and well-reasoned.",
            "The response is well-structured, uses appropriate scientific terminology, and adheres to the specified word count."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
