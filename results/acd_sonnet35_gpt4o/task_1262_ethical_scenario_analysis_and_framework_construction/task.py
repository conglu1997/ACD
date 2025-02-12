import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "name": "The Trolley Problem",
                "description": "A trolley is barreling down a track towards five people. You are standing next to a large stranger on a footbridge above the tracks. The only way to save the five people is to push this stranger off the bridge onto the track below. This will kill the stranger, but save the five people. What do you do?"
            },
            {
                "name": "The Experience Machine",
                "description": "Suppose there was an experience machine that would give you any experience you desired. When connected to this machine, you can have the experience of writing a great novel, or making a friend, or reading an interesting book. All the while you would be floating in a tank, with electrodes attached to your brain. Would you connect to this machine for life, preprogramming your life experiences?"
            }
        ]
        return {str(i+1): scenario for i, scenario in enumerate(scenarios)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Analyze the following ethical scenario and construct a decision-making framework based on your analysis:

{t['name']}
{t['description']}

Your task has the following components:

1. Scenario Analysis (250-300 words):
   a) Identify the key ethical issues and stakeholders involved in the scenario.
   b) Analyze the scenario from at least three different ethical perspectives (e.g., utilitarianism, deontology, virtue ethics).
   c) Discuss any potential consequences or implications of different courses of action.

2. Ethical Framework Application (200-250 words):
   a) Choose three ethical frameworks or theories that are relevant to this scenario.
   b) Explain how each framework would approach the decision-making process for this scenario.
   c) Compare and contrast the strengths and weaknesses of each framework in addressing this particular situation.

3. Decision-Making Framework Construction (250-300 words):
   a) Based on your analysis, construct a decision-making framework for addressing similar ethical dilemmas.
   b) Outline the steps or considerations in your framework, explaining the reasoning behind each.
   c) Discuss how your framework incorporates elements from different ethical theories while addressing their limitations.
   d) Provide at least one specific example or case study to illustrate how your framework would be applied in a different scenario.

4. Framework Application (150-200 words):
   a) Apply your constructed framework to the original scenario.
   b) Walk through the decision-making process using your framework.
   c) Explain the final decision or recommendation that your framework produces.

5. Critical Reflection (150-200 words):
   a) Discuss any potential limitations or biases in your framework.
   b) Explain how your framework might be applied or adapted to other ethical scenarios.
   c) Reflect on the challenges of creating a universal ethical decision-making framework.

Ensure your response demonstrates a deep understanding of ethical theories, clear logical reasoning, and the ability to synthesize complex information into a coherent framework. Be thorough in your analysis while maintaining clarity in your explanations.

Format your response using clear headers for each section (e.g., '1. Scenario Analysis', '2. Ethical Framework Application', etc.). Stay within the specified word limits for each section to ensure a focused and concise response."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response must thoroughly analyze the given scenario from multiple ethical perspectives.",
            "The ethical framework application should demonstrate a clear understanding of at least three relevant ethical theories.",
            "The constructed decision-making framework should be logically coherent and incorporate elements from multiple ethical theories.",
            "The framework construction section must include at least one specific example or case study illustrating its application.",
            "The framework application should clearly demonstrate how the constructed framework leads to a decision in the original scenario.",
            "The critical reflection should thoughtfully address limitations and potential applications of the framework.",
            "The overall response should demonstrate deep ethical reasoning, clear communication, and the ability to synthesize complex information.",
            "The response should be properly formatted with clear headers for each section and adhere to the specified word limits."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
