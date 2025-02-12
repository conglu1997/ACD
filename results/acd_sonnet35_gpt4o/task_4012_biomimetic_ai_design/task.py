import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        biological_inspirations = [
            "photosynthesis",
            "spider silk",
            "termite mounds",
            "lotus leaf",
            "whale fin"
        ]
        sustainability_challenges = [
            "energy efficiency",
            "water purification",
            "sustainable agriculture",
            "waste management",
            "climate change mitigation"
        ]
        ai_techniques = [
            "neural networks",
            "evolutionary algorithms",
            "reinforcement learning",
            "swarm intelligence",
            "fuzzy logic"
        ]
        
        tasks = [
            {
                "biological_inspiration": random.choice(biological_inspirations),
                "sustainability_challenge": random.choice(sustainability_challenges),
                "ai_technique": random.choice(ai_techniques)
            } for _ in range(2)
        ]
        
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that emulates the biological process or structure of {t['biological_inspiration']} to address the sustainability challenge of {t['sustainability_challenge']}, utilizing the AI technique of {t['ai_technique']}. Your response should include:

1. Biomimetic Analysis (250-300 words):
   a) Describe the key features and mechanisms of {t['biological_inspiration']}.
   b) Explain how these features can be applied to address {t['sustainability_challenge']}.
   c) Discuss any existing biomimetic technologies inspired by this biological system.

2. AI System Design (300-350 words):
   a) Outline the architecture of your AI system, explaining how it incorporates {t['ai_technique']}.
   b) Describe how your system emulates the key features of {t['biological_inspiration']}.
   c) Explain how the AI processes data and makes decisions to address {t['sustainability_challenge']}.
   d) Include a high-level diagram or pseudocode representing your system's architecture.

3. Implementation and Scalability (200-250 words):
   a) Discuss the technical requirements for implementing your AI system.
   b) Explain how your system could be scaled up for real-world application.
   c) Address potential challenges in implementation and propose solutions.

4. Performance Evaluation (200-250 words):
   a) Propose metrics to evaluate your system's effectiveness in addressing {t['sustainability_challenge']}.
   b) Describe a hypothetical experiment to test your system's performance.
   c) Discuss how you would compare your system's efficiency to existing solutions.

5. Environmental Impact Assessment (150-200 words):
   a) Analyze the potential positive and negative environmental impacts of your AI system.
   b) Discuss how your system contributes to sustainability beyond its primary function.
   c) Propose methods to mitigate any negative environmental effects.

6. Ethical Implications (150-200 words):
   a) Identify and discuss at least three ethical concerns related to your AI system.
   b) Analyze potential social and economic impacts of widespread adoption.
   c) Propose guidelines for responsible development and use of your technology.

7. Future Developments (100-150 words):
   a) Suggest two potential improvements or extensions to your AI system.
   b) Discuss how advancements in AI or biomimetics might enhance your design.
   c) Propose a related research direction that could further the field of biomimetic AI.

Ensure your response demonstrates a deep understanding of the biological system, AI techniques, and sustainability challenges. Be innovative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section. Your total response should be between 1350-1700 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must design an AI system that emulates {t['biological_inspiration']} to address {t['sustainability_challenge']} using {t['ai_technique']}",
            "The biomimetic analysis should demonstrate a deep understanding of the biological system",
            "The AI system design should be innovative, plausible, and clearly explained",
            "Implementation challenges and scalability issues must be thoughtfully addressed",
            "The performance evaluation plan should be well-designed and relevant",
            "Environmental impact assessment should consider both positive and negative effects",
            "Ethical implications must be thoroughly explored from multiple perspectives",
            "Future developments should be relevant and demonstrate foresight in the field",
            "The response should follow the specified format with clear headings for each section",
            "The response should be within the specified word count range (1350-1700 words)"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
