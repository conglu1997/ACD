class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            '1': {
                'initial_scenario': 'You are tasked with managing a forest ecosystem. Recently, a new species of herbivore has been introduced. Predict the potential impacts on the ecosystem over the next five years. Consider factors such as plant populations, predator-prey relationships, and biodiversity.',
                'followups': {
                    'increase_predators': 'In response to the herbivore population increase, you decide to introduce more predators. Predict the impact of this intervention on the herbivore population, plant populations, and overall ecosystem health over the next five years.',
                    'no_intervention': 'You decide to allow the ecosystem to adapt without intervention. Predict the long-term impacts of the herbivore introduction on plant populations, native herbivores, and overall biodiversity over the next five years.'
                }
            },
            '2': {
                'initial_scenario': 'You are managing a coastal marine ecosystem. Due to climate change, water temperatures are rising. Predict the potential impacts on coral reefs, fish populations, and overall marine biodiversity over the next decade.',
                'followups': {
                    'introduce_resistant_species': 'To combat coral bleaching, you decide to introduce coral species that are more resistant to temperature changes. Predict the impact of this intervention on the existing coral reefs, fish populations, and overall ecosystem stability over the next decade.',
                    'no_intervention': 'Deciding not to intervene, predict the long-term impacts of rising water temperatures on coral reefs, fish populations, and marine biodiversity over the next decade.'
                }
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Simulate the following ecosystem scenario by predicting the impacts of the given changes. Your predictions should be based on a thorough understanding of ecological interactions and dynamics. Here is the initial scenario:

{t['initial_scenario']}

Respond with your detailed predictions in the following format:
Prediction: [Your detailed predictions]

You will receive a follow-up scenario based on your choice that you must also address. Please maintain the format and depth of detail in your responses."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            'The predictions should logically follow from the scenario.',
            'The predictions should demonstrate an understanding of ecological interactions and dynamics.',
            'The response should be coherent, detailed, and logically structured.'
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
