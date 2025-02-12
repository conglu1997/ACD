import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "cognitive_principle": "Chunking",
                "problem_domain": "Memorizing long sequences of numbers",
                "application_scenario": "Remembering historical dates"
            },
            {
                "cognitive_principle": "Elaborative rehearsal",
                "problem_domain": "Learning complex scientific concepts",
                "application_scenario": "Understanding quantum mechanics principles"
            },
            {
                "cognitive_principle": "Method of loci",
                "problem_domain": "Memorizing lists of items",
                "application_scenario": "Recalling items on a shopping list"
            },
            {
                "cognitive_principle": "Dual coding theory",
                "problem_domain": "Learning a new language",
                "application_scenario": "Mastering idiomatic expressions"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design a mnemonic device based on the cognitive principle of {t['cognitive_principle']} to address the problem of {t['problem_domain']}. Then, apply your mnemonic device to the scenario of {t['application_scenario']}. Your response should include:\n\n" \
               f"1. Mnemonic Device Design (200-250 words):\n" \
               f"   a) Explain the chosen cognitive principle and its relevance to memory and learning.\n" \
               f"   b) Describe your mnemonic device in detail, including its structure and how it incorporates the cognitive principle.\n" \
               f"   c) Explain how your device addresses the given problem domain.\n\n" \
               f"2. Application to Scenario (150-200 words):\n" \
               f"   a) Apply your mnemonic device to the given application scenario.\n" \
               f"   b) Provide a specific example of how it would be used in this context.\n" \
               f"   c) Discuss any adaptations needed to fit the specific scenario.\n\n" \
               f"3. Effectiveness Analysis (100-150 words):\n" \
               f"   a) Analyze the potential effectiveness of your mnemonic device.\n" \
               f"   b) Discuss any limitations or challenges in using this device.\n" \
               f"   c) Suggest potential improvements or variations.\n\n" \
               f"4. Cognitive Science Connections (100-150 words):\n" \
               f"   a) Explain how your mnemonic device relates to other cognitive science concepts or theories.\n" \
               f"   b) Discuss how understanding these connections could lead to improved learning strategies.\n\n" \
               f"Ensure your response demonstrates a deep understanding of cognitive science principles, creativity in mnemonic design, and the ability to apply abstract concepts to concrete scenarios. Use appropriate terminology and provide clear explanations.\n\n" \
               f"Format your answer with clear headings for each section. Your total response should be between 550-750 words."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The mnemonic device effectively incorporates the cognitive principle of {t['cognitive_principle']}.",
            f"The mnemonic device is well-designed to address the problem of {t['problem_domain']}.",
            f"The application to the scenario of {t['application_scenario']} is clear and appropriate.",
            "The response includes all required sections (1-4) as specified, adhering to the given word limits.",
            "The mnemonic device design is creative and demonstrates a deep understanding of cognitive science principles.",
            "The effectiveness analysis is thorough and considers both strengths and limitations of the device.",
            "The cognitive science connections are well-explained and relevant.",
            "The response demonstrates the ability to apply abstract cognitive concepts to concrete scenarios.",
            "Appropriate cognitive science terminology is used throughout the response."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
