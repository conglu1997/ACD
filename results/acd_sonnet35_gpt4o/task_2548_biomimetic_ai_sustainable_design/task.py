import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        urban_challenges = [
            "Water management in drought-prone areas",
            "Sustainable transportation in high-density cities",
            "Energy-efficient building design for extreme climates",
            "Urban food production in limited spaces",
            "Waste reduction and circular economy implementation",
            "Air quality improvement in industrial zones",
            "Flood resilience in coastal cities",
            "Urban heat island mitigation"
        ]
        biological_inspirations = [
            "Plant transpiration systems",
            "Ant colony optimization",
            "Termite mound thermoregulation",
            "Mycelium networks",
            "Lotus leaf self-cleaning properties",
            "Whale fin water flow efficiency",
            "Spider silk strength and flexibility",
            "Butterfly wing light manipulation"
        ]
        constraints = [
            "Minimize resource consumption",
            "Enhance biodiversity",
            "Improve social equity",
            "Reduce carbon footprint",
            "Maximize energy efficiency",
            "Ensure scalability across different urban contexts",
            "Promote community engagement and participation",
            "Adapt to future climate change scenarios"
        ]
        
        return {
            "1": {
                "challenge": random.choice(urban_challenges),
                "inspiration": random.choice(biological_inspirations),
                "constraint": random.choice(constraints)
            },
            "2": {
                "challenge": random.choice(urban_challenges),
                "inspiration": random.choice(biological_inspirations),
                "constraint": random.choice(constraints)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that uses principles of biomimicry to generate sustainable solutions for urban planning challenges. Your system should address the urban challenge of {t['challenge']} using inspiration from {t['inspiration']}, while considering the constraint to {t['constraint']}. Your response should include the following sections:

1. AI System Architecture (300-350 words):
   a) Describe the overall structure and components of your AI system.
   b) Explain how your system incorporates principles of biomimicry in its design and function.
   c) Detail how the system processes and analyzes urban planning data.
   d) Discuss how the biological inspiration is integrated into the AI's problem-solving approach.
   e) Provide a text-based description of a visual representation (e.g., flowchart or block diagram) of your AI system architecture.

2. Biomimetic Solution Generation (250-300 words):
   a) Explain the process by which your AI system generates solutions inspired by {t['inspiration']}.
   b) Describe how the system adapts biological principles to address {t['challenge']}.
   c) Discuss how the constraint to {t['constraint']} is factored into the solution generation process.
   d) Provide an example of a potential solution your system might generate.

3. Data Integration and Learning (200-250 words):
   a) Describe the types of data your system would use to inform its solutions.
   b) Explain how the AI learns from both successful and unsuccessful biomimetic adaptations.
   c) Discuss how your system might integrate feedback from urban planners and residents.

4. Evaluation Metrics (200-250 words):
   a) Propose specific metrics to assess the effectiveness of your AI-generated solutions.
   b) Explain how these metrics relate to both urban sustainability and biomimetic principles.
   c) Describe how you would validate the AI's solutions against traditional urban planning approaches.

5. Ethical Considerations and Societal Impact (200-250 words):
   a) Discuss potential ethical implications of using AI and biomimicry in urban planning.
   b) Address any potential biases or limitations in your system's approach.
   c) Analyze the possible long-term impacts of implementing your AI system on urban development and sustainability.
   d) Propose guidelines for responsible development and use of biomimetic AI in urban planning.

6. Limitations and Future Improvements (150-200 words):
   a) Identify and discuss potential limitations or challenges of your proposed AI system.
   b) Suggest areas for future research or improvements to address these limitations.
   c) Discuss how your system might adapt to evolving urban challenges and technological advancements.

Ensure your response demonstrates a deep understanding of artificial intelligence, biology, urban planning, and sustainability principles. Use appropriate technical terminology and provide clear explanations where necessary. Be creative and innovative in your approach while maintaining scientific and practical plausibility.

Format your response with clear headings for each section. Your total response should be between 1300-1600 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The AI system architecture effectively incorporates principles of biomimicry and addresses the urban challenge of {t['challenge']}.",
            f"The solution generation process clearly demonstrates how {t['inspiration']} is used to inspire sustainable urban solutions.",
            f"The proposed system adequately considers the constraint to {t['constraint']} in its design and solution generation.",
            "The response shows a deep understanding and integration of AI, biology, urban planning, and sustainability concepts.",
            "The evaluation metrics and ethical considerations are well-thought-out and relevant to the proposed system.",
            "The response is creative and innovative while maintaining scientific and practical plausibility.",
            "The limitations and future improvements section demonstrates critical thinking and awareness of the system's constraints.",
            "The response adheres to the specified word count and formatting requirements."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
