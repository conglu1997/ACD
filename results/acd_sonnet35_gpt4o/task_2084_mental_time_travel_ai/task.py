import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        time_directions = ['past', 'future']
        cognitive_aspects = ['episodic memory', 'semantic memory', 'prospection', 'theory of mind']
        applications = ['therapeutic interventions', 'decision-making support', 'creative problem-solving', 'historical analysis']
        
        return {
            "1": {
                "time_direction": random.choice(time_directions),
                "cognitive_aspect": random.choice(cognitive_aspects),
                "application": random.choice(applications)
            },
            "2": {
                "time_direction": random.choice(time_directions),
                "cognitive_aspect": random.choice(cognitive_aspects),
                "application": random.choice(applications)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system capable of simulating mental time travel, focusing on {t['time_direction']} projection and emphasizing the cognitive aspect of {t['cognitive_aspect']}. Your response should address the following:

1. System Architecture (250-300 words):
   a) Describe the key components of your AI system for mental time travel simulation.
   b) Explain how it integrates principles from cognitive science, neuroscience, and AI.
   c) Detail how your system simulates {t['cognitive_aspect']} in the context of {t['time_direction']} mental projection.
   d) Discuss any novel technologies or theoretical concepts your system employs.

2. Cognitive Process Simulation (200-250 words):
   a) Explain how your system simulates the process of mental time travel to the {t['time_direction']}.
   b) Describe how it handles the complexity of {t['cognitive_aspect']} in this context.
   c) Discuss how your system addresses challenges specific to {t['time_direction']} mental projection.

3. Concrete Example (100-150 words):
   Provide a specific example of how your system would operate in a given scenario, demonstrating its mental time travel capabilities.

4. Comparison to Existing Architectures (100-150 words):
   Compare your proposed system to at least two existing cognitive architectures, highlighting key differences and potential advantages.

5. Implications for AI Consciousness (200-250 words):
   a) Analyze how the ability to perform mental time travel might contribute to AI consciousness.
   b) Discuss how simulating {t['cognitive_aspect']} relates to self-awareness and sentience in AI.
   c) Compare your approach to existing theories of machine consciousness.

6. Potential Application (150-200 words):
   a) Describe how your system could be applied to {t['application']}.
   b) Explain the potential benefits and challenges of using mental time travel AI in this context.
   c) Discuss any ethical considerations specific to this application.

7. Evaluation and Validation (150-200 words):
   a) Propose methods to evaluate the accuracy and effectiveness of your system's mental time travel simulations.
   b) Suggest experiments to validate your system's performance in simulating {t['cognitive_aspect']}.
   c) Discuss potential challenges in verifying the authenticity of AI-generated past or future scenarios.

8. Ethical and Philosophical Implications (200-250 words):
   a) Discuss the ethical implications of creating AI systems capable of mental time travel.
   b) Analyze potential impacts on concepts of free will, determinism, and the nature of consciousness.
   c) Propose guidelines for responsible development and use of mental time travel AI systems.

Ensure your response demonstrates a deep understanding of cognitive science, AI, and philosophy of mind. Be creative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section. Your total response should be between 1350-1750 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response adequately addresses mental time travel to the {t['time_direction']}.",
            f"The system design incorporates and emphasizes {t['cognitive_aspect']}.",
            f"The potential application to {t['application']} is thoroughly explored.",
            "The response demonstrates a deep understanding of cognitive science, AI, and philosophy of mind.",
            "The ethical and philosophical implications are thoughtfully analyzed.",
            "The proposed evaluation methods are appropriate and well-reasoned.",
            "The response is creative while maintaining scientific plausibility.",
            "A concrete example of the system's operation is provided.",
            "The proposed system is compared to at least two existing cognitive architectures.",
            "The total response is between 1350-1750 words."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
