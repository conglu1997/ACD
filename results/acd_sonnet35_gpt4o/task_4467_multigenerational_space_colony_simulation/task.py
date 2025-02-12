import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "location": "Mars",
                "initial_population": 1000,
                "primary_challenge": "Radiation exposure",
                "unexpected_event": "Discovery of microbial life"
            },
            {
                "location": "Europa (moon of Jupiter)",
                "initial_population": 500,
                "primary_challenge": "Limited energy resources",
                "unexpected_event": "Sudden geothermal activity"
            }
        ]
        
        tasks = {}
        for i in range(2):
            scenario = random.choice(scenarios)
            tasks[str(i+1)] = scenario
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design and manage a sustainable, multi-generational space colony on {t['location']} with an initial population of {t['initial_population']}. Your primary challenge is {t['primary_challenge']}. Plan for a 200-year timeline, making strategic decisions and ethical choices while balancing various interconnected systems. After 100 years, you will face an unexpected event: {t['unexpected_event']}. Provide your response in the following format:

1. Initial Colony Design (250-300 words):
   a) Describe the physical structure and layout of your colony.
   b) Explain your plans for resource management (e.g., air, water, food, energy).
   c) Outline your governance structure and decision-making processes.

2. 100-Year Development Plan (300-350 words):
   a) Detail your strategies for population growth and genetic diversity.
   b) Explain your approach to education and skill development across generations.
   c) Describe your plans for scientific research and technological advancement.
   d) Discuss how you will maintain social cohesion and cultural development.

3. Ethical Framework (200-250 words):
   a) Outline the core ethical principles guiding your colony's development.
   b) Explain how you will handle potential conflicts between individual rights and collective needs.
   c) Discuss your approach to privacy, surveillance, and information control in the colony.

4. Adaptation to Unexpected Event (250-300 words):
   a) Describe your immediate response to the {t['unexpected_event']}.
   b) Explain how you will adapt your long-term plans in light of this event.
   c) Discuss the ethical implications of your response and any difficult decisions you must make.

5. 200-Year Outcome (200-250 words):
   a) Describe the state of your colony after 200 years.
   b) Reflect on the success of your initial plans and the impact of your adaptations.
   c) Discuss any unforeseen challenges or successes in your colony's development.

Ensure your response demonstrates strategic thinking, ethical reasoning, and the ability to balance competing priorities in a complex, dynamic environment. Use appropriate terminology from relevant fields and provide clear explanations for your decisions.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a comprehensive understanding of the complexities involved in managing a multi-generational space colony",
            "The initial colony design and 100-year development plan are well-thought-out and address key challenges",
            "The ethical framework is clearly defined and consistently applied throughout the response",
            "The adaptation to the unexpected event is logical, creative, and considers long-term implications",
            "The 200-year outcome reflects a realistic projection based on the initial plans and adaptations",
            "The response showcases strategic thinking, ethical reasoning, and the ability to balance competing priorities"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
