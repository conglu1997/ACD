import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        biological_inspirations = [
            {
                'inspiration': 'bacterial flagella',
                'function': 'propulsion',
                'target': 'brain tumor'
            },
            {
                'inspiration': 'virus capsid',
                'function': 'encapsulation',
                'target': 'liver cells'
            },
            {
                'inspiration': 'cell membrane',
                'function': 'selective permeability',
                'target': 'lung tissue'
            },
            {
                'inspiration': 'antibody',
                'function': 'recognition',
                'target': 'cancer cells'
            }
        ]
        return {str(i+1): random.choice(biological_inspirations) for i in range(2)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a biomimetic nanobot system for targeted drug delivery, inspired by {t['inspiration']} and utilizing principles of nanotechnology. Your nanobot should be designed to target {t['target']}. The primary function you should focus on is {t['function']}.

Your response should include the following sections:

1. Nanobot Design (300-350 words):
   a) Describe the overall structure and components of your nanobot.
   b) Explain how your design mimics the biological inspiration ({t['inspiration']}).
   c) Detail the nanoscale materials and fabrication techniques you would use.
   d) Discuss how your nanobot achieves the primary function of {t['function']}.

2. Targeting Mechanism (250-300 words):
   a) Explain how your nanobot specifically targets {t['target']}.
   b) Describe any surface modifications or targeting ligands used.
   c) Discuss potential challenges in achieving precise targeting and how you address them.

3. Drug Delivery Mechanism (250-300 words):
   a) Detail how your nanobot would carry and release the drug payload.
   b) Explain the trigger mechanism for drug release (e.g., pH change, enzymatic action, external stimulus).
   c) Discuss how your design ensures controlled and efficient drug delivery.

4. Nanobot-Body Interaction (200-250 words):
   a) Analyze potential interactions between your nanobot and the human body.
   b) Discuss biocompatibility and biodegradability of your nanobot.
   c) Address potential immune responses and how your design mitigates them.

5. Ethical Considerations and Future Applications (200-250 words):
   a) Discuss ethical implications of using nanobots for drug delivery.
   b) Propose two potential future applications of your nanobot technology beyond drug delivery.
   c) Suggest one major challenge that needs to be overcome for widespread adoption of nanobot drug delivery systems.

6. Performance Metrics (100-150 words):
   Propose three quantitative metrics to evaluate the performance of your nanobot system, explaining how each metric would be measured and its significance.

Ensure your response demonstrates a deep understanding of biology, nanotechnology, and medical applications. Use appropriate technical terminology and provide explanations where necessary. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Include at least one equation or chemical formula relevant to your design. Your total response should be between 1300-1600 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The nanobot design clearly mimics {t['inspiration']} and effectively achieves the function of {t['function']}.",
            f"The targeting mechanism for {t['target']} is well-explained, scientifically plausible, and addresses potential challenges.",
            "The drug delivery mechanism is innovative, addresses controlled release effectively, and includes a detailed explanation of the trigger mechanism.",
            "The response demonstrates a deep understanding of nanobot-body interactions, including biocompatibility, biodegradability, and immune responses.",
            "Ethical considerations are thoroughly addressed, and future applications are creative, well-reasoned, and extend beyond drug delivery.",
            "The proposed performance metrics are quantitative, relevant, and their measurement and significance are clearly explained.",
            "The response includes at least one relevant equation or chemical formula.",
            "The response shows a strong integration of knowledge from biology, nanotechnology, and medicine throughout, using appropriate technical terminology.",
            "The response follows the required format and word count guidelines, and demonstrates originality and depth of thought throughout."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
