import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        memory_types = [
            {
                "type": "Episodic Memory",
                "description": "Memory of autobiographical events",
                "quantum_analogy": "Superposition of multiple memory states"
            },
            {
                "type": "Semantic Memory",
                "description": "Memory of factual information",
                "quantum_analogy": "Entanglement of related concepts"
            }
        ]
        return {str(i+1): random.choice(memory_types) for i in range(2)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum-inspired model of human {t['type']} and apply it to enhance brain-computer interfaces for memory augmentation. Your response should include:

1. Quantum-Inspired Memory Model (300-350 words):
   a) Describe your quantum-inspired model of {t['type']}, explaining how it incorporates principles from quantum computing.
   b) Explain how your model accounts for key features of {t['type']} (e.g., {t['description']}).
   c) Discuss how the concept of {t['quantum_analogy']} is implemented in your model.
   d) Compare your quantum-inspired model to traditional neuroscientific models of {t['type']}.

2. Quantum Neural Network Architecture (250-300 words):
   a) Design a quantum neural network architecture that implements your memory model.
   b) Explain the key components of your architecture and how they interact.
   c) Describe how classical and quantum components are integrated in your design.
   d) Discuss any novel quantum algorithms or protocols used in your architecture.

3. Brain-Computer Interface Integration (250-300 words):
   a) Propose a method to interface your quantum memory model with the human brain.
   b) Explain how your BCI would encode and decode neural signals using quantum principles.
   c) Describe the physical implementation of your BCI (e.g., non-invasive vs. invasive).
   d) Discuss potential advantages of your quantum-inspired BCI over classical BCIs.

4. Memory Augmentation Application (200-250 words):
   a) Describe a specific application of your quantum-inspired BCI for memory augmentation.
   b) Explain how your system would enhance or supplement human {t['type']}.
   c) Discuss potential limitations or challenges in implementing this application.
   d) Propose a method to evaluate the effectiveness of your memory augmentation system.

5. Ethical and Philosophical Implications (200-250 words):
   a) Analyze the ethical implications of using quantum-inspired BCIs for memory augmentation.
   b) Discuss how your system might impact our understanding of consciousness and identity.
   c) Consider potential societal impacts of widespread adoption of this technology.
   d) Propose guidelines for the responsible development and use of quantum memory augmentation.

6. Future Research Directions (150-200 words):
   a) Suggest two potential improvements or extensions to your quantum memory model.
   b) Propose a novel experiment that could validate your model using human participants.
   c) Discuss how your approach could influence future trends in quantum neurotechnology.

Ensure your response demonstrates a deep understanding of quantum computing, neuroscience, and brain-computer interfaces. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1350-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must accurately describe a quantum-inspired model of {t['type']}.",
            "The quantum neural network architecture should be logically consistent and incorporate genuine quantum computing principles.",
            "The brain-computer interface integration should be plausible and clearly explained.",
            "The memory augmentation application should be innovative and directly related to the proposed model.",
            "The ethical analysis should be thoughtful and comprehensive.",
            "The response should demonstrate a deep understanding of quantum computing, neuroscience, and brain-computer interfaces."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
