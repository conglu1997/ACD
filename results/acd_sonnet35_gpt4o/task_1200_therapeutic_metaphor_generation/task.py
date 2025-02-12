import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "psychological_state": "Anxiety about the future",
                "therapeutic_goal": "Promoting a sense of control and adaptability",
                "cultural_context": "Western individualistic society"
            },
            {
                "psychological_state": "Grief over loss",
                "therapeutic_goal": "Facilitating acceptance and personal growth",
                "cultural_context": "Eastern collectivist society"
            },
            {
                "psychological_state": "Low self-esteem",
                "therapeutic_goal": "Enhancing self-worth and confidence",
                "cultural_context": "Multicultural urban environment"
            }
        ]
        return {
            "1": random.choice(scenarios),
            "2": random.choice(scenarios)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that analyzes psychological states and generates therapeutic metaphors, then use the system to create metaphors for a specific scenario. A therapeutic metaphor is a figurative comparison that helps clients understand their experiences in a new way, facilitating insight and positive change.

Your task has the following components:

1. System Architecture (250-300 words):
   a) Describe the components of your AI system for generating therapeutic metaphors.
   b) Explain how the system analyzes psychological states and therapeutic goals.
   c) Detail the process of metaphor generation, including any databases or knowledge bases used.
   d) Discuss how the system incorporates cultural context into its metaphor generation.

2. Linguistic Analysis (200-250 words):
   a) Explain how your system analyzes the linguistic structure of effective therapeutic metaphors.
   b) Describe any natural language processing techniques used in your system.
   c) Discuss how the system ensures the generated metaphors are linguistically and culturally appropriate.

3. Psychological Integration (200-250 words):
   a) Describe how your system integrates psychological theories or therapeutic approaches.
   b) Explain how the system matches metaphors to specific psychological states and therapeutic goals.
   c) Discuss any potential limitations or ethical considerations in using AI-generated metaphors in therapy.

4. Metaphor Generation (200-250 words):
   Using your designed system, generate a therapeutic metaphor for the following scenario:
   - Psychological state: {t['psychological_state']}
   - Therapeutic goal: {t['therapeutic_goal']}
   - Cultural context: {t['cultural_context']}

   Provide the generated metaphor (100-150 words) and explain how it addresses the psychological state, supports the therapeutic goal, and fits the cultural context. Remember to be culturally sensitive and appropriate in your metaphor generation.

5. Evaluation and Refinement (150-200 words):
   a) Propose a method for evaluating the effectiveness of your system's generated metaphors.
   b) Describe how you would refine and improve your system based on feedback and evaluation results.
   c) Discuss potential future developments or extensions of your system.

Ensure your response demonstrates a deep understanding of psycholinguistics, therapeutic practices, and AI technologies. Be innovative in your approach while maintaining scientific and practical plausibility. Use appropriate technical terminology and provide clear explanations where necessary.

Format your response with clear headings for each section. Your total response should be between 1000-1250 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a comprehensive understanding of psycholinguistics, therapeutic practices, and AI technologies.",
            "The proposed AI system architecture is well-explained and addresses all required components, including psychological state analysis, metaphor generation, and cultural context integration.",
            "The linguistic analysis section provides a clear explanation of how the system analyzes and generates metaphors, including relevant NLP techniques.",
            "The psychological integration section effectively describes how the system incorporates psychological theories and addresses ethical considerations.",
            "The generated metaphor is creative, appropriate for the given scenario, and clearly explained in terms of its relevance to the psychological state, therapeutic goal, and cultural context.",
            "The generated metaphor is within the specified word count (100-150 words) and demonstrates cultural sensitivity.",
            "The evaluation and refinement section proposes a plausible method for assessing the system's effectiveness and suggests relevant improvements.",
            "The response is well-structured, adheres to the word limits, and uses appropriate technical terminology throughout."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
