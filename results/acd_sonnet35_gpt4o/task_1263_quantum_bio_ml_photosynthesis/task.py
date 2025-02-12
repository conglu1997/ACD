import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_principles = [
            "Superposition",
            "Entanglement",
            "Tunneling",
            "Coherence"
        ]
        ml_approaches = [
            "Quantum Neural Networks",
            "Quantum Support Vector Machines",
            "Quantum Boltzmann Machines",
            "Quantum Generative Adversarial Networks"
        ]
        photosynthetic_processes = [
            "Light harvesting",
            "Charge separation",
            "Electron transport",
            "ATP synthesis"
        ]
        
        tasks = {}
        for i in range(2):
            principle = random.choice(quantum_principles)
            approach = random.choice(ml_approaches)
            process = random.choice(photosynthetic_processes)
            
            tasks[str(i+1)] = {
                "quantum_principle": principle,
                "ml_approach": approach,
                "photosynthetic_process": process
            }
        
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum-inspired machine learning model to predict and analyze quantum effects in photosynthesis, focusing on energy transfer efficiency. Your model should incorporate the quantum principle of {t['quantum_principle']}, use a {t['ml_approach']} approach, and focus on the {t['photosynthetic_process']} process in photosynthesis.

Your response should include the following sections:

1. Quantum-Biological Framework (250-300 words):
   a) Explain the chosen quantum principle ({t['quantum_principle']}) and its relevance to photosynthesis.
   b) Describe how this principle manifests in the {t['photosynthetic_process']} process.
   c) Discuss the current scientific understanding of quantum effects in this aspect of photosynthesis.

2. Machine Learning Model Design (300-350 words):
   a) Describe the architecture of your {t['ml_approach']} model.
   b) Explain how your model incorporates the quantum principle of {t['quantum_principle']}.
   c) Detail how the model will predict and analyze energy transfer efficiency in the {t['photosynthetic_process']} process.
   d) Discuss any novel features or innovations in your model design.

3. Data Requirements and Preprocessing (200-250 words):
   a) Specify the types of data your model would require for training and validation.
   b) Describe any necessary data preprocessing or feature engineering steps.
   c) Discuss challenges in obtaining or simulating relevant quantum biological data.

4. Model Training and Evaluation (200-250 words):
   a) Outline the training process for your quantum-inspired ML model.
   b) Propose evaluation metrics specific to quantum biological predictions.
   c) Describe how you would validate your model's predictions against experimental data or theoretical models.

5. Potential Applications and Implications (200-250 words):
   a) Discuss potential applications of your model in understanding or improving photosynthesis.
   b) Explore possible implications for artificial photosynthesis or bio-inspired quantum technologies.
   c) Speculate on how this approach could be extended to other quantum biological phenomena.

6. Ethical Considerations and Limitations (150-200 words):
   a) Discuss any ethical considerations in developing and applying such a model.
   b) Analyze potential limitations or biases in your approach.
   c) Propose guidelines for responsible development and use of quantum-inspired models in biological research.

Ensure your response demonstrates a deep understanding of quantum mechanics, photosynthesis, and machine learning principles. Use appropriate scientific terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1300-1600 words.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a clear understanding of the quantum principle of {t['quantum_principle']} and its relevance to photosynthesis, particularly in the {t['photosynthetic_process']} process",
            f"The machine learning model design effectively incorporates the {t['ml_approach']} approach and the quantum principle of {t['quantum_principle']}",
            "The response includes a thorough discussion of data requirements, preprocessing, and challenges in obtaining quantum biological data",
            "The model training and evaluation process is well-described, with appropriate metrics for quantum biological predictions",
            "The response explores potential applications and implications of the model in understanding or improving photosynthesis and other quantum biological phenomena",
            "Ethical considerations and limitations of the approach are thoughtfully discussed",
            "The response demonstrates exceptional interdisciplinary integration of quantum mechanics, biology, and machine learning",
            "The proposed model design is innovative while maintaining scientific plausibility",
            "The response is well-structured, following the specified format with clear headings for each section",
            "The response uses appropriate scientific terminology and provides clear explanations for complex concepts",
            "The total response length is between 1300-1600 words"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
