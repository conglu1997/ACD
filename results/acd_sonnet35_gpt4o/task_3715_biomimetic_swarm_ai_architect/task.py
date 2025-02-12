import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "biological_model": "ant colony foraging",
                "ai_application": "urban traffic management"
            },
            {
                "biological_model": "honeybee waggle dance",
                "ai_application": "distributed data processing"
            },
            {
                "biological_model": "bird murmuration",
                "ai_application": "autonomous drone coordination"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a biomimetic swarm AI system inspired by {t['biological_model']}, then analyze its potential applications in {t['ai_application']} and consider the ethical implications. Your response should include:

1. Biological Model Analysis (200-250 words):
   a) Describe the key characteristics and mechanisms of {t['biological_model']}.
   b) Explain how this collective behavior contributes to the success of the species.
   c) Identify specific aspects that could be valuable for AI system design.
   d) Cite at least one relevant scientific study on this biological phenomenon.

2. Swarm AI System Architecture (250-300 words):
   a) Propose a swarm AI system architecture inspired by {t['biological_model']}.
   b) Explain how specific features of your architecture parallel the biological model.
   c) Describe the key components and their interactions within your system.
   d) Include a high-level diagram or pseudocode snippet illustrating a crucial part of your architecture.

3. Application to {t['ai_application']} (200-250 words):
   a) Explain how your biomimetic swarm AI system could be applied to {t['ai_application']}.
   b) Discuss potential advantages of your approach compared to traditional methods.
   c) Identify any challenges or limitations in applying your system to this domain.
   d) Propose a specific scenario or use case demonstrating the system's capabilities.

4. Ethical Analysis (200-250 words):
   a) Identify potential ethical issues arising from the application of your swarm AI system.
   b) Analyze these issues using at least two different ethical frameworks.
   c) Discuss any unique ethical considerations that arise from the biomimetic nature of your system.
   d) Propose guidelines for responsible development and deployment of biomimetic swarm AI.

5. Technical Implementation and Challenges (150-200 words):
   a) Discuss the technical requirements for implementing your swarm AI system.
   b) Identify potential challenges in translating biological behaviors to artificial systems.
   c) Propose solutions or research directions to address these challenges.

6. Future Implications and Research Directions (100-150 words):
   a) Speculate on potential long-term impacts of biomimetic swarm AI on society and technology.
   b) Suggest areas for future research or expansion of your biomimetic approach.
   c) Discuss how this technology might influence our understanding of collective intelligence.

Ensure your response demonstrates a deep understanding of biology, AI principles, and ethical reasoning. Be creative in your approach while maintaining scientific and technological plausibility. Use appropriate terminology and provide clear explanations for complex concepts.

Format your answer with clear headings for each section, numbered as above. Your total response should be between 1100-1400 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of {t['biological_model']} and how it can be applied to AI systems",
            f"The swarm AI system architecture clearly draws inspiration from {t['biological_model']} and is well-suited for {t['ai_application']}",
            "The ethical analysis is thorough and applies at least two ethical frameworks correctly",
            "The technical implementation section identifies meaningful challenges and proposes plausible solutions",
            "The response shows creativity and interdisciplinary knowledge integration throughout"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
