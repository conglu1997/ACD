import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        biological_systems = [
            "cell membrane",
            "bacterial flagellum",
            "photosynthetic complex",
            "DNA replication machinery",
            "neural synapse"
        ]
        quantum_principles = [
            "superposition",
            "entanglement",
            "tunneling",
            "quantum coherence",
            "quantum annealing"
        ]
        medical_conditions = [
            "cancer",
            "neurodegenerative disorders",
            "cardiovascular diseases",
            "autoimmune disorders",
            "infectious diseases"
        ]
        
        tasks = [
            {
                "biological_system": random.choice(biological_systems),
                "quantum_principle": random.choice(quantum_principles),
                "medical_condition": random.choice(medical_conditions)
            } for _ in range(2)
        ]
        
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum-inspired biomimetic nanorobot system for targeted drug delivery, focusing on the {t['medical_condition']} treatment. Your nanorobot should be inspired by the {t['biological_system']} and incorporate the quantum principle of {t['quantum_principle']}. Then, analyze its potential impact on medical treatments and ethical considerations. Your response should include:

1. Nanorobot Design (300-350 words):
   a) Describe the key components and functionality of your nanorobot system.
   b) Explain how your design is inspired by the {t['biological_system']}.
   c) Detail how you incorporate the quantum principle of {t['quantum_principle']} into the nanorobot's operation.
   d) Discuss any novel approaches in your design that enhance its effectiveness for targeted drug delivery.
   e) Provide a visual representation of your nanorobot design using ASCII art or a detailed textual description.

2. Quantum-Bio Integration (250-300 words):
   a) Explain how the quantum principle of {t['quantum_principle']} enhances the nanorobot's capabilities.
   b) Describe the specific mechanisms by which quantum effects interact with biological processes in your system.
   c) Discuss any challenges in maintaining quantum effects at the nanoscale in a biological environment and how you address them.
   d) Provide a mathematical or algorithmic representation of a key quantum-biological interaction in your system.

3. Targeted Drug Delivery Process (200-250 words):
   a) Outline the step-by-step process of how your nanorobot system delivers drugs to treat {t['medical_condition']}.
   b) Explain how the biomimetic design and quantum effects contribute to improved targeting and efficacy.
   c) Discuss potential advantages of your system over conventional drug delivery methods.
   d) Address potential risks or side effects and how they are mitigated in your design.

4. Medical Impact Analysis (200-250 words):
   a) Analyze how your nanorobot system could transform the treatment of {t['medical_condition']}.
   b) Discuss potential improvements in treatment efficacy, patient outcomes, and healthcare costs.
   c) Consider how this technology might impact related medical fields or treatments.
   d) Propose a clinical trial design to test the efficacy and safety of your nanorobot system.

5. Ethical Considerations (200-250 words):
   a) Identify and discuss at least three ethical issues raised by your nanorobot system.
   b) Analyze these issues using a specific ethical framework (e.g., utilitarianism, principlism).
   c) Propose guidelines for the responsible development and use of quantum biomimetic nanorobots in medicine.
   d) Discuss potential societal impacts, including issues of access and equity in healthcare.

6. Future Research Directions (150-200 words):
   a) Suggest two potential improvements or extensions to your nanorobot system.
   b) Propose a research question that could further explore the intersection of quantum computing, biomimetics, and nanomedicine.
   c) Discuss potential applications of your technology beyond {t['medical_condition']} treatment.

Ensure your response demonstrates a deep understanding of quantum mechanics, nanotechnology, biomedical engineering, and ethical reasoning. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative and speculative in your approach while maintaining scientific plausibility.

Format your response using clear headings for each section, numbered as above. Your total response should be between 1300-1600 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must design a nanorobot system for treating {t['medical_condition']} inspired by {t['biological_system']} and incorporating the quantum principle of {t['quantum_principle']}",
            "The nanorobot design should be scientifically plausible and clearly explained, including a visual representation",
            f"A detailed explanation of how the quantum principle of {t['quantum_principle']} is applied in the nanorobot's operation must be provided",
            "The response should demonstrate interdisciplinary knowledge integration across quantum physics, biology, and nanotechnology",
            "The targeted drug delivery process should be well-defined and logically incorporate both biomimetic and quantum elements",
            "The medical impact analysis should be thorough and include a proposed clinical trial design",
            "Ethical considerations must be thoughtfully addressed, including a specific ethical framework analysis",
            "Future research directions should be relevant and well-justified",
            "The response should follow the specified format with clear headings for each section",
            "The response should be within the specified word count range (1300-1600 words)"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
