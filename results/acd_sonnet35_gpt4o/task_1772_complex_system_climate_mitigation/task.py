import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "focus_area": "Urban transportation",
                "key_challenge": "Reducing carbon emissions while maintaining mobility",
                "constraint": "Limited public funding"
            },
            {
                "focus_area": "Agricultural practices",
                "key_challenge": "Balancing food security with environmental sustainability",
                "constraint": "Resistance to change from traditional farming communities"
            }
        ]
        return {str(i+1): scenario for i, scenario in enumerate(random.sample(scenarios, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a complex adaptive system to address climate change mitigation in the area of {t['focus_area']}, with a focus on {t['key_challenge']}. Your system must operate under the constraint of {t['constraint']}. Your response should include the following sections:

1. System Overview (250-300 words):
   a) Describe the key components of your complex adaptive system.
   b) Explain how these components interact and adapt over time.
   c) Discuss how your system addresses the key challenge while operating under the given constraint.

2. Emergence and Self-Organization (200-250 words):
   a) Explain how emergent properties arise from the interactions within your system.
   b) Describe how self-organization contributes to the system's ability to mitigate climate change.
   c) Provide an example of how the system might adapt to an unexpected environmental or social change.

3. Feedback Loops and Tipping Points (200-250 words):
   a) Identify and explain at least two important feedback loops in your system.
   b) Discuss potential tipping points that could lead to significant changes in the system's behavior.
   c) Propose strategies to leverage positive feedback loops and mitigate negative ones.

4. Multi-Scale Interactions (200-250 words):
   a) Describe how your system operates across different scales (e.g., individual, community, national, global).
   b) Explain how actions at one scale influence outcomes at other scales.
   c) Discuss the challenges of coordinating actions across these different scales.

5. Modeling and Simulation (150-200 words):
   a) Propose a method for modeling and simulating your complex adaptive system.
   b) Discuss the key variables and parameters that would need to be included in the model.
   c) Explain how the results of such simulations could inform policy decisions.

6. Ethical Considerations (150-200 words):
   a) Identify potential ethical issues or unintended consequences that could arise from implementing your system.
   b) Discuss how these ethical concerns could be addressed or mitigated.
   c) Propose guidelines for the responsible development and management of your system.

7. Long-Term Impacts and Adaptability (150-200 words):
   a) Speculate on the potential long-term impacts of your system over a 50-year timeframe.
   b) Discuss how your system could adapt to changing environmental, social, and technological conditions over time.
   c) Propose a mechanism for regularly evaluating and updating the system to ensure its continued effectiveness.

Ensure your response demonstrates a deep understanding of complex systems theory, climate science, and relevant social and economic factors. Be creative in your approach while maintaining scientific plausibility and addressing real-world constraints. Use appropriate terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1300-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of complex systems theory and its application to climate change mitigation",
            "The proposed system effectively addresses the given key challenge while operating under the specified constraint",
            "The response includes creative and plausible solutions that span multiple domains (environmental, social, economic)",
            "The analysis of emergence, self-organization, feedback loops, and tipping points is thorough and insightful",
            "The discussion of multi-scale interactions and long-term impacts shows an understanding of the complexities involved in addressing climate change",
            "Ethical considerations and potential unintended consequences are thoughtfully addressed",
            "The response is well-structured, clear, and within the specified word limit"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
