import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        organisms = [
            {
                "name": "Photosynthetic Plastic Decomposer",
                "capability": "Efficiently break down plastic waste while generating oxygen",
                "example_component": "Modified chloroplasts for enhanced photosynthesis and plastic degradation"
            },
            {
                "name": "Carbon-Capturing Microbe",
                "capability": "Rapidly absorb atmospheric CO2 and convert it into stable organic compounds",
                "example_component": "Engineered carbonic anhydrase enzyme for improved CO2 absorption"
            }
        ]
        return {
            "1": random.choice(organisms),
            "2": random.choice(organisms)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a synthetic organism called the {t['name']} with the capability to {t['capability']}. Then, analyze its potential impacts and develop an ethical framework for its implementation. Your response should include:

1. Organism Design (300-350 words):
   a) Describe the key biological components and mechanisms of your synthetic organism. Include at least one component similar to the example: {t['example_component']}.
   b) Explain how you would engineer the organism to achieve its specified capability.
   c) Discuss any potential safeguards or control mechanisms built into the organism's design.
   d) Identify at least two challenges in creating this organism and propose solutions.

2. Environmental Impact Analysis (250-300 words):
   a) Predict three potential positive effects of releasing this organism into the environment.
   b) Identify three potential negative consequences or risks associated with its release.
   c) Describe how the organism might interact with existing ecosystems and biodiversity.
   d) Propose a method to monitor and measure the organism's impact over time.

3. Societal Implications (250-300 words):
   a) Analyze how this synthetic organism could affect at least three different sectors of society (e.g., economy, public health, agriculture).
   b) Discuss potential public perceptions and concerns about the organism.
   c) Explain how the organism's capabilities might influence policy-making or regulations.
   d) Identify any potential dual-use concerns or security risks associated with the organism.

4. Ethical Framework (300-350 words):
   a) Develop a set of ethical guidelines for the development, testing, and release of this synthetic organism.
   b) Address issues of consent, risk assessment, and benefit distribution in your framework.
   c) Propose a decision-making process for determining whether and how to implement the organism.
   d) Discuss how to balance potential benefits against risks and ethical concerns.

5. Future Scenarios (200-250 words):
   a) Describe a best-case scenario for the long-term impact of your synthetic organism.
   b) Outline a worst-case scenario and propose preventive measures or contingency plans.
   c) Suggest two potential adaptations or improvements for the organism based on your analysis.

Ensure your response demonstrates a deep understanding of synthetic biology, ecological systems, and ethical reasoning. Use scientific terminology appropriately and provide explanations where necessary. Be creative in your approach while maintaining biological plausibility and addressing real-world concerns.

Format your response with clear headings for each section and use subheadings (a, b, c, d) as outlined above. Your total response should be between 1300-1550 words. Include a word count at the end of your response."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "Demonstrates comprehensive understanding of synthetic biology principles",
            "Provides a plausible and detailed design for the specified synthetic organism, including the example component or a similar one",
            "Analyzes both positive and negative environmental impacts with specific examples",
            "Discusses societal implications across at least three different sectors",
            "Develops a comprehensive ethical framework addressing all required points",
            "Addresses future scenarios with detailed best-case and worst-case analyses",
            "Shows creativity and innovation while maintaining scientific plausibility",
            "Properly uses scientific terminology and provides clear explanations for complex concepts",
            "Addresses all required points in each section using the specified subheadings",
            "Stays within the specified word count range (1300-1550 words) and includes a word count",
            "Presents a well-structured response with clear headings and subheadings as outlined"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
