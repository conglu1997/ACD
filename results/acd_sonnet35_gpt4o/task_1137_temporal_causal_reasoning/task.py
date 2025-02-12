import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "narrative": "In a world where time flows backwards, a detective investigates a murder that hasn't happened yet.",
                "temporal_twist": "Reverse causality",
                "causal_challenge": "Preventing a future event from causing a past consequence"
            },
            {
                "narrative": "A scientist discovers a particle that exists simultaneously at all points in time, affecting historical and future events.",
                "temporal_twist": "Non-linear time",
                "causal_challenge": "Resolving paradoxes created by simultaneous cause and effect across time"
            }
        ]
        return {
            "1": random.choice(scenarios),
            "2": random.choice(scenarios)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Analyze and manipulate the complex temporal and causal relationships in the following narrative, then apply your understanding to solve abstract reasoning problems and generate a novel scenario.

Narrative: {t['narrative']}
Temporal Twist: {t['temporal_twist']}
Causal Challenge: {t['causal_challenge']}

Your task has five parts:

1. Temporal-Causal Analysis (200-250 words):
   a) Identify and explain the key temporal and causal relationships in the narrative.
   b) Discuss how the temporal twist affects these relationships.
   c) Analyze the logical implications of the causal challenge presented.

2. Paradox Resolution (150-200 words):
   a) Identify any potential paradoxes or logical inconsistencies in the narrative.
   b) Propose a logically consistent resolution to these paradoxes.
   c) Explain how your resolution maintains the integrity of the narrative's temporal and causal structure.

3. Abstract Reasoning Problem (200-250 words):
   Design and solve an abstract reasoning problem based on the temporal and causal principles in the narrative. Your problem should:
   a) Incorporate the temporal twist and causal challenge.
   b) Require multi-step logical deductions.
   c) Have a unique, definitively correct solution.
   Provide both the problem and its solution with a step-by-step explanation.

4. Novel Scenario Generation (200-250 words):
   Create a new scenario that extends or modifies the original narrative. Your scenario should:
   a) Introduce a new temporal or causal element that interacts with the existing ones.
   b) Explore the logical consequences of this new element.
   c) Present a thought-provoking dilemma or question arising from the modified temporal-causal structure.

5. Cognitive Implications (150-200 words):
   a) Discuss how the temporal and causal manipulations in this task relate to human cognition and perception of time.
   b) Analyze potential challenges these concepts might pose for artificial intelligence systems.
   c) Propose an experiment to test whether humans or AI models are better at handling these types of temporal-causal reasoning tasks.

Ensure your response demonstrates a deep understanding of temporal logic, causal reasoning, and abstract problem-solving. Be creative and logically rigorous in your analysis and scenario generation."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a clear understanding of complex temporal and causal relationships.",
            "The paradox resolution is logically consistent and well-explained.",
            "The abstract reasoning problem is well-designed, incorporates the given elements, and has a unique, correct solution.",
            "The novel scenario is creative, logically sound, and extends the original narrative in an interesting way.",
            "The discussion of cognitive implications shows insight into both human cognition and AI capabilities.",
            "The overall response exhibits high-level abstract reasoning and creative problem-solving skills."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
