import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        language_features = [
            {
                "feature": "Temporal concepts",
                "description": "How time is represented and expressed in the language"
            },
            {
                "feature": "Spatial relationships",
                "description": "How space and relative positions are conceptualized"
            },
            {
                "feature": "Color categorization",
                "description": "How colors are divided and named in the language"
            },
            {
                "feature": "Evidentiality",
                "description": "How the source of information is grammatically marked"
            }
        ]
        
        cognitive_tasks = [
            "Problem-solving in a maze environment",
            "Pattern recognition in abstract shapes",
            "Categorization of natural objects",
            "Sequence prediction and generation"
        ]
        
        return {
            "1": {
                "language_feature": random.choice(language_features),
                "cognitive_task": random.choice(cognitive_tasks)
            },
            "2": {
                "language_feature": random.choice(language_features),
                "cognitive_task": random.choice(cognitive_tasks)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a simulated AI agent with a unique constructed language that emphasizes the language feature of {t['language_feature']['feature']}, which is described as: {t['language_feature']['description']}. Then, analyze how this language structure influences the agent's ability to perform the cognitive task of {t['cognitive_task']}. Your response should include:

1. Language Design (250-300 words):
   a) Describe the key features of your constructed language, focusing on how it emphasizes {t['language_feature']['feature']}.
   b) Provide at least 5 example words or phrases in your language, with their meanings and explanations of how they embody the emphasized feature.
   c) Explain how this language structure might influence the agent's perception and cognition.

2. AI Agent Simulation (200-250 words):
   a) Describe how your AI agent would be designed to use this language as its primary mode of 'thinking' and processing information.
   b) Explain potential advantages or limitations this language structure might create for the agent's cognitive processes.

3. Cognitive Task Analysis (250-300 words):
   a) Analyze in detail how the agent's language structure would influence its approach to the cognitive task of {t['cognitive_task']}.
   b) Provide specific examples of how the agent might perform differently compared to agents with other language structures.
   c) Discuss any potential biases or unique problem-solving strategies that might emerge due to the language structure.

4. Comparative Analysis (200-250 words):
   a) Compare and contrast how your AI agent's performance might differ from an agent using a language emphasizing a different feature.
   b) Discuss the implications of these differences for our understanding of linguistic relativity and artificial intelligence.

5. Experimental Design (100-150 words):
   Propose an experiment to test the influence of your language structure on AI cognitive performance. Include a hypothesis, methodology, and expected results.

Ensure your response demonstrates a deep understanding of linguistics, cognitive science, and artificial intelligence. Be creative in your language design and analysis while maintaining scientific plausibility and logical consistency."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The constructed language design clearly emphasizes the feature of {t['language_feature']['feature']}.",
            "The analysis of the AI agent's cognitive processes is thorough and logically connected to the language structure.",
            f"The cognitive task analysis provides insightful observations about how the language structure influences the agent's approach to {t['cognitive_task']}.",
            "The comparative analysis offers meaningful insights into linguistic relativity and its implications for AI.",
            "The proposed experiment is well-designed and relevant to testing the influence of language structure on AI cognitive performance.",
            "The overall response shows a high level of interdisciplinary knowledge integration, creativity, and analytical reasoning."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
