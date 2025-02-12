import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "enhancement_type": "Memory consolidation",
                "suppression_type": "Traumatic memories",
                "application": "PTSD treatment"
            },
            {
                "enhancement_type": "Skill acquisition",
                "suppression_type": "Cognitive biases",
                "application": "Educational optimization"
            },
            {
                "enhancement_type": "Emotional regulation",
                "suppression_type": "Addictive behaviors",
                "application": "Addiction therapy"
            },
            {
                "enhancement_type": "Sensory perception",
                "suppression_type": "Chronic pain memories",
                "application": "Pain management"
            },
            {
                "enhancement_type": "Decision-making processes",
                "suppression_type": "Implicit biases",
                "application": "Judicial system improvement"
            },
            {
                "enhancement_type": "Creative ideation",
                "suppression_type": "Self-limiting beliefs",
                "application": "Artistic performance enhancement"
            }
        ]
        return {
            "1": random.choice(scenarios),
            "2": random.choice(scenarios)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a hypothetical AI-driven neurotechnology system for selective memory enhancement and suppression, then analyze its potential applications and ethical implications. Your system should focus on {t['enhancement_type']} for enhancement and {t['suppression_type']} for suppression. Analyze its application in {t['application']}. Your response should include the following sections:

1. System Architecture (300-350 words):
   a) Describe the key components of your AI-driven neurotechnology system.
   b) Explain how it interfaces with the human brain to enable memory enhancement and suppression.
   c) Detail the AI algorithms and neural mechanisms involved in the process.
   d) Discuss any novel technologies or approaches used in your design.

2. Memory Manipulation Process (250-300 words):
   a) Explain the step-by-step process of how your system enhances {t['enhancement_type']}.
   b) Describe how the system identifies and suppresses {t['suppression_type']}.
   c) Discuss the precision and limitations of your memory manipulation techniques.
   d) Address potential side effects or unintended consequences of the process.

3. AI Decision-Making Framework (250-300 words):
   a) Outline the criteria your AI system uses to decide which memories to enhance or suppress.
   b) Explain how the AI balances user input with objective measures of memory importance.
   c) Describe safeguards implemented to prevent misuse or unintended memory alterations.
   d) Discuss how the AI system learns and improves its decision-making over time.

4. Application Analysis: {t['application']} (200-250 words):
   a) Analyze how your system could be applied in the specified field.
   b) Discuss potential benefits and risks of using memory manipulation in this context.
   c) Propose a protocol for implementing your system in this application.
   d) Suggest metrics for evaluating the effectiveness and safety of your system in this use case.

5. Ethical Implications (250-300 words):
   a) Identify and discuss key ethical concerns raised by your memory manipulation system.
   b) Analyze potential impacts on personal identity, free will, and social dynamics.
   c) Discuss issues of consent, privacy, and potential for misuse.
   d) Propose ethical guidelines for the development and use of such technology.

6. Societal Impact and Regulation (200-250 words):
   a) Predict potential societal changes that could result from widespread use of your system.
   b) Discuss how existing legal and regulatory frameworks might apply to this technology.
   c) Propose new policies or regulations needed to govern the use of AI-driven memory manipulation.
   d) Consider the global implications and potential for international conflicts over this technology.

Ensure your response demonstrates a deep understanding of neuroscience, artificial intelligence, and neuroethics. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility and ethical responsibility.

Format your response with clear headings for each section. Your total response should be between 1450-1750 words.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a comprehensive understanding of neuroscience, AI, and ethics.",
            "The proposed system design is innovative, detailed, and scientifically plausible.",
            "The memory manipulation process is well-explained and addresses potential challenges.",
            "The AI decision-making framework is thoughtfully designed with appropriate safeguards.",
            "The application analysis is thorough and considers both benefits and risks.",
            "The ethical implications are critically examined with depth and nuance.",
            "The societal impact and regulation discussion shows foresight and understanding of policy challenges.",
            "The response maintains coherence and relevance throughout all sections and adheres to the specified word limits."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
