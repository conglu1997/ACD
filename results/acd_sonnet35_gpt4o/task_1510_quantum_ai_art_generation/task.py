import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_principles = [
            "Superposition",
            "Entanglement",
            "Interference",
            "Quantum Tunneling"
        ]
        ai_techniques = [
            "Generative Adversarial Networks",
            "Reinforcement Learning",
            "Quantum Neural Networks",
            "Evolutionary Algorithms"
        ]
        art_forms = [
            "Interactive 4D Sculptures",
            "Synesthetic Music-Color Compositions",
            "Quantum-Entangled Virtual Reality Environments",
            "Probability-Based Fractal Animations"
        ]
        return {
            "1": {
                "quantum_principle": random.choice(quantum_principles),
                "ai_technique": random.choice(ai_techniques),
                "art_form": random.choice(art_forms)
            },
            "2": {
                "quantum_principle": random.choice(quantum_principles),
                "ai_technique": random.choice(ai_techniques),
                "art_form": random.choice(art_forms)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design and analyze a quantum-inspired AI system for generating and evaluating {t['art_form']}, incorporating the quantum principle of {t['quantum_principle']} and the AI technique of {t['ai_technique']}. Your response should include:\n\n1. System Architecture (250-300 words):\n   a) Describe the key components of your quantum-inspired AI art generation system.\n   b) Explain how your system incorporates the specified quantum principle and AI technique.\n   c) Discuss how your system models the creation and evaluation of the given art form.\n   d) Provide a high-level diagram or pseudocode representing your system's architecture.\n\n2. Quantum-AI Integration (200-250 words):\n   a) Explain how the specified quantum principle enhances or enables the AI technique in your system.\n   b) Describe any novel quantum algorithms or structures used in your design.\n   c) Discuss potential advantages of your quantum-inspired approach over classical AI methods for art generation.\n\n3. Artistic Process and Output (200-250 words):\n   a) Describe the creative process your system employs to generate the specified art form.\n   b) Explain how quantum principles influence the artistic output.\n   c) Provide an example of a potential artistic creation from your system, highlighting its unique quantum-inspired features.\n\n4. Evaluation and Feedback (150-200 words):\n   a) Propose a method for your system to evaluate its own artistic creations.\n   b) Explain how this evaluation process incorporates both quantum and AI elements.\n   c) Discuss how your system could learn and improve its artistic output over time.\n\n5. Technical Challenges and Solutions (150-200 words):\n   a) Identify key technical challenges in implementing your quantum-inspired AI art system.\n   b) Propose solutions or approaches to address these challenges.\n   c) Discuss any limitations of current quantum hardware or AI techniques that may impact your system.\n\n6. Philosophical and Ethical Implications (150-200 words):\n   a) Discuss the philosophical implications of using quantum-inspired AI for artistic creation.\n   b) Address potential ethical concerns related to authorship, creativity, and the role of AI in art.\n   c) Propose guidelines for the responsible development and use of quantum AI in creative domains.\n\n7. Future Directions (100-150 words):\n   a) Suggest two potential extensions or applications of your quantum-inspired AI art system.\n   b) Propose a novel research question that emerges from the intersection of quantum computing, AI, and art.\n\nEnsure your response demonstrates a deep understanding of quantum computing principles, AI techniques, and artistic creation. Be creative and innovative in your approach while maintaining scientific and technological plausibility. Use appropriate technical terminology and provide clear explanations where necessary.\n\nFormat your response with clear headings for each section. Your total response should be between 1200-1550 words."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of the specified quantum principle and AI technique, and their potential applications in artistic creation.",
            "The proposed system architecture is innovative, coherent, and effectively integrates quantum and AI elements for art generation.",
            "The explanation of the artistic process and potential outputs showcases creativity and a clear link to quantum-inspired features.",
            "The evaluation and feedback mechanism demonstrates a thoughtful approach to assessing and improving AI-generated art.",
            "Technical challenges are identified and addressed with plausible solutions or approaches.",
            "The discussion of philosophical and ethical implications shows depth of thought and awareness of the broader impact of quantum AI in art.",
            "The proposed future directions and research questions are innovative and well-grounded in the intersection of quantum computing, AI, and art."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
