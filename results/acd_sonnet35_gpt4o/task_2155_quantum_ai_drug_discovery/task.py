import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_properties = ['superposition', 'entanglement', 'tunneling']
        ai_techniques = ['reinforcement learning', 'generative adversarial networks', 'attention mechanisms']
        drug_targets = ['neurodegenerative diseases', 'cancer', 'viral infections']
        
        tasks = {
            "1": {
                "quantum_property": random.choice(quantum_properties),
                "ai_technique": random.choice(ai_techniques),
                "drug_target": random.choice(drug_targets)
            },
            "2": {
                "quantum_property": random.choice(quantum_properties),
                "ai_technique": random.choice(ai_techniques),
                "drug_target": random.choice(drug_targets)
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum-enhanced AI system for drug discovery that leverages both quantum computing and machine learning to predict drug-protein interactions and optimize molecular structures. Your system should incorporate the quantum property of {t['quantum_property']}, utilize the AI technique of {t['ai_technique']}, and focus on developing drugs for {t['drug_target']}. Your response should include:

1. System Architecture (300-350 words):
   a) Describe the key components of your quantum-enhanced AI drug discovery system.
   b) Explain how you integrate quantum computing and AI in your design.
   c) Detail how your system incorporates the specified quantum property and AI technique.
   d) Discuss how your system is tailored to address the given drug target.
   e) Include a high-level diagram or flowchart of your system architecture (describe this textually).

2. Quantum-AI Integration (250-300 words):
   a) Explain how the quantum property enhances the AI-driven drug discovery process.
   b) Describe any novel algorithms or techniques you've developed to leverage both quantum and AI capabilities.
   c) Discuss potential synergies between quantum computing and the specified AI technique in the context of drug discovery.

3. Drug Discovery Process (200-250 words):
   a) Outline the steps your system takes to identify and optimize potential drug candidates.
   b) Explain how your system predicts drug-protein interactions and optimizes molecular structures.
   c) Describe how your approach might accelerate or improve traditional drug discovery methods.

4. Challenges and Solutions (200-250 words):
   a) Identify potential technical challenges in implementing your quantum-enhanced AI drug discovery system.
   b) Propose solutions or approaches to overcome these challenges.
   c) Discuss any limitations of your system and how they might be addressed in future iterations.

5. Experimental Validation (150-200 words):
   a) Propose an experimental setup to validate the effectiveness of your system.
   b) Describe key metrics you would use to evaluate its performance.
   c) Discuss how you would compare your system's results to traditional drug discovery methods.

6. Ethical and Societal Implications (150-200 words):
   a) Discuss potential ethical concerns related to using quantum-enhanced AI for drug discovery.
   b) Analyze possible societal impacts of accelerated drug development.
   c) Propose guidelines for responsible development and use of such technology.

Ensure your response demonstrates a deep understanding of quantum computing, artificial intelligence, and biochemistry. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative and innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1250-1550 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response includes a detailed system architecture that integrates quantum computing (using {t['quantum_property']}) and AI (using {t['ai_technique']}) for drug discovery targeting {t['drug_target']}.",
            "The quantum-AI integration is well-explained and scientifically plausible.",
            "The drug discovery process is clearly outlined and demonstrates an understanding of biochemistry and pharmacology.",
            "Challenges and potential solutions are thoughtfully discussed.",
            "An appropriate experimental validation approach is proposed.",
            "Ethical and societal implications are thoroughly considered.",
            "The overall response demonstrates creativity, scientific plausibility, and a deep understanding of quantum computing, artificial intelligence, and biochemistry."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
