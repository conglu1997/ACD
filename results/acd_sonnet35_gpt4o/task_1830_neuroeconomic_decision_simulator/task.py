import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "scenario": "Global Recession Recovery",
                "context": "Predicting consumer behavior and market trends during economic recovery from a global recession"
            },
            {
                "scenario": "Technological Disruption",
                "context": "Analyzing market reactions to a breakthrough in quantum computing that threatens current cryptographic systems"
            },
            {
                "scenario": "Climate Change Adaptation",
                "context": "Forecasting economic shifts and investment patterns in response to severe climate change impacts"
            },
            {
                "scenario": "Demographic Shift",
                "context": "Predicting economic consequences of rapid population aging in developed countries"
            },
            {
                "scenario": "Geopolitical Tension",
                "context": "Analyzing global market responses to increasing trade tensions between major economic powers"
            }
        ]
        return {
            "1": random.choice(scenarios),
            "2": random.choice(scenarios)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a neuroeconomic AI system that simulates human decision-making processes in complex economic scenarios, then apply it to predict and analyze global market trends for the following scenario: {t['scenario']} - {t['context']}. Your response should include:

1. System Architecture (300-350 words):
   a) Describe the key components of your neuroeconomic AI system.
   b) Explain how your system integrates neuroscientific principles, economic theories, and AI technologies.
   c) Detail how the system models human cognitive biases and emotional factors in decision-making.
   d) Include a diagram or flowchart of your system architecture using ASCII art or Unicode characters.

2. Data Integration and Processing (200-250 words):
   a) Describe the types of data your system would require (e.g., neuroimaging, economic indicators, market data).
   b) Explain how you would preprocess and integrate these diverse data types.
   c) Discuss any novel approaches to data fusion or feature extraction in your system.

3. Decision-Making Simulation (250-300 words):
   a) Explain how your system simulates human decision-making processes in economic contexts.
   b) Describe specific cognitive models or algorithms used in your simulation.
   c) Discuss how your system accounts for individual differences in decision-making styles.
   d) Provide an example of how the system would simulate a decision in the given scenario.

4. Market Trend Analysis (200-250 words):
   a) Describe how your system would use the simulated decisions to predict market trends.
   b) Explain your approach to aggregating individual decisions into macro-level predictions.
   c) Discuss how your system handles uncertainty and generates confidence intervals for its predictions.

5. Ethical Considerations (150-200 words):
   a) Discuss potential ethical issues in using AI to simulate and predict human economic behavior.
   b) Address concerns about privacy, manipulation, and the potential for market destabilization.
   c) Propose guidelines for the responsible development and use of neuroeconomic AI systems.

6. Limitations and Future Directions (150-200 words):
   a) Identify key limitations of your proposed system.
   b) Suggest potential improvements or extensions to address these limitations.
   c) Propose a research direction that could further advance the field of AI-driven neuroeconomics.

Ensure your response demonstrates a deep understanding of neuroscience, economics, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative in your approach while maintaining scientific plausibility.

Format your answer with clear headings for each section, numbered as above. Your total response should be between 1250-1550 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of neuroscience, economics, and artificial intelligence.",
            "The proposed system integrates principles from multiple disciplines in a coherent and innovative way.",
            "The decision-making simulation and market trend analysis are well-explained and scientifically plausible.",
            "Ethical considerations are thoroughly addressed, with thoughtful guidelines proposed.",
            "The response includes creative solutions while maintaining scientific accuracy.",
            "All sections are completed as instructed, with clear headings and appropriate length."
        ]
        return float(eval_with_llm_judge(instructions, submission, criteria))