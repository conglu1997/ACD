import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        emergency_scenarios = [
            "natural disaster response",
            "hostage negotiation",
            "medical triage in mass casualty event",
            "space station critical system failure",
            "cybersecurity breach in critical infrastructure"
        ]
        communication_constraints = [
            "limited vocabulary",
            "time pressure",
            "emotional stress",
            "cultural differences",
            "technical jargon"
        ]
        cognitive_factors = [
            "decision fatigue",
            "information overload",
            "cognitive biases",
            "sensory impairment",
            "multilingual environment"
        ]
        
        tasks = {
            "1": {
                "scenario": random.choice(emergency_scenarios),
                "constraint": random.choice(communication_constraints),
                "cognitive_factor": random.choice(cognitive_factors)
            },
            "2": {
                "scenario": random.choice(emergency_scenarios),
                "constraint": random.choice(communication_constraints),
                "cognitive_factor": random.choice(cognitive_factors)
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design and analyze a specialized language protocol for emergency communication in the scenario of {t['scenario']}, considering the communication constraint of {t['constraint']} and the cognitive factor of {t['cognitive_factor']}. Then, apply this protocol to solve a complex crisis within the given scenario. Provide your response in the following format:

1. Language Protocol Design (250-300 words):
   a) Describe the key features of your specialized language protocol.
   b) Explain how it addresses the given communication constraint and cognitive factor.
   c) Provide examples of specific terms, phrases, or communication structures in your protocol.

2. Cognitive Analysis (200-250 words):
   a) Analyze how your protocol might affect cognitive processes in high-stress situations.
   b) Discuss potential benefits and drawbacks of your approach compared to standard communication.
   c) Explain how your protocol mitigates the specified cognitive factor.

3. Crisis Scenario (250-300 words):
   a) Describe a complex crisis situation within the given emergency scenario.
   b) Explain how key decision-makers would use your language protocol to address the crisis.
   c) Provide a sample dialogue or communication exchange using your protocol.

4. Effectiveness Evaluation (200-250 words):
   a) Assess the potential effectiveness of your protocol in the given scenario.
   b) Discuss any limitations or potential unintended consequences of your approach.
   c) Propose a method to empirically test the effectiveness of your protocol.

5. Broader Implications (150-200 words):
   a) Discuss how your protocol might be adapted for other emergency scenarios.
   b) Explore potential applications of your approach outside of emergency situations.
   c) Consider ethical implications of implementing specialized communication protocols.

Ensure your response demonstrates a deep understanding of linguistics, cognitive science, and crisis management. Be creative in your approach while maintaining plausibility and addressing real-world constraints. Use clear headings for each section and number your paragraphs within each section.

Your total response should be between 1050-1300 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response addresses the specific emergency scenario of {t['scenario']}",
            f"The language protocol design considers the communication constraint of {t['constraint']}",
            f"The cognitive analysis addresses the factor of {t['cognitive_factor']}",
            "The language protocol is creative, yet plausible and practical for emergency use",
            "The crisis scenario and its resolution using the protocol are well-described and logical",
            "The effectiveness evaluation is thorough and includes a proposed empirical test",
            "The response demonstrates interdisciplinary knowledge of linguistics, cognitive science, and crisis management",
            "The broader implications section thoughtfully explores adaptations and ethical considerations",
            "The response adheres to the specified format and word count guidelines"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
