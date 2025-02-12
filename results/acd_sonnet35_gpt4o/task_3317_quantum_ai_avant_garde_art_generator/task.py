import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'quantum_principle': 'Superposition',
                'ai_technique': 'Generative Adversarial Networks (GANs)',
                'art_form': 'Holographic Sculptures',
                'artistic_movement': 'Neo-Surrealism'
            },
            {
                'quantum_principle': 'Entanglement',
                'ai_technique': 'Quantum Reinforcement Learning',
                'art_form': 'Interactive Soundscapes',
                'artistic_movement': 'Post-Digital Expressionism'
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum-inspired AI system for generating and critiquing avant-garde art, focusing on the quantum principle of {t['quantum_principle']}, the AI technique of {t['ai_technique']}, the art form of {t['art_form']}, and the artistic movement of {t['artistic_movement']}. Your response should include:

1. System Architecture (300-350 words):
   a) Describe the key components of your quantum-inspired AI art generation and critique system.
   b) Explain how {t['quantum_principle']} is integrated into the system's design and functionality.
   c) Detail how {t['ai_technique']} is utilized in the creative process and art analysis.
   d) Discuss how your system incorporates principles from {t['artistic_movement']} in its artistic approach.

2. Quantum-Artistic Integration (250-300 words):
   a) Explain how {t['quantum_principle']} enhances or modifies the art generation and critique process.
   b) Discuss any novel artistic insights or capabilities that emerge from this integration.
   c) Address potential challenges in combining quantum principles with artistic creation and evaluation.

3. Art Generation Process (250-300 words):
   a) Provide a step-by-step explanation of how your system would generate a piece of {t['art_form']}.
   b) Illustrate with a specific example, describing the artwork in detail.
   c) Explain how quantum effects influence the creative process and the resulting artwork.

4. Art Critique Mechanism (200-250 words):
   a) Describe how your AI system analyzes and critiques the generated {t['art_form']}.
   b) Explain how it incorporates principles from {t['artistic_movement']} in its evaluation.
   c) Provide an example critique of the artwork described in the previous section.

5. Artistic and Technological Implications (200-250 words):
   a) Analyze how your system might impact or challenge traditional artistic practices and theory.
   b) Discuss potential new artistic paradigms that could emerge from quantum-inspired AI art.
   c) Address any philosophical implications of applying quantum principles to artistic creation and critique.

6. Experimental Evaluation (200-250 words):
   a) Propose an experiment to evaluate the artistic merit and innovation of your quantum-inspired AI art system.
   b) Describe the methodology, including how you would involve human artists and critics.
   c) Discuss potential challenges in empirically evaluating avant-garde art created by AI.
   d) Explain how you would measure the impact of quantum principles on the artistic output.

Ensure your response demonstrates a deep understanding of quantum computing, artificial intelligence, and art theory. Use appropriate terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific and artistic rigor.

Format your response with clear headings for each section. Your total response should be between 1400-1700 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of quantum computing principles, AI techniques, and art theory.",
            f"The system design effectively incorporates the quantum principle of {t['quantum_principle']} and the AI technique of {t['ai_technique']}.",
            f"The art generation and critique process is well-explained and aligns with the principles of {t['artistic_movement']}.",
            f"The description of the generated {t['art_form']} is creative, detailed, and plausible within the given constraints.",
            "The discussion of artistic and technological implications shows thoughtful consideration of the system's potential impact on art and society.",
            "The proposed experimental evaluation is well-designed and addresses the challenges of assessing AI-generated avant-garde art.",
            "The writing is clear, well-structured, and uses appropriate technical and artistic terminology.",
            "The response is innovative and speculative while maintaining scientific and artistic plausibility."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
