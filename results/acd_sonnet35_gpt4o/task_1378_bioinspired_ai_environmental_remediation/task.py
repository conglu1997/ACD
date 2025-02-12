import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        environmental_challenges = [
            {
                "challenge": "Microplastic pollution in oceans",
                "biological_inspiration": "Filter-feeding organisms"
            },
            {
                "challenge": "Urban air pollution",
                "biological_inspiration": "Plant-based air purification"
            }
        ]
        return {
            "1": random.choice(environmental_challenges),
            "2": random.choice(environmental_challenges)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a bio-inspired AI system for environmental monitoring and remediation, focusing on the environmental challenge of {t['challenge']}. Your system should draw inspiration from {t['biological_inspiration']}. Complete the following tasks:

1. System Design (300-350 words):
   a) Describe the key components of your bio-inspired AI system.
   b) Explain how your system incorporates principles from {t['biological_inspiration']}.
   c) Detail how AI is integrated into the biological aspects of your system.
   d) Discuss how your system addresses the specific environmental challenge.

2. Monitoring and Data Analysis (250-300 words):
   a) Explain how your system monitors the environment and collects data.
   b) Describe the AI algorithms or techniques used for data analysis and interpretation.
   c) Discuss how your system can adapt to changing environmental conditions.

3. Remediation Process (250-300 words):
   a) Detail the specific remediation actions your system can perform.
   b) Explain how these actions are triggered and controlled by the AI component.
   c) Discuss any potential side effects or unintended consequences of the remediation process.

4. Scalability and Deployment (200-250 words):
   a) Analyze the feasibility of scaling up your system for large-scale environmental remediation.
   b) Discuss potential challenges in deploying your system in real-world environments.
   c) Propose solutions to overcome these challenges.

5. Ethical and Ecological Implications (200-250 words):
   a) Discuss the ethical considerations of using AI-driven bio-inspired systems for environmental intervention.
   b) Analyze potential impacts on local ecosystems and biodiversity.
   c) Propose guidelines for responsible development and deployment of your system.

6. Performance Evaluation (150-200 words):
   a) Describe methods for evaluating the effectiveness of your system in addressing the environmental challenge.
   b) Propose metrics for measuring both short-term and long-term environmental impact.
   c) Discuss how you would validate the safety of your system for the environment and human health.

7. Future Developments (150-200 words):
   a) Suggest two potential improvements or expansions to your system.
   b) Discuss how emerging technologies in AI or biotechnology could enhance your system's capabilities.
   c) Propose a related environmental challenge that could be addressed using a similar approach.

Ensure your response demonstrates a deep understanding of biotechnology, environmental science, and artificial intelligence. Be creative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1500-1850 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of biotechnology, environmental science, and artificial intelligence principles.",
            "The system design effectively incorporates bio-inspiration and AI integration to address the given environmental challenge.",
            "The monitoring, data analysis, and remediation processes are well-explained and scientifically plausible.",
            "Ethical implications and ecological impacts are thoroughly considered and analyzed.",
            "The response shows creativity and innovation while maintaining scientific accuracy and feasibility."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
