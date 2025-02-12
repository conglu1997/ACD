import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cognitive_processes = [
            "working memory",
            "attention allocation",
            "decision making under uncertainty",
            "language acquisition",
            "emotional regulation",
            "spatial navigation",
            "concept formation",
            "social cognition"
        ]
        application_domains = [
            "educational technology",
            "mental health interventions",
            "human-computer interaction",
            "autonomous vehicles",
            "personalized medicine",
            "crisis management systems",
            "creative AI assistants",
            "ethical AI decision-making"
        ]
        return {
            "1": {
                "cognitive_process": random.choice(cognitive_processes),
                "application_domain": random.choice(application_domains)
            },
            "2": {
                "cognitive_process": random.choice(cognitive_processes),
                "application_domain": random.choice(application_domains)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that models the cognitive process of {t['cognitive_process']} and demonstrate its application in the domain of {t['application_domain']}. Your response should include the following sections:

1. Cognitive Process Analysis (200-250 words):
   a) Describe the key features and mechanisms of {t['cognitive_process']} in human cognition.
   b) Discuss relevant theories or models from cognitive psychology and neuroscience.
   c) Identify specific aspects that are crucial for computational modeling.

2. AI System Design (250-300 words):
   a) Propose an innovative AI architecture to model {t['cognitive_process']}.
   b) Explain how your system incorporates key features of the cognitive process.
   c) Describe the main components, algorithms, or neural network structures in your model.
   d) Include a simple diagram or flowchart of your AI system (use ASCII art).
   e) Cite at least two relevant research papers or theories that support your design choices.

3. Computational Implementation (200-250 words):
   a) Outline the key steps for implementing your AI system.
   b) Discuss potential challenges in translating the cognitive process into a computational model.
   c) Propose methods to validate your model against human cognitive data.

4. Application in {t['application_domain']} (200-250 words):
   a) Describe how your AI system could be applied in the domain of {t['application_domain']}.
   b) Discuss potential benefits and limitations of using this model in this application.
   c) Propose a specific use case and explain its potential impact.

5. Implications for Human Cognition (150-200 words):
   a) Discuss how your AI model might provide insights into human {t['cognitive_process']}.
   b) Identify aspects of the cognitive process that your model illuminates or fails to capture.
   c) Propose a hypothesis about human cognition based on your model's behavior.

6. Ethical Considerations (150-200 words):
   a) Discuss potential ethical issues in modeling {t['cognitive_process']} and applying it to {t['application_domain']}.
   b) Propose guidelines for responsible development and use of such AI systems.
   c) Discuss potential societal implications of widespread use of this technology.

7. Limitations and Future Work (100-150 words):
   a) Acknowledge the limitations of your proposed AI system.
   b) Suggest areas for future research or improvements to address these limitations.

Ensure your response demonstrates a deep understanding of cognitive psychology, neuroscience, and artificial intelligence. Use appropriate terminology and provide clear explanations where necessary. Be creative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1250-1600 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must include a well-structured AI system design for modeling {t['cognitive_process']}.",
            f"The analysis should demonstrate a deep understanding of {t['cognitive_process']} from both cognitive psychology and neuroscience perspectives.",
            f"The computational implementation section should provide a clear and feasible approach to translating the cognitive model into an AI system.",
            f"The application in {t['application_domain']} should be innovative and well-reasoned.",
            "The response must include all seven required sections with appropriate content and adherence to word limits.",
            "The proposed AI system and its analysis should be creative yet scientifically plausible and grounded in current understanding of cognitive processes and AI capabilities.",
            "The response should cite at least two relevant research papers or theories to support the AI system design.",
            "The limitations of the proposed AI system should be clearly acknowledged and addressed."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
