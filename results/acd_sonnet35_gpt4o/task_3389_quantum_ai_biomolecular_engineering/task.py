import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        challenges = [
            {
                "quantum_principle": "superposition",
                "ai_technique": "reinforcement learning",
                "biomolecular_target": "protein folding",
                "bioengineering_application": "drug design",
                "related_domain": "neuroscience"
            },
            {
                "quantum_principle": "entanglement",
                "ai_technique": "generative adversarial networks",
                "biomolecular_target": "DNA origami",
                "bioengineering_application": "nanomaterial synthesis",
                "related_domain": "materials science"
            }
        ]
        return {str(i+1): challenge for i, challenge in enumerate(challenges)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum-inspired AI system for modeling and manipulating complex biomolecular structures, focusing on {t['biomolecular_target']}. Your system should incorporate the quantum principle of {t['quantum_principle']} and use {t['ai_technique']} as a key AI technique. Then, apply your system to the bioengineering challenge of {t['bioengineering_application']} and analyze its implications for {t['related_domain']}. Your response should include:

1. System Architecture (300-350 words):
   a) Describe the key components of your quantum-inspired AI system for biomolecular modeling and manipulation.
   b) Explain how you incorporate {t['quantum_principle']} into your design.
   c) Detail how {t['ai_technique']} is integrated into your system.
   d) Discuss the interface between quantum-inspired components, AI algorithms, and biomolecular simulations.
   e) Include a high-level diagram or pseudocode to illustrate your architecture (describe this textually).

2. Biomolecular Modeling and Manipulation Process (250-300 words):
   a) Explain step-by-step how your system models and manipulates {t['biomolecular_target']}.
   b) Describe how quantum-inspired computation provides an advantage in this process.
   c) Detail how {t['ai_technique']} enhances the modeling and manipulation capabilities.
   d) Discuss any novel algorithms or techniques you've developed for this application.

3. Application to {t['bioengineering_application']} (250-300 words):
   a) Outline how your system is applied to the specified bioengineering challenge.
   b) Describe the potential benefits and limitations of your approach in this context.
   c) Propose a specific example or use case within {t['bioengineering_application']}.
   d) Discuss how your system could accelerate or improve current methods in this field.

4. Cross-domain Analysis: Implications for {t['related_domain']} (200-250 words):
   a) Analyze how your quantum-inspired AI biomolecular engineering system could impact or advance {t['related_domain']}.
   b) Identify potential synergies or conflicts between your system's capabilities and current approaches in {t['related_domain']}.
   c) Propose a novel application or research direction that combines your system with {t['related_domain']}.
   d) Discuss any challenges or opportunities in bridging these scientific domains.

5. Performance Analysis and Validation (200-250 words):
   a) Propose metrics to evaluate the performance of your quantum-inspired AI biomolecular engineering system.
   b) Describe how you would validate the accuracy and reliability of your system's outputs.
   c) Discuss potential advantages in terms of speed, accuracy, or capabilities compared to classical approaches.
   d) Address any potential sources of error or uncertainty in your system.

6. Ethical and Societal Implications (200-250 words):
   a) Identify and discuss key ethical concerns raised by your system and its application.
   b) Analyze potential impacts on medicine, biotechnology, and society at large.
   c) Discuss issues of safety, regulation, and potential for misuse.
   d) Propose guidelines for the responsible development and use of such technology.

7. Future Developments and Challenges (150-200 words):
   a) Identify key technical challenges in implementing your system with current technologies.
   b) Propose potential solutions or areas for future research to address these challenges.
   c) Speculate on how advancements in quantum computing, AI, and bioengineering might enhance your system.
   d) Discuss the long-term potential of quantum-inspired AI in molecular and synthetic biology.

Ensure your response demonstrates a deep understanding of quantum computing principles, artificial intelligence, molecular biology, bioengineering, and {t['related_domain']}. Use appropriate technical terminology from all relevant fields and provide clear explanations where necessary. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1550-1900 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The system design incorporates the quantum principle of {t['quantum_principle']}",
            f"The AI technique {t['ai_technique']} is effectively integrated into the system",
            f"The system demonstrates a clear approach to modeling and manipulating {t['biomolecular_target']}",
            f"The application to {t['bioengineering_application']} is well-explained and plausible",
            f"The implications for {t['related_domain']} are thoroughly analyzed",
            "The response shows a deep understanding of quantum computing, AI, molecular biology, and the related scientific domain",
            "The ethical and societal implications are comprehensively discussed",
            "The response demonstrates creativity and innovation while maintaining scientific plausibility"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
