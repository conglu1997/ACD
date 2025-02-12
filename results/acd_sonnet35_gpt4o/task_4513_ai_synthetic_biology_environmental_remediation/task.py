import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        environmental_issues = [
            "Oil spill cleanup",
            "Heavy metal contamination in soil",
            "Plastic pollution in oceans",
            "Atmospheric carbon dioxide reduction"
        ]
        organism_types = [
            "Bacteria",
            "Algae",
            "Fungi",
            "Synthetic protocells"
        ]
        ai_approaches = [
            "Evolutionary algorithms",
            "Reinforcement learning",
            "Generative adversarial networks",
            "Neuroevolution"
        ]
        
        tasks = {}
        for i in range(2):
            tasks[str(i+1)] = {
                "environmental_issue": random.choice(environmental_issues),
                "organism_type": random.choice(organism_types),
                "ai_approach": random.choice(ai_approaches)
            }
        
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that creates and optimizes synthetic organisms for environmental remediation, focusing on {t['environmental_issue']} using {t['organism_type']} as the base organism and {t['ai_approach']} as the primary AI method. Then, analyze its potential applications and ethical implications. Your response should include:

1. AI System Architecture (300-350 words):
   a) Describe the key components of your AI system for designing synthetic organisms.
   b) Explain how your system incorporates {t['ai_approach']} to optimize organism design.
   c) Detail how the AI integrates biological knowledge with environmental remediation goals.
   d) Include a high-level diagram or flowchart of your system's architecture (use ASCII art or a structured text description, with at least 10 lines).

2. Synthetic Biology Approach (250-300 words):
   a) Explain the genetic modifications your system would propose for {t['organism_type']} to address {t['environmental_issue']}.
   b) Describe how your system ensures the stability and safety of the synthetic organisms.
   c) Discuss any novel synthetic biology techniques your system might employ.

3. Environmental Remediation Strategy (250-300 words):
   a) Detail how your synthetic organisms would tackle {t['environmental_issue']}.
   b) Analyze the potential effectiveness and efficiency of this approach compared to current methods.
   c) Discuss any potential ecological impacts of introducing these synthetic organisms into the environment.

4. AI Optimization Process (200-250 words):
   a) Explain how your AI system optimizes the synthetic organisms over time.
   b) Describe the feedback mechanisms and data sources used for optimization.
   c) Discuss how the system balances multiple objectives (e.g., effectiveness, safety, ecological impact).

5. Scalability and Practical Implementation (200-250 words):
   a) Propose a strategy for scaling up the production and deployment of your synthetic organisms.
   b) Discuss potential challenges in implementing this technology in real-world scenarios.
   c) Suggest methods for monitoring and controlling the synthetic organisms post-deployment.

6. Ethical and Regulatory Considerations (200-250 words):
   a) Identify and discuss at least three ethical concerns raised by your AI-driven synthetic biology approach.
   b) Propose guidelines for responsible development and use of this technology.
   c) Discuss potential regulatory frameworks that might govern the use of AI-designed synthetic organisms for environmental remediation.

7. Future Research Directions (150-200 words):
   a) Propose two potential extensions or applications of your AI-driven synthetic biology system.
   b) Suggest experiments or studies to address unresolved questions about the long-term impacts of this technology.

Ensure your response demonstrates a deep understanding of synthetic biology, artificial intelligence, environmental science, and ethics. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative and innovative in your approach while maintaining scientific plausibility and addressing real-world constraints.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1550-1900 words. Include at least 5 relevant citations or references throughout your response, using a consistent citation style (e.g., APA or IEEE). Add a 'References' section at the end of your response (not counted in the word limit) with full citations for all sources mentioned."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of synthetic biology, artificial intelligence, environmental science, and ethics",
            "The AI system architecture is well-designed and clearly explained, with a coherent integration of the specified AI approach",
            "The synthetic biology approach is scientifically plausible and tailored to the given environmental issue",
            "The environmental remediation strategy is well-thought-out and addresses potential ecological impacts",
            "The AI optimization process is clearly explained and addresses multiple objectives",
            "Scalability and practical implementation challenges are thoroughly discussed",
            "Ethical and regulatory considerations are thoughtfully analyzed with concrete proposals",
            "Future research directions are innovative and relevant",
            "The response is well-structured, within the specified word count, and includes all required sections",
            "The response includes at least 5 relevant citations or references, with a proper 'References' section",
            "The high-level diagram or flowchart is clear, detailed, and at least 10 lines long"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
