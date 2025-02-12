import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        time_frames = ['past', 'future']
        scenarios = [
            'personal life event',
            'historical occurrence',
            'technological advancement',
            'environmental change',
            'social movement'
        ]
        linguistic_aspects = [
            'tense and aspect usage',
            'temporal adverbials',
            'causal connectives',
            'hypothetical constructions',
            'evidentiality markers'
        ]
        
        tasks = {
            "1": {
                "time_frame": random.choice(time_frames),
                "scenario": random.choice(scenarios),
                "linguistic_aspect": random.choice(linguistic_aspects)
            },
            "2": {
                "time_frame": random.choice(time_frames),
                "scenario": random.choice(scenarios),
                "linguistic_aspect": random.choice(linguistic_aspects)
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Engage in a mental time travel exercise focusing on a {t['time_frame']} {t['scenario']}. Your task is to create a coherent narrative that demonstrates temporal projection and linguistic sophistication. Follow these steps:

1. Scenario Development (200-250 words):
   a) Describe a specific {t['scenario']} set in the {t['time_frame']} (if past, at least 50 years ago; if future, at least 50 years ahead).
   b) Provide rich contextual details that ground the scenario in its temporal setting.
   c) Explain the significance of this scenario and why it was chosen for temporal projection.

2. Narrative Construction (250-300 words):
   a) Create a first-person narrative from the perspective of someone in the present day mentally projecting themselves into the scenario.
   b) Incorporate at least five instances of {t['linguistic_aspect']} in your narrative.
   c) Ensure your narrative maintains causal consistency and logical coherence across the temporal projection.

3. Linguistic Analysis (200-250 words):
   a) Analyze your use of {t['linguistic_aspect']} in the narrative.
   b) Explain how these linguistic features contribute to the sense of temporal projection.
   c) Discuss any challenges you encountered in maintaining linguistic coherence across different time frames.

4. Cognitive Implications (150-200 words):
   a) Discuss how this exercise reflects human cognitive abilities for mental time travel.
   b) Compare the cognitive processes involved in projecting to the past versus the future.
   c) Speculate on how an AI language model might approach this task differently from a human.

5. AI Capability Assessment (200-250 words):
   a) Evaluate the potential capabilities and limitations of current AI language models in performing this kind of temporal projection task.
   b) Propose a specific test or benchmark that could assess an AI's proficiency in mental time travel within a linguistic context.
   c) Discuss the implications of AI performance on this task for our understanding of machine cognition and temporality.

Ensure your response demonstrates a deep understanding of temporal cognition, linguistic features related to time, and the challenges of mental projection across different time frames. Be creative in your scenario and narrative while maintaining logical consistency and linguistic sophistication.

Format your response with clear headings for each section. Your total response should be between 1000-1250 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response includes a well-developed {t['scenario']} set in the {t['time_frame']}",
            f"The narrative incorporates at least five instances of {t['linguistic_aspect']}",
            "The narrative maintains causal consistency and logical coherence across the temporal projection",
            f"The linguistic analysis thoroughly examines the use of {t['linguistic_aspect']} in the narrative",
            "The response discusses cognitive implications of mental time travel and compares past vs. future projection",
            "The AI capability assessment evaluates potential strengths and limitations of language models in temporal projection tasks",
            "The response demonstrates a deep understanding of temporal cognition and linguistic features related to time",
            "The ideas presented are creative while maintaining logical consistency and linguistic sophistication",
            "The response is well-structured with clear headings for each section",
            "The total response falls within the specified word count range of 1000-1250 words"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
