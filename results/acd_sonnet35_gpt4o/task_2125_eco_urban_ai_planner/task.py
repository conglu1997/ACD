import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        urban_challenges = [
            "traffic congestion",
            "air pollution",
            "urban heat islands",
            "biodiversity loss",
            "water management",
            "energy efficiency"
        ]
        ecosystem_services = [
            "carbon sequestration",
            "air purification",
            "water filtration",
            "temperature regulation",
            "pollination",
            "noise reduction"
        ]
        ai_techniques = [
            "reinforcement learning",
            "multi-agent systems",
            "computer vision",
            "natural language processing",
            "evolutionary algorithms",
            "knowledge graphs"
        ]
        tasks = [
            {
                "urban_challenge": random.choice(urban_challenges),
                "ecosystem_service": random.choice(ecosystem_services),
                "ai_technique": random.choice(ai_techniques)
            },
            {
                "urban_challenge": random.choice(urban_challenges),
                "ecosystem_service": random.choice(ecosystem_services),
                "ai_technique": random.choice(ai_techniques)
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that integrates ecological principles and urban planning to optimize sustainable city development, focusing on the following elements:

1. Urban Challenge: {t['urban_challenge']}
2. Ecosystem Service: {t['ecosystem_service']}
3. AI Technique: {t['ai_technique']}

Your task consists of the following steps:

1. System Architecture (250-300 words):
   a) Describe the key components of your AI system and how they interact.
   b) Explain how your system incorporates ecological principles and urban planning concepts.
   c) Discuss how the specified AI technique is utilized in your system's design.
   d) Include a simple diagram or flowchart of your system's architecture.

2. Data Integration and Analysis (200-250 words):
   a) Identify the types of data your system would need to address the given urban challenge.
   b) Explain how your system would collect, process, and analyze this data.
   c) Describe how your system would model and quantify the specified ecosystem service.

3. Optimization Approach (200-250 words):
   a) Detail your system's approach to optimizing urban development while maximizing the ecosystem service.
   b) Explain how your system balances competing priorities and constraints.
   c) Discuss any novel algorithms or methods your system employs.

4. Practical Application (200-250 words):
   a) Provide a specific example of how your system would address the given urban challenge.
   b) Describe the expected outcomes and benefits of implementing your system.
   c) Discuss potential challenges in deploying your system in real-world urban environments.

5. Ethical Considerations and Stakeholder Engagement (150-200 words):
   a) Identify potential ethical issues arising from the use of AI in urban planning and ecosystem management.
   b) Propose guidelines for responsible development and use of your system.
   c) Describe how your system would incorporate input from diverse stakeholders.

6. Scalability and Adaptability (150-200 words):
   a) Explain how your system could be scaled to different city sizes and types.
   b) Discuss how your system could adapt to changing environmental conditions or urban dynamics.
   c) Propose potential extensions or modifications to address other urban challenges or ecosystem services.

Ensure your response demonstrates a deep understanding of ecology, artificial intelligence, and urban planning. Use appropriate terminology from each field and provide clear explanations for complex concepts. Be creative in your approach while maintaining scientific and practical plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1150-1450 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response effectively addresses the urban challenge of {t['urban_challenge']} using the AI technique of {t['ai_technique']} while optimizing for the ecosystem service of {t['ecosystem_service']}.",
            "The system architecture is well-designed and clearly explained, with a coherent integration of ecological principles and urban planning concepts.",
            "The data integration and analysis approach is comprehensive and appropriate for the given challenge and ecosystem service.",
            "The optimization approach is innovative and effectively balances urban development with ecosystem service maximization.",
            "The practical application example is relevant and demonstrates the potential impact of the system.",
            "Ethical considerations are thoughtfully addressed, with appropriate guidelines for responsible use.",
            "The system's scalability and adaptability are well-explained and plausible.",
            "The response demonstrates a deep understanding of ecology, artificial intelligence, and urban planning throughout.",
            "The response is creative while maintaining scientific and practical plausibility.",
            "The response follows the specified format and is within the 1150-1450 word range."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
