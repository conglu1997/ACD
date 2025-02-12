import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        resources = [
            {
                "name": "Dreams",
                "description": "In this world, dreams can be harvested and used as a source of energy and creative inspiration."
            },
            {
                "name": "Emotions",
                "description": "Emotions can be quantified, stored, and traded as a valuable commodity."
            },
            {
                "name": "Time",
                "description": "Personal time can be transferred between individuals and is the primary medium of exchange."
            },
            {
                "name": "Memories",
                "description": "Memories can be extracted, stored, and used as a form of currency and knowledge transfer."
            }
        ]
        return {str(i+1): resource for i, resource in enumerate(random.sample(resources, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design and analyze a fictional economic system based on the unconventional resource: {t['name']}. {t['description']}

Your task is to:

1. Describe the basic mechanics of how this resource is harvested, quantified, and traded (3-4 sentences).

2. Explain three key economic principles or concepts that would govern this economy (1-2 sentences each).

3. Discuss two potential societal impacts of this economic system (2-3 sentences each):
   a) One positive impact
   b) One negative impact or potential abuse of the system

4. Propose one innovative industry or job that would arise in this economy (2-3 sentences).

5. Draw a specific parallel between an aspect of this fictional economy and a current real-world economic issue or trend, explaining how insights from your fictional system might apply to the real-world situation (3-4 sentences).

Ensure your response is creative yet grounded in economic theory. Your analysis should demonstrate an understanding of how economic systems function and impact society, while also showing imaginative thinking about how unconventional resources could shape an economy.

Format your response using clear headings for each section. Your total response should be between 400-500 words.

Remember to use the following structure for your response:

1. Resource Mechanics
[Your answer here]

2. Key Economic Principles
[Your answer here]

3. Societal Impacts
a) Positive Impact:
[Your answer here]
b) Negative Impact:
[Your answer here]

4. Innovative Industry/Job
[Your answer here]

5. Real-World Parallel
[Your answer here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response includes a coherent description of an economic system based on {t['name']}",
            "The explanation of economic principles is accurate and relevant to the fictional economy",
            "The societal impacts discussed are logical consequences of the proposed economic system",
            "The proposed industry or job is creative and consistent with the economy's mechanics",
            "The parallel drawn to a real-world economic issue is specific, insightful, and well-reasoned",
            "The overall response demonstrates both economic understanding and creative thinking",
            "The response follows the specified format and is within the 400-500 word limit"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
