import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        environmental_issues = [
            {
                'issue': 'Climate change mitigation',
                'description': 'Reducing greenhouse gas emissions and adapting to global warming'
            },
            {
                'issue': 'Sustainable resource management',
                'description': 'Efficient use and conservation of natural resources'
            }
        ]
        
        behavioral_principles = [
            {
                'principle': 'Nudge theory',
                'description': 'Using positive reinforcement and indirect suggestions to influence behavior'
            },
            {
                'principle': 'Social proof',
                'description': 'People\'s tendency to follow the actions of others'
            }
        ]
        
        tasks = [
            {
                'environmental_issue': random.choice(environmental_issues),
                'behavioral_principle': behavioral_principles[0]
            },
            {
                'environmental_issue': random.choice(environmental_issues),
                'behavioral_principle': behavioral_principles[1]
            }
        ]
        
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that uses the behavioral economics principle of {t['behavioral_principle']['principle']} to optimize individual and collective behavior for {t['environmental_issue']['issue']}. Your response should include:

1. AI System Architecture (300-350 words):
   a) Describe the main components of your AI system and how they interact.
   b) Explain how your system incorporates {t['behavioral_principle']['principle']}.
   c) Detail how the system collects and processes data on individual and collective behavior.
   d) Include a simple ASCII diagram or flowchart of your system architecture.

2. Behavioral Intervention Design (250-300 words):
   a) Explain how your AI system designs and implements behavioral interventions.
   b) Provide examples of specific interventions targeting {t['environmental_issue']['issue']}.
   c) Describe how the system adapts interventions based on user responses and environmental impact.

3. Environmental Impact Assessment (200-250 words):
   a) Propose methods for measuring the environmental impact of behavioral changes.
   b) Explain how your system evaluates the effectiveness of its interventions.
   c) Discuss potential unintended consequences and how your system might detect and mitigate them.

4. Ethical Considerations (200-250 words):
   a) Discuss the ethical implications of using AI and behavioral economics to influence environmental behavior.
   b) Address concerns about privacy, autonomy, and potential misuse of the system.
   c) Propose guidelines for responsible development and use of your AI system.

5. Scalability and Adaptation (150-200 words):
   a) Explain how your system could be scaled up to address global environmental challenges.
   b) Discuss how it might be adapted to different cultural contexts or other environmental issues.

6. Integration with Existing Systems (150-200 words):
   a) Propose how your AI system could be integrated with existing environmental monitoring and policy-making frameworks.
   b) Discuss potential challenges in implementation and how they might be overcome.

Ensure your response demonstrates a deep understanding of environmental science, artificial intelligence, and behavioral economics. Use appropriate technical terminology and provide clear explanations where necessary. Be creative in your approach while maintaining scientific plausibility and ethical responsibility.

Format your response with clear headings for each section. Your total response should be between 1250-1550 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of {t['environmental_issue']['issue']} and how {t['behavioral_principle']['principle']} can be applied to address it.",
            "The AI system design is innovative, coherent, and grounded in principles of both artificial intelligence and behavioral economics.",
            "The proposed behavioral interventions are creative, specific, and likely to be effective.",
            "The response thoroughly addresses ethical considerations and proposes responsible guidelines.",
            "The system's scalability, adaptability, and integration with existing frameworks are well-considered and realistic."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
