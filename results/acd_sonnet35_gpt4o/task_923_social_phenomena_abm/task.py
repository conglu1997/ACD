import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "phenomenon": "Information spread and opinion formation in social networks",
                "key_factors": ["network structure", "individual bias", "information source credibility"],
                "policy_goal": "Mitigate the spread of misinformation"
            },
            {
                "phenomenon": "Urban segregation and neighborhood formation",
                "key_factors": ["income inequality", "racial preferences", "housing policies"],
                "policy_goal": "Promote diverse and integrated communities"
            }
        ]
        return {
            "1": random.choice(scenarios),
            "2": random.choice(scenarios)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design and implement an agent-based model (ABM) to simulate the complex social phenomenon of {t['phenomenon']}. An ABM is a computational model that simulates the actions and interactions of autonomous agents to understand the behavior of a system as a whole. Your task has five parts:

1. Model Design (300 words):
   a) Describe the key components of your ABM, including agent types and their attributes. (100 words)
   b) Explain how you will incorporate the key factors: {', '.join(t['key_factors'])}. (100 words)
   c) Outline the rules governing agent interactions and decision-making processes. (100 words)

2. Implementation Details (250 words):
   a) Provide pseudocode for the main simulation loop and one key agent behavior. (150 words)
   b) Explain how you will initialize the model and set up initial conditions. (100 words)

3. Data Collection and Analysis (250 words):
   a) Specify three key metrics you will collect from the simulation and explain their importance. (100 words)
   b) Describe two statistical methods or analytical techniques you will use to analyze the results. (100 words)
   c) Propose one novel metric or analytical technique specific to {t['phenomenon']}. (50 words)

4. Results Interpretation (250 words):
   a) Present a hypothetical set of results from your simulation, including trends for your key metrics. (100 words)
   b) Interpret these results in the context of the social phenomenon being studied. (100 words)
   c) Discuss one potential emergent behavior or unexpected outcome from the simulation. (50 words)

5. Policy Recommendations (200 words):
   a) Based on your simulation results, propose two specific policy interventions to address the goal: {t['policy_goal']}. (100 words)
   b) Explain the rationale behind each intervention and how it relates to the simulation outcomes. (100 words)

Ensure your response demonstrates an understanding of agent-based modeling, the specific social phenomenon, and relevant social science theories. Use technical terminology appropriately and provide explanations where necessary. Be creative in your approach while maintaining scientific plausibility.

Please structure your response with clear headings for each of the five main sections, and use subheadings for each sub-task."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The model design includes agent types, key factors, and interaction rules.",
            "The implementation details provide clear pseudocode and initialization procedures.",
            "The data collection and analysis plan includes relevant metrics and analytical techniques.",
            "The results interpretation presents plausible hypothetical outcomes and insightful analysis.",
            "The policy recommendations are specific and well-justified based on the simulation outcomes.",
            "The overall response demonstrates understanding of ABM and the specific social phenomenon."
        ]
        score = sum([1/6 for c in criteria if eval_with_llm_judge(instructions, submission, [c])])
        return min(1.0, max(0.0, score))  # Ensure the score is between 0 and 1, inclusive
