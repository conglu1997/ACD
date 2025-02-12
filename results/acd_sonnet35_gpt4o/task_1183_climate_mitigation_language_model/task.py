import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "topic": "Carbon capture and storage technologies",
                "paper_title": "Recent advances in direct air capture for carbon dioxide removal",
                "policy_question": "How can government incentives accelerate the adoption of direct air capture technologies?"
            },
            {
                "topic": "Renewable energy integration",
                "paper_title": "Grid stability challenges in high renewable energy penetration scenarios",
                "policy_question": "What regulatory frameworks are needed to support a rapid transition to 100% renewable energy while maintaining grid reliability?"
            },
            {
                "topic": "Sustainable agriculture and food systems",
                "paper_title": "Innovative approaches to reduce greenhouse gas emissions in agriculture",
                "policy_question": "How can policies promote sustainable farming practices while ensuring food security and farmer livelihoods?"
            }
        ]
        selected_tasks = random.sample(tasks, 2)
        return {"1": selected_tasks[0], "2": selected_tasks[1]}

    @staticmethod
    def get_instructions(t: dict) -> str:
        word_counts = {
            "paper_analysis": random.randint(300, 350),
            "technical_report": random.randint(400, 450),
            "policy_response": random.randint(250, 300),
            "communication_strategy": random.randint(150, 200)
        }
        
        return f"""As an AI language model specialized in climate change mitigation strategies, your task is to analyze a scientific paper, generate a report, and answer a policy-related question. Focus on the topic of {t['topic']}. Your response should include the following sections:

1. Paper Analysis ({word_counts['paper_analysis']} words):
   a) Summarize the key findings and methodologies of the paper titled "{t['paper_title']}".
   b) Identify the main climate mitigation strategies discussed in the paper.
   c) Evaluate the potential impact of these strategies on global carbon emissions.

2. Technical Report Generation ({word_counts['technical_report']} words):
   Based on your analysis and additional knowledge:
   a) Describe the current state of technology or policy related to {t['topic']}.
   b) Discuss challenges and opportunities for implementation or scaling.
   c) Propose at least two innovative solutions or improvements in this area.
   d) Include relevant statistics or data to support your points.

3. Policy Question Response ({word_counts['policy_response']} words):
   Address the following question: "{t['policy_question']}"
   a) Provide a well-reasoned answer based on current scientific understanding and policy landscapes.
   b) Consider potential economic, social, and environmental impacts of your proposed approach.
   c) Suggest at least one specific policy measure or initiative to support your recommendation.

4. Communication Strategy ({word_counts['communication_strategy']} words):
   a) Outline an approach to effectively communicate the key points from your report to a non-expert audience.
   b) Suggest ways to address potential misconceptions or controversies related to {t['topic']}.

Ensure your response demonstrates a deep understanding of climate science, policy mechanisms, and effective science communication. Use appropriate technical terminology and provide clear explanations where necessary. Be innovative in your approach while maintaining scientific accuracy and policy relevance.

Format your response with clear headings for each section and adhere to the specified word counts."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response accurately summarizes and analyzes the given scientific paper.",
            "The technical report demonstrates a deep understanding of the topic and proposes innovative solutions.",
            "The policy question is addressed comprehensively with well-reasoned arguments and specific recommendations.",
            "The communication strategy effectively translates complex scientific concepts for a non-expert audience.",
            "The overall response shows a strong grasp of climate science, policy mechanisms, and interdisciplinary problem-solving.",
            "The response adheres to the specified word counts and formatting requirements."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
