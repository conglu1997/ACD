import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cognitive_processes = [
            'divergent thinking',
            'conceptual blending',
            'analogical reasoning',
            'constraint relaxation',
            'incubation and insight'
        ]
        creative_domains = [
            'visual arts',
            'music composition',
            'creative writing',
            'scientific discovery',
            'architectural design'
        ]
        ai_techniques = [
            'neural networks',
            'genetic algorithms',
            'reinforcement learning',
            'probabilistic graphical models',
            'transformer models'
        ]
        
        tasks = {
            "1": {
                "cognitive_process": random.choice(cognitive_processes),
                "creative_domain": random.choice(creative_domains),
                "ai_technique": random.choice(ai_techniques)
            },
            "2": {
                "cognitive_process": random.choice(cognitive_processes),
                "creative_domain": random.choice(creative_domains),
                "ai_technique": random.choice(ai_techniques)
            }
        }
        
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that simulates and enhances human creativity by mimicking the cognitive process of {t['cognitive_process']}. Apply this system to enhance creativity in the domain of {t['creative_domain']}, incorporating the AI technique of {t['ai_technique']}. Your response should include the following sections:

1. Cognitive Process Analysis (200-250 words):
   a) Explain the key principles of {t['cognitive_process']} and its role in human creativity.
   b) Describe how this process contributes to creative thinking in {t['creative_domain']}.
   c) Identify the main challenges in computationally modeling this cognitive process.

2. AI System Architecture (250-300 words):
   a) Provide a high-level overview of your AI system's architecture.
   b) Explain how your system incorporates {t['ai_technique']} to model {t['cognitive_process']}.
   c) Describe how your system interacts with human users to enhance their creativity.
   d) Discuss how your system maintains a balance between mimicking human cognition and leveraging AI capabilities.

3. Application in {t['creative_domain']} (200-250 words):
   a) Explain how your AI system would be applied specifically in {t['creative_domain']}.
   b) Describe the inputs, processes, and outputs of your system in this creative context.
   c) Provide an example of how your system might enhance a specific creative task in this domain.

4. Creativity Enhancement Mechanisms (200-250 words):
   a) Describe specific mechanisms by which your system enhances human creativity.
   b) Explain how these mechanisms relate to the cognitive process of {t['cognitive_process']}.
   c) Discuss how your system might overcome creative blocks or biases that humans typically face.

5. Evaluation and Validation (150-200 words):
   a) Propose methods for evaluating the effectiveness of your system in enhancing creativity.
   b) Discuss the challenges in measuring creativity enhancement and how you would address them.
   c) Suggest ways to validate that the system is truly enhancing creativity rather than simply automating creative tasks.

6. Ethical Considerations (150-200 words):
   a) Identify potential ethical issues raised by an AI system that enhances human creativity.
   b) Discuss the implications for intellectual property and authorship.
   c) Propose guidelines for the responsible development and use of creativity-enhancing AI.

7. Future Directions (100-150 words):
   a) Suggest two potential improvements or extensions to your system.
   b) Discuss how this technology might evolve and impact creative processes in the future.

Ensure your response demonstrates a deep understanding of cognitive science, artificial intelligence, and the specific creative domain. Use appropriate terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1250-1600 words.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of {t['cognitive_process']} and its role in creativity.",
            f"The AI system architecture effectively incorporates {t['ai_technique']} to model {t['cognitive_process']}.",
            f"The application in {t['creative_domain']} is well-explained and demonstrates domain-specific knowledge.",
            "The creativity enhancement mechanisms are innovative and well-grounded in cognitive science.",
            "The evaluation and validation methods are appropriate and comprehensive.",
            "Ethical considerations are thoughtfully addressed.",
            "The response is creative and original while maintaining scientific plausibility.",
            "The writing is clear, well-structured, and adheres to the specified word counts and format."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
