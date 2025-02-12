import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        brain_regions = ['prefrontal cortex', 'hippocampus', 'amygdala', 'cerebellum']
        oscillation_types = ['alpha', 'beta', 'theta', 'gamma', 'delta']
        therapeutic_goals = ['stress reduction', 'memory enhancement', 'emotion regulation', 'motor control improvement']
        
        tasks = {
            "1": {
                "brain_region": random.choice(brain_regions),
                "oscillation_type": random.choice(oscillation_types),
                "therapeutic_goal": random.choice(therapeutic_goals)
            },
            "2": {
                "brain_region": random.choice(brain_regions),
                "oscillation_type": random.choice(oscillation_types),
                "therapeutic_goal": random.choice(therapeutic_goals)
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a novel music therapy system that uses AI to compose music based on neural oscillations, focusing on the {t['brain_region']} and {t['oscillation_type']} waves, with the therapeutic goal of {t['therapeutic_goal']}. Your response should include the following sections:

1. Neuroscientific Foundation (200-250 words):
   a) Explain the role of the {t['brain_region']} in cognition and behavior.
   b) Describe the characteristics and functions of {t['oscillation_type']} waves.
   c) Discuss how these neural oscillations might relate to the therapeutic goal of {t['therapeutic_goal']}.

2. AI-Driven Composition System (250-300 words):
   a) Design an AI system that can generate music based on neural oscillation patterns.
   b) Explain how your system would translate {t['oscillation_type']} waves from the {t['brain_region']} into musical elements (e.g., rhythm, pitch, harmony).
   c) Describe the machine learning algorithms or models you would use for this task.
   d) Discuss how your system would ensure the generated music remains aesthetically pleasing while serving its therapeutic purpose.

3. Therapeutic Application (200-250 words):
   a) Propose a specific protocol for using your AI-generated music in therapy sessions aimed at {t['therapeutic_goal']}.
   b) Explain how the musical elements might interact with neural oscillations to promote the desired therapeutic outcome.
   c) Discuss potential challenges in implementing this therapy and how you would address them.

4. Evaluation Methodology (200-250 words):
   a) Design an experiment to test the efficacy of your music therapy system.
   b) Describe the metrics you would use to measure changes in neural oscillations and therapeutic outcomes.
   c) Explain how you would control for placebo effects and other confounding variables.

5. Ethical Considerations (150-200 words):
   a) Discuss potential risks or ethical concerns associated with using AI-generated music for neural modulation.
   b) Propose guidelines for the responsible development and use of this technology.
   c) Consider potential long-term implications for brain plasticity and cognitive functioning.

Ensure your response demonstrates a deep understanding of neuroscience, music theory, and artificial intelligence. Be creative in your approach while maintaining scientific plausibility and rigor. Use appropriate terminology from all relevant fields and provide explanations where necessary.

Format your response with clear headings for each section. Your total response should be between 1000-1250 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a comprehensive understanding of the specified brain region, neural oscillation type, and their potential relation to the therapeutic goal.",
            "The AI-driven composition system is innovative, well-explained, and effectively translates neural oscillations into musical elements.",
            "The therapeutic application is clearly described and logically connected to the neuroscientific foundation and AI system design.",
            "The evaluation methodology is well-designed and addresses potential confounds and placebo effects.",
            "Ethical considerations are thoughtfully discussed with appropriate guidelines proposed.",
            "The response integrates knowledge from neuroscience, music theory, and artificial intelligence effectively.",
            "The submission is well-structured with clear sections as requested in the instructions."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
