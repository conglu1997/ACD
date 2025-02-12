import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        languages = ['Mandarin', 'Spanish', 'Arabic', 'Hindi', 'Russian']
        quantum_concepts = ['superposition', 'interference', 'measurement']
        nlp_tasks = ['sentiment analysis', 'named entity recognition', 'text classification']
        
        return {
            "1": {
                "source_language": random.choice(languages),
                "target_language": random.choice(languages),
                "quantum_concept": random.choice(quantum_concepts),
                "nlp_task": random.choice(nlp_tasks)
            },
            "2": {
                "source_language": random.choice(languages),
                "target_language": random.choice(languages),
                "quantum_concept": random.choice(quantum_concepts),
                "nlp_task": random.choice(nlp_tasks)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design a quantum algorithm for analyzing semantic relationships in natural language using the principle of quantum entanglement, and apply it to cross-lingual {t['nlp_task']} between {t['source_language']} and {t['target_language']}. Your algorithm should specifically leverage the quantum concept of {t['quantum_concept']}. Your response should include:\n\n1. Quantum-Linguistic Framework (300-350 words):\n   a) Explain how quantum entanglement can be used to model semantic relationships in language.\n   b) Describe how you will represent words or phrases as quantum states.\n   c) Explain how the quantum concept of {t['quantum_concept']} is incorporated into your framework.\n   d) Discuss the potential advantages of this quantum approach over classical NLP methods.\n\n2. Cross-Lingual Algorithm Design (250-300 words):\n   a) Provide a step-by-step description of your quantum algorithm for cross-lingual {t['nlp_task']}.\n   b) Explain how your algorithm handles the transition between {t['source_language']} and {t['target_language']}.\n   c) Describe any quantum gates or operations specific to your algorithm.\n   d) Discuss how your algorithm addresses challenges specific to the chosen languages.\n\n3. Quantum Circuit Representation (150-200 words):\n   a) Provide a high-level quantum circuit diagram (using ASCII art) that represents the key components of your algorithm.\n   b) Explain the function of each major component in the circuit.\n\n4. Performance Analysis (200-250 words):\n   a) Discuss the expected computational complexity of your algorithm.\n   b) Compare its theoretical performance to classical algorithms for the same task.\n   c) Analyze potential speedup or accuracy improvements.\n   d) Identify any limitations or constraints of your quantum approach.\n\n5. Implementation Challenges (150-200 words):\n   a) Discuss the main challenges in implementing your algorithm on current or near-term quantum hardware.\n   b) Propose potential solutions or workarounds for these challenges.\n   c) Suggest any classical preprocessing or postprocessing steps that might be necessary.\n\n6. Ethical and Societal Implications (150-200 words):\n   a) Discuss potential ethical concerns related to using quantum computing for cross-lingual NLP tasks.\n   b) Explore the societal impacts of highly efficient cross-lingual analysis tools.\n   c) Propose guidelines for responsible development and use of quantum NLP technologies.\n\nEnsure your response demonstrates a deep understanding of both quantum computing principles and computational linguistics. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.\n\nFormat your response with clear headings for each section. Your total response should be between 1200-1500 words."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of both quantum computing and computational linguistics.",
            "The quantum-linguistic framework is well-explained and integrates quantum entanglement with semantic analysis.",
            "The cross-lingual algorithm design is clearly described and addresses the specific NLP task and languages.",
            "The quantum circuit representation is provided and explained adequately.",
            "The performance analysis and implementation challenges are thoroughly discussed.",
            "Ethical and societal implications are thoughtfully considered.",
            "The response is creative and innovative while maintaining scientific plausibility."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
