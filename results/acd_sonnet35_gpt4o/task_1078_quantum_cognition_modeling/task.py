import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_principles = ['superposition', 'entanglement', 'interference', 'measurement problem']
        cognitive_processes = ['decision making', 'memory formation', 'attention', 'perception']
        psychological_phenomena = ['cognitive dissonance', 'false memory', 'confirmation bias', 'change blindness']
        
        return {
            "1": {
                "quantum_principle": random.choice(quantum_principles),
                "cognitive_process": random.choice(cognitive_processes),
                "psychological_phenomenon": random.choice(psychological_phenomena)
            },
            "2": {
                "quantum_principle": random.choice(quantum_principles),
                "cognitive_process": random.choice(cognitive_processes),
                "psychological_phenomenon": random.choice(psychological_phenomena)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design a theoretical framework that applies the quantum mechanical principle of {t['quantum_principle']} to model the cognitive process of {t['cognitive_process']}. Then, use this framework to explain the psychological phenomenon of {t['psychological_phenomenon']}. Your response should include:\n\n1. Theoretical Framework (250-300 words):\n   a) Explain how the quantum principle of {t['quantum_principle']} can be applied to model {t['cognitive_process']}.\n   b) Describe the key components and mechanisms of your quantum cognition model.\n   c) Discuss how your model differs from classical cognitive models of {t['cognitive_process']}.\n   d) Provide a mathematical or conceptual representation of your model (use clear textual description).\n\n2. Application to Psychological Phenomenon (200-250 words):\n   a) Briefly describe the psychological phenomenon of {t['psychological_phenomenon']}.\n   b) Apply your quantum cognition model to explain this phenomenon.\n   c) Highlight how your quantum-based explanation differs from traditional explanations.\n\n3. Experimental Predictions (150-200 words):\n   a) Propose two testable predictions that your quantum cognition model makes about {t['psychological_phenomenon']}.\n   b) Describe an experimental setup that could test one of these predictions.\n\n4. Implications and Limitations (150-200 words):\n   a) Discuss the broader implications of your model for our understanding of cognition and consciousness.\n   b) Address potential limitations or criticisms of applying quantum mechanics to cognitive processes.\n\n5. Interdisciplinary Connections (100-150 words):\n   Explain how your quantum cognition model might inform or be applied in a field outside of psychology or physics.\n\nEnsure your response demonstrates a deep understanding of both quantum mechanics and cognitive science. Use appropriate terminology and provide clear explanations for complex concepts. Be creative in your approach while maintaining scientific plausibility and logical consistency.\n\nFormat your response with clear headings for each section."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response correctly applies the quantum principle of {t['quantum_principle']} to model {t['cognitive_process']}.",
            "The theoretical framework is well-explained, logically consistent, and demonstrates a deep understanding of both quantum mechanics and cognitive science.",
            f"The application of the model to explain {t['psychological_phenomenon']} is clear, insightful, and demonstrates how quantum principles can offer new perspectives on psychological phenomena.",
            "The proposed experimental predictions and setup are scientifically sound and directly related to the quantum cognition model.",
            "The discussion of implications and limitations shows critical thinking and awareness of the challenges in applying quantum mechanics to cognition.",
            "The interdisciplinary connection is innovative and well-reasoned.",
            "The overall response demonstrates creativity, scientific rigor, and the ability to integrate complex concepts from different fields."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
