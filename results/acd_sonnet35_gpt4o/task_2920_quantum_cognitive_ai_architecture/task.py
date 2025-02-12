import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_principles = [
            "superposition",
            "entanglement",
            "quantum tunneling"
        ]
        cognitive_processes = [
            "working memory",
            "long-term memory consolidation",
            "episodic memory retrieval"
        ]
        ai_applications = [
            "natural language processing",
            "computer vision",
            "decision making under uncertainty"
        ]
        
        tasks = {
            "1": {
                "quantum_principle": random.choice(quantum_principles),
                "cognitive_process": random.choice(cognitive_processes),
                "ai_application": random.choice(ai_applications)
            },
            "2": {
                "quantum_principle": random.choice(quantum_principles),
                "cognitive_process": random.choice(cognitive_processes),
                "ai_application": random.choice(ai_applications)
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum-inspired neural network architecture for AI that mimics human {t['cognitive_process']}, integrating the quantum principle of {t['quantum_principle']}. Then, apply this architecture to the AI application of {t['ai_application']}. Your response should include the following sections:

1. Conceptual Framework (250-300 words):
   a) Explain how the quantum principle of {t['quantum_principle']} can be applied to model {t['cognitive_process']}.
   b) Describe how this quantum-inspired approach differs from classical neural network architectures.
   c) Discuss potential advantages of this approach for AI systems.

2. Architecture Design (300-350 words):
   a) Provide a detailed description of your quantum-inspired neural network architecture.
   b) Explain how each component of your architecture relates to both quantum principles and neuroscientific understanding of {t['cognitive_process']}.
   c) Include a diagram or pseudocode representation of your architecture. If using a diagram, describe it in text. If using pseudocode, use a code block format.

3. Mathematical Formulation (200-250 words):
   a) Present the key mathematical equations that describe your quantum-inspired neural network.
   b) Explain the significance of each term in your equations.
   c) Discuss how your formulation incorporates both quantum and neurobiological principles.

4. Learning and Inference (200-250 words):
   a) Describe how your architecture learns from data and performs inference.
   b) Explain how quantum effects are utilized in these processes.
   c) Compare the computational complexity of your approach to classical methods.

5. Application to {t['ai_application']} (250-300 words):
   a) Explain how your quantum-inspired architecture can be applied to {t['ai_application']}.
   b) Describe the potential advantages of your approach in this application.
   c) Discuss any challenges or limitations that may arise in this application.

6. Experimental Design (150-200 words):
   a) Propose an experiment to test the performance of your architecture in the chosen application.
   b) Describe the dataset, evaluation metrics, and baseline models you would use.

7. Ethical Considerations and Future Directions (150-200 words):
   a) Discuss potential ethical implications of using quantum-inspired AI architectures that mimic human cognition.
   b) Suggest two future research directions to further develop this technology.

Ensure your response demonstrates a deep understanding of quantum mechanics, neuroscience, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered exactly as above. Adhere to the word count guidelines for each section. Your total response should be between 1500-1850 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a clear understanding of {t['quantum_principle']} and how it can be applied to model {t['cognitive_process']}.",
            "The quantum-inspired neural network architecture is innovative, well-explained, and scientifically plausible.",
            "The response includes a diagram or pseudocode representation of the proposed architecture.",
            "The mathematical formulation accurately represents the proposed architecture and incorporates both quantum and neurobiological principles.",
            f"The application to {t['ai_application']} is well-reasoned and demonstrates potential advantages of the quantum-inspired approach.",
            "The experimental design is appropriate for testing the performance of the proposed architecture.",
            "The response addresses ethical considerations and suggests relevant future research directions.",
            "The overall response shows strong interdisciplinary thinking, connecting concepts from quantum mechanics, neuroscience, and artificial intelligence in a novel and scientifically plausible manner.",
            "The response adheres to the specified word count guidelines for each section."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
