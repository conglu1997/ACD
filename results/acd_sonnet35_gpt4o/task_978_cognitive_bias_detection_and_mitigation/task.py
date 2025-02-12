import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cognitive_biases = [
            {
                "name": "Confirmation Bias",
                "description": "The tendency to search for, interpret, favor, and recall information in a way that confirms or supports one's prior beliefs or values."
            },
            {
                "name": "Anchoring Bias",
                "description": "The tendency to rely too heavily on the first piece of information offered (the 'anchor') when making decisions."
            },
            {
                "name": "Availability Heuristic",
                "description": "The tendency to overestimate the likelihood of events with greater 'availability' in memory, which can be influenced by how unusual or emotionally charged they may be."
            },
            {
                "name": "Dunning-Kruger Effect",
                "description": "A cognitive bias in which people with limited knowledge or competence in a given intellectual or social domain greatly overestimate their own knowledge or competence in that domain."
            }
        ]
        
        scenarios = [
            "A team of scientists is reviewing research proposals for funding.",
            "A jury is deliberating in a high-profile criminal case.",
            "A group of investors is deciding whether to fund a new startup.",
            "A government task force is developing policies to address climate change."
        ]
        
        tasks = {}
        for i in range(2):
            tasks[str(i+1)] = {
                "cognitive_bias": random.choice(cognitive_biases),
                "scenario": random.choice(scenarios)
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Analyze the following scenario for the presence of {t['cognitive_bias']['name']} and propose an AI-assisted mitigation strategy:

Scenario: {t['scenario']}
Cognitive Bias: {t['cognitive_bias']['name']} - {t['cognitive_bias']['description']}

Your task:

1. Explanation (100-150 words):
   a) Describe how the given cognitive bias might manifest in the scenario.
   b) Explain the potential negative impacts of this bias on decision-making in this context.

2. Detection Method (100-150 words):
   a) Propose a method for detecting this cognitive bias using natural language processing and machine learning techniques.
   b) Explain how your method would work and what indicators it would look for in the language or behavior of the participants.

3. AI-Assisted Mitigation Strategy (150-200 words):
   a) Design an AI-assisted tool or process to help mitigate the effects of this cognitive bias in the given scenario.
   b) Explain how your proposed solution works and how it addresses the specific challenges posed by this bias.
   c) Discuss any potential limitations or ethical considerations of your AI-assisted approach.

4. Comparative Analysis (100-150 words):
   a) Compare the effectiveness of your AI-assisted approach to traditional (non-AI) methods of bias mitigation.
   b) Discuss the potential advantages and disadvantages of relying on AI for cognitive bias mitigation.

Ensure your response demonstrates a deep understanding of cognitive psychology, natural language processing, and AI ethics. Be innovative in your approach while maintaining scientific plausibility and addressing real-world challenges.

Format your response with clear headings for each section."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response accurately explains how the cognitive bias might manifest in the given scenario",
            "The proposed detection method uses relevant NLP and ML techniques",
            "The AI-assisted mitigation strategy is innovative and addresses the specific challenges of the bias",
            "The comparative analysis thoughtfully discusses advantages and disadvantages of AI-assisted bias mitigation",
            "The response demonstrates a deep understanding of cognitive psychology, NLP, and AI ethics"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
