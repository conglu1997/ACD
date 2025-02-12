import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        biological_systems = [
            "spider silk",
            "lotus leaf",
            "gecko feet",
            "shark skin",
            "butterfly wings"
        ]
        engineering_challenges = [
            "material strength",
            "water repellency",
            "adhesion",
            "drag reduction",
            "color without pigments"
        ]
        application_domains = [
            "aerospace",
            "architecture",
            "medical devices",
            "transportation",
            "energy production"
        ]
        return {
            "1": {
                "biological_system": random.choice(biological_systems),
                "engineering_challenge": random.choice(engineering_challenges),
                "application_domain": random.choice(application_domains)
            },
            "2": {
                "biological_system": random.choice(biological_systems),
                "engineering_challenge": random.choice(engineering_challenges),
                "application_domain": random.choice(application_domains)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that analyzes biological structures and processes to solve complex engineering problems through biomimicry. This task requires you to integrate knowledge from biology, engineering, and artificial intelligence to create an innovative solution inspired by nature.

Your system should focus on the biological system of {t['biological_system']}, addressing the engineering challenge of {t['engineering_challenge']}, and apply the solution to the domain of {t['application_domain']}. Approach each section systematically, ensuring you draw connections between the biological principles and engineering applications throughout your response.

Your response should include the following sections:

1. Biological System Analysis (250-300 words):
   a) Describe the key features and mechanisms of {t['biological_system']} relevant to {t['engineering_challenge']}.
   b) Explain how these features contribute to the system's effectiveness in nature.
   c) Identify the underlying principles that could be applied to engineering solutions.
   Tip: Focus on the specific aspects of the biological system that relate to the engineering challenge.

2. AI System Architecture (300-350 words):
   a) Outline the main components of your AI system for analyzing and applying biomimetic principles.
   b) Describe the data inputs, processing steps, and outputs of your system.
   c) Explain any novel algorithms or techniques used in your AI model.
   d) Discuss how your system integrates knowledge from biology and engineering.
   Tip: Consider how machine learning techniques can be used to identify and apply relevant biological principles.

3. Biomimetic Solution (250-300 words):
   a) Present your AI-generated solution for {t['engineering_challenge']} inspired by {t['biological_system']}.
   b) Explain how your solution mimics or adapts the biological principles identified earlier.
   c) Describe the potential advantages of your biomimetic solution over traditional approaches.
   Tip: Be specific about how the biological principles are translated into engineering solutions.

4. Application to {t['application_domain']} (200-250 words):
   a) Discuss how your biomimetic solution can be applied to {t['application_domain']}.
   b) Describe specific use cases or products that could benefit from this solution.
   c) Address any challenges in implementing the solution in this domain and propose ways to overcome them.
   Tip: Consider the unique requirements and constraints of the application domain.

5. Evaluation and Validation (150-200 words):
   a) Propose methods to evaluate the effectiveness of your AI-generated biomimetic solution.
   b) Describe experiments or simulations to validate the solution's performance.
   c) Discuss potential limitations of your approach and how they might be addressed.
   Tip: Think about both quantitative and qualitative evaluation methods.

6. Ethical Considerations and Sustainability (150-200 words):
   a) Discuss any ethical implications of using AI-driven biomimicry in engineering.
   b) Address potential environmental impacts of your solution, both positive and negative.
   c) Propose guidelines for responsible development and application of biomimetic technologies.
   Tip: Consider long-term consequences and potential unintended effects.

Ensure your response demonstrates a deep understanding of biology, engineering principles, and artificial intelligence. Use appropriate technical terminology and provide clear explanations where necessary. Be creative and innovative in your approach while maintaining scientific plausibility. Remember to draw connections between different disciplines throughout your response.

Format your response with clear headings for each section. Your total response should be between 1300-1600 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of the biological system {t['biological_system']} and its relevance to {t['engineering_challenge']}.",
            "The AI system architecture is well-designed and clearly explained, integrating knowledge from biology and engineering.",
            f"The biomimetic solution effectively addresses the engineering challenge of {t['engineering_challenge']} using principles derived from {t['biological_system']}.",
            f"The application to {t['application_domain']} is well-thought-out and includes specific use cases.",
            "The evaluation and validation methods proposed are appropriate and comprehensive.",
            "Ethical considerations and sustainability issues are thoughtfully addressed.",
            "The response is creative and innovative while maintaining scientific plausibility.",
            "The response effectively integrates knowledge from biology, engineering, and artificial intelligence throughout."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
