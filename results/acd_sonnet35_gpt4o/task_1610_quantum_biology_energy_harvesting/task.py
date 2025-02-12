import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_principles = [
            'Quantum Coherence',
            'Quantum Entanglement',
            'Quantum Tunneling'
        ]
        photosynthetic_processes = [
            'Light Harvesting',
            'Charge Separation',
            'Electron Transport'
        ]
        energy_applications = [
            'Solar Cell Enhancement',
            'Artificial Photosynthesis',
            'Biofuel Production'
        ]
        
        tasks = [
            {
                'quantum_principle': principle,
                'photosynthetic_process': process,
                'energy_application': application
            }
            for principle in quantum_principles
            for process in photosynthetic_processes
            for application in energy_applications
        ]
        
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum-inspired model of photosynthesis focusing on the quantum principle of {t['quantum_principle']} and the photosynthetic process of {t['photosynthetic_process']}. Then, apply this model to develop a novel energy harvesting technology for {t['energy_application']}. Your response should include:

1. Quantum Biology Model (300-350 words):
   a) Explain how {t['quantum_principle']} could play a role in {t['photosynthetic_process']}.
   b) Propose a theoretical model that integrates quantum effects with biological processes.
   c) Describe the key components and mechanisms of your model.
   d) Discuss how your model differs from classical descriptions of photosynthesis.

2. Mathematical Formulation (200-250 words):
   a) Provide a mathematical representation of a key aspect of your quantum biology model.
   b) Explain the variables and equations used in your formulation.
   c) Discuss how this mathematical model captures the integration of quantum and biological principles.

3. Energy Harvesting Technology (250-300 words):
   a) Based on your quantum biology model, propose a novel energy harvesting technology for {t['energy_application']}.
   b) Describe the key components and working principles of your technology.
   c) Explain how it improves upon existing technologies in this area.
   d) Discuss potential challenges in implementing this technology and how they might be overcome.

4. Experimental Design (200-250 words):
   a) Propose an experiment to test a key aspect of your quantum biology model.
   b) Describe the experimental setup, including any specialized equipment required.
   c) Explain what results would support or refute your model.
   d) Discuss potential technical challenges and how you would address them.

5. Broader Implications (200-250 words):
   a) Analyze the potential impact of your quantum biology model on our understanding of life processes.
   b) Discuss how your energy harvesting technology could influence global energy production and sustainability efforts.
   c) Explore potential applications of your model or technology in fields beyond energy production.

6. Ethical Considerations (150-200 words):
   a) Identify potential ethical issues related to the development or application of your quantum biology model and energy technology.
   b) Propose guidelines for responsible research and development in this field.
   c) Discuss how to ensure equitable access to the benefits of this technology.

Ensure your response demonstrates a deep understanding of quantum mechanics, biology, and energy technology. Use appropriate scientific terminology and provide clear explanations where necessary. Be creative and speculative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1300-1600 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of {t['quantum_principle']} and its potential role in {t['photosynthetic_process']}",
            "The quantum biology model is well-explained and integrates quantum and biological principles in a novel way",
            f"The proposed energy harvesting technology for {t['energy_application']} is innovative and based on the quantum biology model",
            "The mathematical formulation accurately represents a key aspect of the quantum biology model",
            "The experimental design is well-thought-out and addresses potential challenges",
            "The response explores broader implications and ethical considerations thoroughly",
            "The response is creative, scientifically plausible, and demonstrates interdisciplinary thinking throughout",
            "The response adheres to the specified format and word count guidelines for each section"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
