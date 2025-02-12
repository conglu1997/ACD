import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        philosophical_traditions = [
            "Western Analytic",
            "Eastern Buddhism",
            "African Ubuntu",
            "Indigenous Australian Dreamtime"
        ]
        cognitive_tasks = [
            "Ethical Dilemma Resolution",
            "Scientific Theory Formation",
            "Artistic Creation",
            "Social Conflict Mediation"
        ]
        
        return {
            "1": {"tradition": random.choice(philosophical_traditions), "task": random.choice(cognitive_tasks)},
            "2": {"tradition": random.choice(philosophical_traditions), "task": random.choice(cognitive_tasks)}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that simulates a cognitive framework based on the {t['tradition']} philosophical tradition, and analyze how this framework influences the AI's approach to {t['task']}. Your response should include:

1. Philosophical Framework (250-300 words):
   a) Summarize the key principles and concepts of the {t['tradition']} philosophical tradition.
   b) Explain how these principles shape cognition, perception, and reasoning.
   c) Discuss any unique features of this tradition that might challenge conventional AI approaches.

2. AI System Architecture (300-350 words):
   a) Describe the key components of your AI system that enable the simulation of this philosophical cognitive framework.
   b) Explain how your system models the core concepts and reasoning patterns of the tradition.
   c) Discuss how you integrate this framework into the AI's decision-making and problem-solving processes.
   d) Address any technical challenges in implementing this philosophical approach in an AI system.

3. Task Analysis (300-350 words):
   a) Describe how your AI system, operating under the {t['tradition']} framework, would approach the task of {t['task']}.
   b) Provide a step-by-step breakdown of the AI's problem-solving or decision-making process for this task.
   c) Highlight how this approach differs from conventional AI methods for similar tasks.
   d) Present a specific example or case study demonstrating your AI system's approach to the given task.

4. Comparative Analysis (250-300 words):
   a) Compare how your AI system might perform on the given task compared to an AI using a different philosophical framework.
   b) Discuss potential advantages and limitations of the {t['tradition']} approach for this type of task.
   c) Analyze how this philosophical framework might influence the AI's biases, strengths, or blind spots.
   d) Explore potential synergies or conflicts between this approach and other philosophical traditions in AI.

5. Ethical and Societal Implications (150-200 words):
   a) Discuss the ethical considerations of implementing diverse philosophical frameworks in AI systems.
   b) Explore potential societal impacts of AI systems that can simulate different cultural or philosophical perspectives.
   c) Propose guidelines for responsible development and use of such philosophically diverse AI systems.

6. Future Research Directions (150-200 words):
   a) Suggest two specific research questions or experiments to further explore the potential of your philosophical cognition simulator.
   b) Discuss how this approach might contribute to the development of more culturally aware and ethically aligned AI systems.
   c) Address potential limitations or challenges of your proposed AI system and suggest ways to overcome them.

Ensure your response demonstrates a deep understanding of the chosen philosophical tradition, artificial intelligence, and cognitive science. Use appropriate technical terminology and provide clear explanations where necessary. Be creative in your approach while maintaining scientific plausibility and addressing potential limitations or challenges.

Format your response with clear headings for each section. Your total response should be between 1400-1700 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response should demonstrate a deep understanding of the {t['tradition']} philosophical tradition and its application to AI cognition.",
            f"The AI system design should credibly incorporate key principles of the {t['tradition']} tradition into its cognitive framework.",
            f"The analysis of the AI's approach to {t['task']} should be logically consistent with the philosophical framework and highlight unique aspects of this approach.",
            "The response should include a specific example or case study demonstrating the AI system's approach to the given task.",
            "The comparative analysis should provide insightful contrasts between different philosophical approaches in AI.",
            "The response should address ethical implications, future research directions, and potential limitations thoughtfully.",
            "The overall response should be creative, scientifically plausible, and demonstrate strong interdisciplinary knowledge integration."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
