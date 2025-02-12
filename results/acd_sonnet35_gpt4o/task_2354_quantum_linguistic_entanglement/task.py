import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_principles = [
            "superposition",
            "entanglement",
            "quantum tunneling",
            "quantum interference"
        ]
        linguistic_applications = [
            "sentiment analysis",
            "machine translation",
            "text summarization",
            "language generation"
        ]
        return {
            "1": {
                "quantum_principle": random.choice(quantum_principles),
                "linguistic_application": random.choice(linguistic_applications)
            },
            "2": {
                "quantum_principle": random.choice(quantum_principles),
                "linguistic_application": random.choice(linguistic_applications)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        principle_explanations = {
            "superposition": "the ability of a quantum system to exist in multiple states simultaneously",
            "entanglement": "a phenomenon where quantum particles become correlated in such a way that the quantum state of each particle cannot be described independently",
            "quantum tunneling": "a quantum mechanical phenomenon where a particle tunnels through a barrier that it classically could not surmount",
            "quantum interference": "the interference pattern observed in quantum systems, where the probability amplitudes of alternative paths interfere with each other"
        }
        return f"Design a quantum-inspired natural language processing system that applies the principle of {t['quantum_principle']} ({principle_explanations[t['quantum_principle']]}) to the task of {t['linguistic_application']}. Your response should include:\n\n" \
               f"1. Quantum-Linguistic System Design (300-350 words):\n" \
               f"   a) Explain how you adapt {t['quantum_principle']} to model language phenomena.\n" \
               f"   b) Describe the key components of your system and their quantum-inspired functionalities.\n" \
               f"   c) Provide a mathematical formulation or pseudo-code snippet that illustrates your approach.\n\n" \
               f"2. Application to {t['linguistic_application']} (250-300 words):\n" \
               f"   a) Detail how your quantum-inspired system performs the task of {t['linguistic_application']}.\n" \
               f"   b) Compare your approach to traditional methods for this task.\n" \
               f"   c) Discuss potential advantages and limitations of your quantum-inspired approach.\n\n" \
               f"3. Quantum-Linguistic Analysis (200-250 words):\n" \
               f"   a) Analyze a short text sample (2-3 sentences) using your quantum-inspired system.\n" \
               f"   b) Explain the results and how they differ from classical NLP approaches.\n" \
               f"   c) Discuss any emergent properties or unexpected behaviors in your system.\n\n" \
               f"4. Theoretical Implications (150-200 words):\n" \
               f"   a) Discuss how your system might model or reflect cognitive processes in language understanding.\n" \
               f"   b) Explore potential implications for our understanding of language and quantum phenomena.\n\n" \
               f"5. Future Research Directions (100-150 words):\n" \
               f"   a) Propose two novel experiments or applications building on your quantum-linguistic system.\n" \
               f"   b) Suggest how your approach could be extended to other areas of NLP or cognitive science.\n\n" \
               f"Ensure your response demonstrates a deep understanding of both quantum computing principles and linguistic theory. Use appropriate terminology from both fields and provide clear explanations where necessary. Be creative and rigorous in your approach while acknowledging the speculative nature of the task.\n\n" \
               f"Format your response with clear headings for each section, numbered as above. Your total response should be between 1000-1250 words."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of {t['quantum_principle']} and how it can be applied to {t['linguistic_application']}.",
            "The quantum-inspired system design is creative, plausible, and well-explained, including a relevant mathematical formulation or pseudo-code.",
            f"The application to {t['linguistic_application']} is thoroughly described and compared to traditional methods.",
            "The quantum-linguistic analysis of a text sample is insightful and clearly differentiated from classical NLP approaches.",
            "The discussion of theoretical implications and future research directions is thoughtful and grounded in the proposed system's capabilities."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
