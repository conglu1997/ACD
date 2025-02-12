import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_effects = [
            "quantum tunneling",
            "quantum coherence",
            "quantum entanglement",
            "superposition"
        ]
        biological_processes = [
            "photosynthesis",
            "enzyme catalysis",
            "DNA mutation",
            "neural signaling"
        ]
        ethical_considerations = [
            "moral status of artificial life",
            "impact on ecosystem balance",
            "potential for uncontrolled replication",
            "implications for human enhancement"
        ]
        applications = [
            "environmental remediation",
            "medical diagnostics and treatment",
            "quantum computing integration",
            "space exploration and colonization"
        ]
        return {
            "1": {
                "quantum_effect": random.choice(quantum_effects),
                "biological_process": random.choice(biological_processes),
                "ethical_consideration": random.choice(ethical_considerations),
                "application": random.choice(applications)
            },
            "2": {
                "quantum_effect": random.choice(quantum_effects),
                "biological_process": random.choice(biological_processes),
                "ethical_consideration": random.choice(ethical_considerations),
                "application": random.choice(applications)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a theoretical framework for creating artificial life forms that harness quantum biological effects, then analyze the ethical implications and potential applications of such entities. Your design should focus on the quantum effect of {t['quantum_effect']} in the biological process of {t['biological_process']}. Consider the ethical implication of {t['ethical_consideration']} and explore potential applications in {t['application']}.

Your response should include the following sections:

1. Quantum-Biological Framework (300-350 words):
   a) Describe the key components of your artificial life form and how it incorporates {t['quantum_effect']}.
   b) Explain how {t['quantum_effect']} enhances or modifies the {t['biological_process']} in your design.
   c) Discuss the theoretical basis for your design, citing relevant research in quantum biology.
   d) Include a diagram or detailed description of your artificial life form's structure and function.

2. Creation and Control Mechanisms (250-300 words):
   a) Outline the proposed method for creating your artificial life form.
   b) Describe any novel techniques or technologies required for its synthesis.
   c) Explain how the quantum properties of the life form can be controlled or manipulated.
   d) Discuss potential challenges in maintaining quantum effects at a biological scale.

3. Ethical Analysis (250-300 words):
   a) Analyze the ethical implications of creating artificial life forms with quantum properties.
   b) Discuss in detail the ethical consideration of {t['ethical_consideration']}.
   c) Explore the potential impact on our understanding of life and consciousness.
   d) Propose guidelines for responsible development and use of quantum-biological artificial life.

4. Applications and Societal Impact (200-250 words):
   a) Describe potential applications of your artificial life form in {t['application']}.
   b) Explain how the quantum-biological properties enable or enhance these applications.
   c) Discuss potential risks and benefits to society.
   d) Speculate on how this technology might evolve and impact various fields of science and industry.

5. Experimental Design (200-250 words):
   a) Propose an experiment to test a key aspect of your quantum-biological artificial life form.
   b) Describe the methodology, including any specialized equipment or techniques required.
   c) Explain how you would measure and verify the quantum effects in your artificial life form.
   d) Discuss potential outcomes and their implications for your theoretical framework.

6. Interdisciplinary Implications (150-200 words):
   a) Explore how your framework might inform or be informed by other scientific disciplines.
   b) Discuss potential collaborations between quantum physicists, biologists, and ethicists in this field.
   c) Propose a novel research question that arises from the intersection of quantum mechanics, biology, and artificial life.

Ensure your response demonstrates a deep understanding of quantum mechanics, biology, and bioethics. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative and speculative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1350-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a clear understanding of {t['quantum_effect']} and its potential role in {t['biological_process']}.",
            f"The ethical consideration of {t['ethical_consideration']} is thoroughly analyzed and discussed.",
            f"The proposed application in {t['application']} is well-explained and scientifically plausible.",
            "The response shows a deep understanding of quantum biology, artificial life, and bioethics principles.",
            "The proposed experimental design is well-thought-out and relevant to testing the key aspects of the quantum-biological artificial life form.",
            "The interdisciplinary implications are insightful and demonstrate an understanding of the broader scientific context.",
            "The response is creative and innovative while maintaining scientific plausibility.",
            "The ethical analysis is thorough and considers multiple perspectives.",
            "The response adheres to the specified word limits for each section and demonstrates concise, focused writing."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
