import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "creative_field": "Visual Arts",
                "ethical_issue": "AI-generated art ownership",
                "futuristic_context": "Virtual reality museums"
            },
            {
                "creative_field": "Music",
                "ethical_issue": "Emotional manipulation through AI-composed music",
                "futuristic_context": "Brain-computer interfaces for music consumption"
            },
            {
                "creative_field": "Literature",
                "ethical_issue": "AI-authored works exploring controversial themes",
                "futuristic_context": "Personalized story generation based on reader's memories"
            },
            {
                "creative_field": "Architecture",
                "ethical_issue": "AI-designed buildings affecting human behavior",
                "futuristic_context": "Self-evolving smart cities"
            },
            {
                "creative_field": "Fashion Design",
                "ethical_issue": "AI-driven beauty standards and body modification",
                "futuristic_context": "Programmable, shape-shifting clothing"
            }
        ]
        return {
            "1": random.choice(scenarios),
            "2": random.choice(scenarios)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that generates and resolves complex ethical dilemmas in the field of {t['creative_field']}, focusing on the issue of {t['ethical_issue']} in the context of {t['futuristic_context']}. Then, analyze its decision-making process and implications. Your response should include:

1. AI System Architecture (250-300 words):
   a) Describe the key components of your AI system for generating and resolving ethical dilemmas.
   b) Explain how your system incorporates ethical frameworks and creative domain knowledge.
   c) Detail any novel algorithms or approaches used in your design.

2. Dilemma Generation (200-250 words):
   a) Explain how your AI system generates a complex ethical dilemma related to the given scenario.
   b) Provide an example of a specific dilemma your system might generate.
   c) Discuss how the system ensures the dilemma is both ethically challenging and relevant to the creative field.

3. Resolution Process (250-300 words):
   a) Describe the step-by-step process your AI system uses to analyze and resolve the generated dilemma.
   b) Explain how the system balances ethical considerations with creative and practical concerns.
   c) Discuss any potential biases or limitations in your system's approach to resolution.
   d) Include a specific example or scenario to illustrate your system's decision-making process.

4. Implications Analysis (200-250 words):
   a) Analyze the potential consequences of implementing your AI system's solution in the given futuristic context.
   b) Discuss how this might impact the creative field, society, and individual artists/creators.
   c) Consider any unintended consequences or ethical concerns that might arise from your system's decision-making.

5. Human-AI Collaboration (150-200 words):
   a) Propose a framework for how human experts in ethics and the creative field could collaborate with your AI system.
   b) Discuss the potential benefits and challenges of this collaboration.

6. Evaluation and Accountability (150-200 words):
   a) Suggest methods for evaluating the ethical soundness and creative merit of your AI system's solutions.
   b) Discuss how accountability could be ensured in cases where the AI's decisions lead to harmful outcomes.

Ensure your response demonstrates a deep understanding of ethics, the specified creative field, and AI systems. Be innovative in your approach while maintaining plausibility. Use appropriate terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section. Your total response should be between 1200-1500 words. Please include the word count for each section in parentheses at the end of the section."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a comprehensive understanding of AI systems, ethics, and the specified creative field.",
            "The proposed AI system architecture and dilemma resolution process are innovative yet plausible.",
            "The analysis of implications is thorough, considers multiple perspectives, and explicitly addresses ethical concerns.",
            "The response includes specific examples or scenarios to illustrate the AI system's decision-making process.",
            "The writing is clear, well-structured, and uses appropriate terminology.",
            "The response adheres to the specified word count guidelines."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
