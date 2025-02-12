import random
import math

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        languages = ['English', 'Mandarin', 'Spanish', 'Arabic']
        linguistic_features = ['Phonology', 'Syntax', 'Lexicon', 'Morphology']
        time_spans = [50, 100, 200]
        
        tasks = [
            {
                'language': random.choice(languages),
                'linguistic_feature': random.choice(linguistic_features),
                'time_span': random.choice(time_spans)
            } for _ in range(2)
        ]
        
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Create a mathematical model of language evolution using dynamical systems theory and apply it to predict future changes in {t['language']}, focusing on the linguistic feature of {t['linguistic_feature']}. Your task has the following parts:

1. Dynamical Systems Model (250-300 words):
   a) Design a dynamical system model to represent the evolution of {t['linguistic_feature']} in {t['language']}.
   b) Define the state variables, parameters, and equations that govern the system.
   c) Explain how your model captures key aspects of language change, such as internal and external factors influencing evolution.
   d) Provide a visual representation of your model using ASCII art or a clear textual description.

Note: Dynamical systems theory studies the long-term behavior of systems that change over time. For example, a simple dynamical system might be described by the equation x(t+1) = ax(t)(1-x(t)), where x(t) represents the state of the system at time t, and 'a' is a parameter. Your model should be more complex and specific to language evolution.

2. Mathematical Formulation (200-250 words):
   a) Provide the mathematical equations for your model, using appropriate notation from dynamical systems theory.
   b) Explain the meaning and significance of each term in your equations.
   c) Describe any assumptions or simplifications made in your model.

3. Linguistic Grounding (150-200 words):
   a) Explain how your model relates to established theories of language change in linguistics.
   b) Provide examples of how specific linguistic phenomena in {t['language']} are represented in your model.

4. Predictive Analysis (200-250 words):
   a) Use your model to predict changes in {t['linguistic_feature']} of {t['language']} over the next {t['time_span']} years.
   b) Describe the predicted changes and explain the reasoning behind them based on your model.
   c) Provide a specific example of a predicted change, including the initial state and the projected future state.
   d) Discuss any potential bifurcations or phase transitions in your model and their linguistic implications.

5. Model Evaluation (150-200 words):
   a) Propose a method to validate your model using historical linguistic data.
   b) Discuss potential limitations of your model and suggest ways to address them.
   c) Explain how your model could be extended to incorporate other linguistic features or languages.

6. Ethical Implications (100-150 words):
   a) Discuss the potential ethical implications of using such a model for language prediction.
   b) Consider issues such as linguistic diversity, language policy, and potential misuse of the model.
   c) Propose guidelines for the responsible use of your model in linguistic research and policy-making.

Ensure your response demonstrates a deep understanding of both dynamical systems theory and linguistics. Use technical terminology appropriately and provide explanations where necessary. Be creative in your approach while maintaining scientific plausibility and mathematical rigor.

Format your response using clear headings for each section. Strive for clarity and coherence throughout your response, ensuring that each part connects logically to the others."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response includes a well-designed dynamical system model for language evolution (0.2 points)",
            "The mathematical formulation is clear and appropriate for the proposed model (0.2 points)",
            "The model is grounded in linguistic theory and accurately represents aspects of language change (0.1 points)",
            f"The predictive analysis provides plausible changes in {t['linguistic_feature']} of {t['language']} over {t['time_span']} years, including a specific example (0.2 points)",
            "The response includes a thoughtful evaluation of the model, including validation methods and limitations (0.1 points)",
            "The response includes a visual representation of the dynamical system model (0.1 points)",
            "The ethical implications of the model are discussed, with proposed guidelines for responsible use (0.1 points)"
        ]
        score = sum([float(eval_with_llm_judge(instructions, submission, [criterion])) * float(criterion.split('(')[1].split(' ')[0]) for criterion in criteria])
        return round(score, 1)
