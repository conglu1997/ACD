import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {"target": "Neural Synapses", "application": "Alzheimer's Disease Treatment"},
            {"target": "Cancer Cells", "application": "Early-Stage Tumor Detection"},
            {"target": "Mitochondria", "application": "Cellular Energy Optimization"}
        ]
        return {str(i+1): scenario for i, scenario in enumerate(random.sample(scenarios, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum-biological nanobot system for non-invasive medical diagnosis and treatment, focusing on {t['target']} for the application of {t['application']}. Then, analyze its potential applications and ethical implications. Your response should include:

1. Quantum-Biological Nanobot Design (300-350 words):
   a) Describe the key components and mechanisms of your nanobot system.
   b) Explain how it incorporates quantum effects (e.g., superposition, entanglement) in its functioning.
   c) Detail how the nanobot interacts with {t['target']} at the molecular level.
   d) Include a high-level diagram of your nanobot system (describe it textually).

2. Quantum Mechanics Integration (200-250 words):
   a) Explain which specific quantum mechanical principles your system utilizes.
   b) Describe how these quantum effects enhance the nanobot's capabilities for {t['application']}.
   c) Discuss any challenges in maintaining quantum coherence in a biological environment and how your design addresses them.

3. Biological Interface (200-250 words):
   a) Explain how your nanobot system interfaces with {t['target']} without disrupting normal biological functions.
   b) Describe any biomimetic features incorporated into your design.
   c) Discuss potential cellular responses to the nanobot and how these are mitigated.

4. Diagnosis and Treatment Mechanism (250-300 words):
   a) Detail how your nanobot system performs diagnosis related to {t['application']}.
   b) Explain the treatment mechanism for {t['application']}.
   c) Describe how the system distinguishes between healthy and diseased states.
   d) Discuss the advantages of your approach compared to conventional methods.

5. Potential Applications and Limitations (200-250 words):
   a) Propose two additional medical applications for your nanobot system beyond {t['application']}.
   b) Analyze potential limitations or risks of your system.
   c) Suggest future improvements or research directions to enhance its capabilities.

6. Ethical Implications (200-250 words):
   a) Discuss ethical considerations related to using quantum-biological nanobots for medical purposes.
   b) Address concerns about privacy, consent, and potential misuse.
   c) Propose guidelines for the responsible development and use of this technology.

Ensure your response demonstrates a deep understanding of quantum mechanics, molecular biology, and medical applications. Be innovative in your approach while maintaining scientific plausibility. Use appropriate terminology from all relevant fields and provide clear explanations for complex concepts.

Format your response with clear headings for each section. Your total response should be between 1350-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of quantum mechanics and its potential applications in biology",
            "The nanobot design is innovative, scientifically plausible, and effectively integrates quantum effects",
            "The biological interface and interaction with the target is well-explained and considers potential challenges",
            "The diagnosis and treatment mechanisms are clearly described and show advantages over conventional methods",
            "Additional applications and limitations are thoughtfully analyzed",
            "Ethical implications are thoroughly discussed with appropriate guidelines proposed",
            "The response uses correct terminology from quantum physics, biology, and medicine",
            "The answer is well-structured, coherent, and adheres to the specified word count"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
