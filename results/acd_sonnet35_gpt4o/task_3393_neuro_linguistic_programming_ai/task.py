import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        nlp_techniques = [
            "Anchoring",
            "Reframing",
            "Meta Model",
            "Milton Model",
            "Rapport building"
        ]
        therapeutic_goals = [
            "Anxiety reduction",
            "Depression management",
            "Self-esteem improvement",
            "Stress management",
            "Phobia treatment"
        ]
        tasks = [
            {
                "nlp_technique": technique,
                "therapeutic_goal": goal
            }
            for technique in nlp_techniques
            for goal in therapeutic_goals
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that integrates principles of neurolinguistic programming (NLP) with advanced language models to create a therapeutic conversational agent. Focus on the NLP technique of {t['nlp_technique']} and the therapeutic goal of {t['therapeutic_goal']}. Your response should include the following sections:

1. System Architecture (300-350 words):
   a) Describe the key components of your AI system, including how it integrates NLP principles with language models.
   b) Explain how your system incorporates the specific NLP technique and addresses the given therapeutic goal.
   c) Discuss any novel algorithms or techniques used in your system.
   d) Include a simple diagram or flowchart illustrating the system's architecture.

2. NLP-AI Integration (250-300 words):
   a) Explain how your system translates the chosen NLP technique into AI-implementable processes.
   b) Describe the mapping between NLP principles and AI functionalities.
   c) Discuss any challenges in this integration and how your system addresses them.

3. Therapeutic Interaction Simulation (250-300 words):
   a) Provide a detailed example dialogue between your AI agent and a hypothetical client, demonstrating the use of the specified NLP technique.
   b) Explain how this interaction addresses the given therapeutic goal.
   c) Analyze the AI's responses, highlighting the application of NLP principles and language model capabilities.

4. Ethical Considerations and Safeguards (200-250 words):
   a) Discuss potential ethical issues related to using AI for therapeutic purposes.
   b) Address concerns about privacy, consent, and the limitations of AI in mental health contexts.
   c) Propose specific safeguards and guidelines for the responsible use of your system.

5. Comparative Analysis (200-250 words):
   a) Compare your AI-NLP approach to traditional therapeutic methods and existing mental health chatbots.
   b) Discuss potential advantages and limitations of your system.
   c) Analyze how your approach might complement or challenge current therapeutic practices.

6. Future Developments and Research Directions (150-200 words):
   a) Suggest potential improvements or extensions to your system.
   b) Discuss how this technology might evolve in the next decade.
   c) Propose a research agenda to further explore the intersection of NLP, AI, and mental health therapy.

Ensure your response demonstrates a deep understanding of neurolinguistic programming, language models, therapeutic practices, and AI ethics. Be creative in your approach while maintaining scientific and ethical plausibility. Use appropriate terminology from all relevant fields and provide clear explanations where necessary.

Format your response with clear headings for each section. Your total response should be between 1350-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must demonstrate a clear understanding of the NLP technique {t['nlp_technique']} and how it can be applied to achieve the therapeutic goal of {t['therapeutic_goal']}.",
            "The AI system design should be innovative, logically consistent, and well-explained.",
            "The therapeutic interaction simulation should be realistic and effectively demonstrate the application of NLP principles and AI capabilities.",
            "The response must thoughtfully address ethical considerations and propose meaningful safeguards.",
            "The comparative analysis should be balanced and insightful.",
            "The response should follow the specified format with clear section headings and adhere to the word count guidelines."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
