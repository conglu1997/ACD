import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        societal_trends = [
            "Environmental consciousness",
            "Political polarization",
            "Technological adoption",
            "Economic inequality",
            "Cultural globalization",
            "Health awareness",
            "Educational paradigms",
            "Urban development"
        ]
        evolutionary_principles = [
            "Natural selection",
            "Genetic drift",
            "Mutation",
            "Gene flow",
            "Epigenetic inheritance",
            "Adaptive radiation",
            "Convergent evolution",
            "Evolutionary arms race"
        ]
        task = {
            "societal_trend": random.choice(societal_trends),
            "evolutionary_principle": random.choice(evolutionary_principles)
        }
        return {"1": task, "2": task}

    @staticmethod
    def get_instructions(t: dict) -> str:
        societal_trend = t["societal_trend"]
        evolutionary_principle = t["evolutionary_principle"]
        
        return f"Design an AI system that integrates complex systems theory and evolutionary biology principles to model, predict, and potentially influence societal trends and behaviors. Your system should focus on the societal trend of {societal_trend} and incorporate the evolutionary principle of {evolutionary_principle}. Your response should be original and not based on existing models or systems. Include the following sections:\n\n" \
               f"1. System Architecture (300-350 words):\n" \
               f"   a) Describe the key components of your AI system for modeling societal trends.\n" \
               f"   b) Explain how your system integrates complex systems theory and evolutionary biology principles.\n" \
               f"   c) Detail the specific AI techniques and algorithms used in your system.\n" \
               f"   d) Provide a high-level diagram or flowchart of your system architecture (describe it textually).\n\n" \
               f"2. Data and Modeling (250-300 words):\n" \
               f"   a) Specify the types of data your system would use and potential sources.\n" \
               f"   b) Explain how your system would process and analyze this data.\n" \
               f"   c) Describe how your system incorporates the specified evolutionary principle in its modeling approach.\n" \
               f"   d) Discuss how your system handles uncertainties and complexities in societal trend prediction.\n\n" \
               f"3. Predictive Capabilities (250-300 words):\n" \
               f"   a) Explain how your AI system predicts future trends related to {societal_trend}.\n" \
               f"   b) Describe the time scales at which your system can make predictions and why.\n" \
               f"   c) Discuss how your system accounts for potential 'butterfly effects' or cascading changes in society.\n" \
               f"   d) Provide a hypothetical example of a prediction your system might make.\n\n" \
               f"4. Influence Mechanisms (200-250 words):\n" \
               f"   a) Propose mechanisms by which your system could potentially influence {societal_trend}.\n" \
               f"   b) Explain how these mechanisms relate to the evolutionary principle of {evolutionary_principle}.\n" \
               f"   c) Discuss the ethical implications of using AI to influence societal trends.\n\n" \
               f"5. Evaluation and Validation (200-250 words):\n" \
               f"   a) Propose methods to evaluate the accuracy and reliability of your system's predictions.\n" \
               f"   b) Describe how you would validate the effectiveness of the influence mechanisms.\n" \
               f"   c) Discuss the challenges in evaluating such a complex system and how you would address them.\n\n" \
               f"6. Ethical Considerations and Safeguards (200-250 words):\n" \
               f"   a) Identify potential ethical issues arising from the use of AI to predict and influence societal trends.\n" \
               f"   b) Discuss how your system addresses issues of fairness, transparency, and accountability.\n" \
               f"   c) Propose safeguards to prevent misuse or unintended consequences of your system.\n\n" \
               f"7. Future Developments (150-200 words):\n" \
               f"   a) Suggest two potential improvements or extensions to your system.\n" \
               f"   b) Propose a research question that could further the development of AI systems for societal modeling and influence.\n\n" \
               f"Ensure your response demonstrates a deep understanding of complex systems theory, evolutionary biology, and artificial intelligence. Use appropriate technical terminology and provide clear explanations where necessary. Be innovative in your approach while maintaining scientific and practical plausibility.\n\n" \
               f"Format your response with clear headings for each section. Your total response should be between 1550-1900 words. Include a total word count at the end of your response."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of complex systems theory, evolutionary biology, and artificial intelligence, with appropriate use of technical terminology.",
            "The AI system design integrates the specified societal trend and evolutionary principle coherently and innovatively.",
            "The system architecture, data modeling, and predictive capabilities are well-explained and scientifically plausible.",
            "The influence mechanisms and their ethical implications are thoughtfully discussed.",
            "The evaluation methods, ethical considerations, and future developments are thoroughly addressed.",
            "The response is well-structured, follows the given format with clear headings, and adheres to the word count guidelines.",
            "The proposed system design is original and not based on existing models or systems."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
