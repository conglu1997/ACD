import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                'domain': 'Public Health',
                'decision': 'Vaccine Adoption',
                'biases': [
                    ('Availability heuristic', 'Overestimating the probability of events associated with memorable or dramatic occurrences'),
                    ('Confirmation bias', 'Seeking or interpreting information in a way that confirms one\'s preexisting beliefs'),
                    ('Bandwagon effect', 'The tendency to do or believe things because many other people do or believe the same')
                ]
            },
            {
                'domain': 'Financial Markets',
                'decision': 'Investment Strategy',
                'biases': [
                    ('Loss aversion', 'The tendency to prefer avoiding losses over acquiring equivalent gains'),
                    ('Overconfidence bias', 'Overestimating one\'s own abilities or judgments'),
                    ('Anchoring', 'The tendency to rely too heavily on the first piece of information encountered when making decisions')
                ]
            }
        ]
        return {str(i+1): scenario for i, scenario in enumerate(scenarios)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        biases_explained = '\n'.join([f"   - {bias}: {explanation}" for bias, explanation in t['biases']])
        return f"""Design an AI system that simulates human decision-making processes in the domain of {t['domain']}, specifically focusing on the decision of {t['decision']}. Your system should incorporate cognitive biases, emotional factors, and social influences, with particular emphasis on the following biases:

{biases_explained}

Your response should include the following sections:

1. System Architecture (250-300 words):
   a) Describe the key components of your AI system for simulating human decision-making.
   b) Explain how your system models cognitive biases, emotional factors, and social influences.
   c) Discuss any novel elements in your design that enable realistic simulation of human behavior.

2. Bias and Influence Modeling (200-250 words):
   a) Explain how your system represents and simulates the specified cognitive biases.
   b) Describe the mechanisms for modeling emotional factors in decision-making.
   c) Discuss how your model incorporates social influences and their impact on decisions.

3. Decision-Making Process (200-250 words):
   a) Outline the steps your AI system takes to simulate a decision-making process.
   b) Explain how different factors (biases, emotions, social influences) interact in this process.
   c) Describe how your system handles conflicting influences or multiple decision options.

4. Application to the Given Scenario (250-300 words):
   a) Apply your AI system to simulate decision-making in the specified domain and decision context.
   b) Provide a detailed example of how your system would model an individual's decision-making process.
   c) Discuss how the specified biases manifest in this scenario and influence the decision outcome.

5. Validation and Calibration (150-200 words):
   a) Propose methods to validate your AI system against real-world human behavior.
   b) Discuss how you would calibrate and refine your model based on empirical data.
   c) Address potential limitations or ethical considerations in simulating human decision-making.

6. Implications and Applications (150-200 words):
   a) Discuss the potential impact of your AI system on understanding and predicting human behavior.
   b) Explore possible applications in fields such as public policy, marketing, or behavioral economics.
   c) Consider any ethical implications or challenges that might arise from using this technology.

Ensure your response demonstrates a deep understanding of cognitive psychology, behavioral economics, and artificial intelligence. Be creative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section. Your total response should be between 1200-1500 words. Adhere to the specified word count for each section as closely as possible."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of cognitive psychology, behavioral economics, and artificial intelligence.",
            "The AI system design effectively incorporates cognitive biases, emotional factors, and social influences in decision-making simulation.",
            "The application to the given scenario is detailed, plausible, and clearly illustrates the system's capabilities.",
            "The proposed validation and calibration methods are scientifically sound and address potential limitations.",
            "The discussion of implications and applications shows thoughtful consideration of the technology's potential impact and ethical concerns.",
            "The response is creative and innovative while maintaining scientific plausibility.",
            "The writing is clear, well-structured, and uses appropriate technical terminology.",
            "The response adheres to the specified word counts for each section and the overall length."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
