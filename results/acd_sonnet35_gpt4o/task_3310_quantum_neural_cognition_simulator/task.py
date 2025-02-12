import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cognitive_processes = [
            {
                'process': 'Working memory',
                'domain': 'Strategic decision-making',
                'quantum_principle': 'Superposition'
            },
            {
                'process': 'Pattern recognition',
                'domain': 'Visual art analysis',
                'quantum_principle': 'Entanglement'
            },
            {
                'process': 'Language processing',
                'domain': 'Real-time translation',
                'quantum_principle': 'Quantum tunneling'
            },
            {
                'process': 'Emotional regulation',
                'domain': 'Conflict resolution',
                'quantum_principle': 'Quantum annealing'
            }
        ]
        
        return {str(i+1): random.choice(cognitive_processes) for i in range(2)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum-inspired neural network model to simulate and enhance the cognitive process of {t['process']}, then apply it to solve a complex problem in the domain of {t['domain']}. Your model should incorporate the quantum principle of {t['quantum_principle']}. Your response should include:

1. Quantum-Inspired Neural Architecture (250-300 words):
   a) Describe the key components of your quantum-inspired neural network model.
   b) Explain how it simulates and enhances the cognitive process of {t['process']}.
   c) Detail how you incorporate the quantum principle of {t['quantum_principle']} into your model.
   d) Provide a high-level diagram or mathematical representation of your model's architecture. If using a diagram, describe it in text format (e.g., ASCII art or a structured text description). If using a mathematical representation, ensure all symbols are clearly defined.

2. Cognitive Process Simulation (200-250 words):
   a) Explain how your model simulates the specific cognitive process of {t['process']}.
   b) Discuss how the quantum-inspired approach enhances this cognitive process compared to classical neural networks.
   c) Describe any novel computational or algorithmic techniques used in your simulation.
   d) Provide a concrete example of how your model would process a specific input related to {t['process']}.

3. Domain Application (250-300 words):
   a) Apply your model to solve a complex problem in the domain of {t['domain']}.
   b) Provide a detailed description of the problem and how your model addresses it.
   c) Explain how the enhanced cognitive process contributes to solving this problem.
   d) Discuss any potential limitations or challenges in applying your model to this domain.
   e) Propose a hypothetical experiment to validate your model's performance in this domain.

4. Performance Analysis (200-250 words):
   a) Propose specific metrics for evaluating the performance of your quantum-inspired neural network.
   b) Compare the expected performance of your model to at least two traditional approaches in both cognitive simulation and problem-solving in the specified domain.
   c) Discuss any potential quantum advantages or computational speedups your model might offer, providing quantitative estimates where possible.
   d) Address potential scalability issues and how they might be overcome.

5. Ethical Implications and Future Directions (150-200 words):
   a) Analyze at least three potential ethical concerns related to enhancing human cognitive processes with quantum-inspired AI.
   b) Discuss broader implications of your model for neuroscience and artificial intelligence, including potential risks and benefits to society.
   c) Propose two future research directions that could further advance this field, explaining how they build upon your current model.

Ensure your response demonstrates a deep understanding of quantum computing principles, neuroscience, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility. Avoid simply restating existing theories; instead, focus on developing novel ideas and connections between fields.

Format your response with clear headings for each section and use numbered subheadings for each point. Your total response should be between 1050-1300 words. Include your diagram or mathematical representation within the relevant section of your text response.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a comprehensive understanding of quantum computing principles, neuroscience, and artificial intelligence in the context of simulating and enhancing {t['process']}.",
            f"The proposed quantum-inspired neural network effectively incorporates the quantum principle of {t['quantum_principle']} and provides a plausible mechanism for enhancing {t['process']}.",
            f"The model's application to the domain of {t['domain']} is creative, well-explained, and addresses a significant problem in that field.",
            "The performance analysis includes specific metrics and compares the model to at least two traditional approaches, with quantitative estimates where possible.",
            "The ethical implications section addresses at least three potential concerns and demonstrates a thoughtful consideration of the broader impact of this technology.",
            "The response includes a clear diagram or mathematical representation that effectively illustrates the model's architecture or key concepts.",
            "The response follows the required format and word count guidelines, uses appropriate technical terminology throughout, and presents novel ideas rather than simply restating existing theories."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
