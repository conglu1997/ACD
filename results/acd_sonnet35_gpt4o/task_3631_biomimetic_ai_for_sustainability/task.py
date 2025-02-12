import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "ecosystem": "coral reef",
                "challenge": "ocean acidification"
            },
            {
                "ecosystem": "rainforest",
                "challenge": "deforestation"
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a highly innovative biomimetic AI system inspired by the {t['ecosystem']} ecosystem to address the environmental challenge of {t['challenge']}. Your design should be original and push the boundaries of current AI and biomimicry applications. Then, analyze its potential impact and ethical implications. Your response should include:

1. Ecosystem Analysis (200-250 words):
   a) Describe the key characteristics and processes of the {t['ecosystem']} ecosystem relevant to addressing {t['challenge']}.
   b) Identify specific biological mechanisms or strategies that could be adapted for an AI system.
   c) Explain how these natural strategies contribute to the ecosystem's resilience or efficiency.

2. Biomimetic AI System Design (300-350 words):
   a) Propose an original AI system architecture that mimics the identified biological mechanisms.
   b) Explain how your system integrates biomimetic principles with cutting-edge AI technologies.
   c) Describe the key components and their interactions within your system.
   d) Discuss how your innovative system would approach solving the {t['challenge']} problem.

3. Implementation and Scalability (200-250 words):
   a) Outline the steps required to implement your biomimetic AI system.
   b) Discuss potential challenges in translating biological processes to AI algorithms.
   c) Explain how your system could be scaled to address the {t['challenge']} problem on a global level.

4. Environmental Impact Assessment (200-250 words):
   a) Analyze the potential positive and negative environmental impacts of your system.
   b) Compare the efficiency and effectiveness of your biomimetic approach to traditional solutions.
   c) Discuss any potential unintended consequences and how they might be mitigated.

5. Ethical Implications (150-200 words):
   a) Identify ethical considerations related to implementing your biomimetic AI system.
   b) Discuss potential impacts on local communities and ecosystems.
   c) Propose guidelines for responsible development and deployment of your system.

6. Future Research Directions (100-150 words):
   a) Suggest two potential improvements or extensions to your biomimetic AI system.
   b) Propose an experiment to validate the effectiveness of your approach.
   c) Discuss how your system might contribute to our understanding of both natural ecosystems and artificial intelligence.

Ensure your response demonstrates a deep understanding of the chosen ecosystem, relevant biological processes, AI technologies, and environmental science. Be highly innovative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1150-1450 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must demonstrate a deep understanding of the {t['ecosystem']} ecosystem and its relevance to addressing {t['challenge']}.",
            "The biomimetic AI system design should clearly integrate biological principles with cutting-edge AI technologies in an innovative and original manner.",
            "The analysis should include a thorough consideration of implementation challenges, environmental impacts, and ethical implications.",
            "The response should be highly creative and push the boundaries of current AI and biomimicry applications while maintaining scientific plausibility.",
            "The submission must adhere to the specified structure and word count guidelines."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
