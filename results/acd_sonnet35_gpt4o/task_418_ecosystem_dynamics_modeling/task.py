import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        ecosystems = [
            {
                "name": "Floating Sky Islands",
                "description": "A series of floating islands in the sky, each with its own microclimate and species.",
                "key_species": ["Sky Whales", "Cloudberry Bushes", "Wind Serpents", "Floating Fungi"]
            },
            {
                "name": "Subterranean Crystal Caverns",
                "description": "A vast network of underground caverns illuminated by bioluminescent crystals.",
                "key_species": ["Crystal Bats", "Glowworm Colonies", "Blind Cave Fish", "Luminous Lichen"]
            },
            {
                "name": "Temporal Forest",
                "description": "A forest where different areas experience different rates of time passage.",
                "key_species": ["Chrono-Oaks", "Time-Shifting Deer", "Epoch Butterflies", "Ageless Moss"]
            }
        ]
        return {str(i+1): ecosystem for i, ecosystem in enumerate(random.sample(ecosystems, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Model the fictional ecosystem of the {t['name']} and analyze its dynamics. Your task has the following parts:

1. Ecosystem Modeling (200-250 words):
   a) Describe the key components and interactions within the {t['name']} ecosystem.
   b) Explain how energy flows through the system and how key species interact.
   c) Identify at least one keystone species and explain its role in the ecosystem.

2. Dynamic Prediction (150-200 words):
   a) Predict how the ecosystem might evolve over the next 100 years if left undisturbed.
   b) Identify potential tipping points or critical thresholds in the system.

3. External Pressure Analysis (100-150 words):
   a) Introduce a significant external pressure (e.g., climate change, invasive species) to the ecosystem.
   b) Analyze how this pressure would affect the ecosystem's dynamics and stability.

4. Intervention Design (150-200 words):
   a) Propose three possible interventions to maintain the ecosystem's stability in face of the external pressure.
   b) Explain the rationale behind each intervention and its potential cascading effects.

5. Adaptive Management Plan (100-150 words):
   a) Design a monitoring plan to track the ecosystem's health and the effectiveness of interventions.
   b) Describe how you would adjust your interventions based on monitoring results.

6. Conclusion (50-100 words):
   Summarize the key insights from your analysis and the potential long-term outlook for the ecosystem.

Ensure your response demonstrates a deep understanding of ecological principles, systems thinking, and the interconnectedness of ecosystem components. Be creative in your analysis and proposed solutions while maintaining scientific plausibility.

Format your response with clear headings for each section and use paragraphs for readability. Your total response should be between 750-1050 words, adhering to the word count for each section.

Key species to consider: {', '.join(t['key_species'])}"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a comprehensive understanding of ecosystem dynamics and interactions",
            "The ecosystem model is creative, coherent, and scientifically plausible",
            "The dynamic prediction and external pressure analysis show logical reasoning and systems thinking",
            "The proposed interventions are innovative, well-reasoned, and consider potential cascading effects",
            "The adaptive management plan demonstrates an understanding of ecological monitoring and feedback loops",
            f"The response effectively incorporates the key species: {', '.join(t['key_species'])}",
            "The conclusion summarizes key insights and provides a coherent long-term outlook",
            "The response adheres to the specified word counts and formatting guidelines"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
