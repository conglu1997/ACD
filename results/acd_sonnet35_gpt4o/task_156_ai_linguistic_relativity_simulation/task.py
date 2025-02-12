import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "language_feature": "grammatical gender",
                "cognitive_domain": "object classification",
                "decision_context": "resource allocation in a simulated economy"
            },
            {
                "language_feature": "evidentiality markers",
                "cognitive_domain": "information processing and trust assessment",
                "decision_context": "evaluating news sources in a social media environment"
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that simulates linguistic relativity effects, focusing on how {t['language_feature']} might influence AI cognition in the domain of {t['cognitive_domain']}. Then, analyze its potential impact on {t['decision_context']}. Your response should include the following sections, each clearly labeled:

1. AI System Design (200-250 words):
   - Describe the key components of your AI system that enable it to simulate linguistic relativity effects.
   - Explain how the system incorporates {t['language_feature']} and how this feature might influence its cognitive processes related to {t['cognitive_domain']}.
   - Propose a novel mechanism or algorithm that allows the AI to switch between different linguistic frameworks and observe changes in its cognitive outcomes.

2. Cognitive Impact Analysis (200-250 words):
   - Analyze how the presence or absence of {t['language_feature']} might affect the AI's performance in tasks related to {t['cognitive_domain']}.
   - Provide specific examples of how the AI's processing or decision-making might differ based on the linguistic structure it's operating under.
   - Discuss potential biases or limitations that might emerge as a result of these linguistic influences.

3. Decision-Making Simulation (200-250 words):
   - Describe a detailed scenario related to {t['decision_context']} where your AI system would be applied.
   - Explain how the linguistic relativity effects might influence the AI's decision-making in this context.
   - Compare and contrast the potential outcomes when the AI operates under at least two different linguistic frameworks.

4. Philosophical Implications (150-200 words):
   - Discuss the philosophical implications of an AI system exhibiting linguistic relativity effects.
   - Consider questions of AI consciousness, the nature of machine 'thinking', and the relationship between language and reality in artificial systems.

5. Ethical Considerations and Safeguards (150-200 words):
   - Identify at least three potential ethical issues that could arise from deploying such an AI system in real-world applications.
   - Propose specific safeguards or guidelines for responsible development and use of linguistically influenced AI systems.

Ensure your response is creative, well-reasoned, and grounded in current understanding of linguistics, cognitive science, and artificial intelligence. Use clear headings for each section of your response, and number your points where appropriate."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The AI System Design section must include a novel mechanism for simulating linguistic relativity effects related to {t['language_feature']}.",
            f"The Cognitive Impact Analysis must provide at least two specific examples of how {t['language_feature']} might influence AI cognition in {t['cognitive_domain']}.",
            f"The Decision-Making Simulation must describe a detailed scenario in {t['decision_context']} and compare outcomes under at least two different linguistic frameworks.",
            "The Philosophical Implications section should discuss at least two distinct philosophical questions related to linguistic relativity in AI.",
            "The Ethical Considerations and Safeguards section must identify at least three potential ethical issues and propose specific safeguards.",
            "The overall response must demonstrate interdisciplinary knowledge, creativity, and critical thinking without relying on common examples or simplistic explanations."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
