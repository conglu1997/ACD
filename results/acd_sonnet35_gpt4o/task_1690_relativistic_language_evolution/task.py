import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        relativistic_effects = ['time dilation', 'length contraction', 'relativity of simultaneity']
        linguistic_features = ['phonology', 'morphology', 'syntax', 'semantics']
        communication_scenarios = ['interstellar colonization', 'first contact', 'time-delayed diplomacy']
        
        return {
            "1": {
                "relativistic_effect": random.choice(relativistic_effects),
                "linguistic_feature": random.choice(linguistic_features),
                "communication_scenario": random.choice(communication_scenarios)
            },
            "2": {
                "relativistic_effect": random.choice(relativistic_effects),
                "linguistic_feature": random.choice(linguistic_features),
                "communication_scenario": random.choice(communication_scenarios)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a language evolution simulation that incorporates the principle of {t['relativistic_effect']} from special relativity, focusing on its effects on {t['linguistic_feature']}. Then, analyze the implications of this simulation for {t['communication_scenario']}. Your response should include:

1. Simulation Design (300-350 words):
   a) Describe the key components and mechanisms of your language evolution simulation.
   b) Explain how {t['relativistic_effect']} is integrated into the simulation.
   c) Detail how the simulation models changes in {t['linguistic_feature']} over time.
   d) Provide a simple example or scenario illustrating how your simulation works.

2. Relativistic Linguistics Analysis (250-300 words):
   a) Analyze how {t['relativistic_effect']} influences the evolution of {t['linguistic_feature']}.
   b) Discuss potential linguistic phenomena that might emerge due to relativistic effects.
   c) Compare your relativistic language evolution model to traditional historical linguistics models.

3. Interstellar Communication Implications (250-300 words):
   a) Explore the consequences of your simulation for {t['communication_scenario']}.
   b) Discuss challenges and potential solutions for effective communication under relativistic conditions.
   c) Propose a communication protocol or system that accounts for relativistic language evolution.

4. Thought Experiment (200-250 words):
   a) Describe a hypothetical scenario where two civilizations attempt to communicate using your relativistic language model.
   b) Analyze potential misunderstandings or novel linguistic phenomena that might arise.
   c) Discuss the philosophical implications of relativistic effects on language and meaning.

5. Scientific and Technological Considerations (150-200 words):
   a) Identify key scientific or technological challenges in implementing or testing your model.
   b) Propose methods for empirically validating predictions made by your simulation.
   c) Discuss how advancements in physics or linguistics might refine or alter your model.

Ensure your response demonstrates a deep understanding of both linguistics and special relativity. Be creative in your approach while maintaining scientific plausibility. Use appropriate terminology from both fields and provide clear explanations where necessary.

Your total response should be between 1150-1400 words. Use clear headings for each section and number your paragraphs within each section."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The simulation design clearly incorporates {t['relativistic_effect']} and models changes in {t['linguistic_feature']}.",
            "The analysis demonstrates a deep understanding of both linguistics and special relativity.",
            f"The implications for {t['communication_scenario']} are thoroughly explored and logically derived from the simulation.",
            "The thought experiment is creative, plausible, and illustrates key concepts effectively.",
            "Scientific and technological considerations are addressed with insight and critical thinking.",
            "The response is well-structured, using appropriate terminology and clear explanations.",
            "The total response is between 1150-1400 words and follows the specified format."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
