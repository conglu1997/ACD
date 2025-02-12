import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        domains = ['visual art', 'philosophy']
        art_movements = ['Surrealism', 'Abstract Expressionism', 'Conceptual Art']
        philosophical_topics = ['Existentialism', 'Epistemology', 'Ethics']
        ethical_considerations = ['AI bias', 'Human creativity', 'Intellectual property']
        
        tasks = []
        for domain in domains:
            if domain == 'visual art':
                for movement in art_movements:
                    for consideration in ethical_considerations:
                        tasks.append({
                            'domain': domain,
                            'subject': movement,
                            'ethical_consideration': consideration
                        })
            else:
                for topic in philosophical_topics:
                    for consideration in ethical_considerations:
                        tasks.append({
                            'domain': domain,
                            'subject': topic,
                            'ethical_consideration': consideration
                        })
        
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system capable of generating and critiquing abstract interpretations in {t['domain']}, focusing on {t['subject']}. Then, analyze its output and ethical implications, particularly considering {t['ethical_consideration']}. Your response should include the following sections:

1. AI System Architecture (300-350 words):
   a) Describe the key components of your AI system for abstract reasoning and critique.
   b) Explain how your system processes and generates interpretations in {t['domain']}.
   c) Detail any novel approaches or algorithms used to handle abstract concepts and subjective judgments.
   d) Discuss how your system addresses potential biases and ensures fairness in its interpretations.

2. Knowledge Representation and Reasoning (250-300 words):
   a) Explain how your AI system represents knowledge about {t['subject']}.
   b) Describe the reasoning mechanisms used to generate and evaluate interpretations.
   c) Discuss how your system handles ambiguity and multiple valid interpretations.

3. Interpretation Generation and Critique (300-350 words):
   a) Provide an example of an abstract interpretation or argument your AI system might generate about {t['subject']}.
   b) Demonstrate how your system would critique this interpretation, highlighting strengths and weaknesses.
   c) Explain how your system ensures the coherence and relevance of its interpretations and critiques.

4. Comparative Analysis (200-250 words):
   a) Compare your AI system's approach to interpretation and critique with human approaches in {t['domain']}.
   b) Discuss any unique insights or perspectives your AI system might offer.
   c) Analyze potential limitations of your AI system compared to human experts.

5. Ethical Implications (250-300 words):
   a) Discuss the ethical implications of using AI for abstract reasoning and critique in {t['domain']}.
   b) Analyze potential impacts on human creativity, critical thinking, and the field of {t['domain']}.
   c) Address the specific ethical consideration of {t['ethical_consideration']} in the context of your AI system.
   d) Propose guidelines for responsible development and use of such AI systems in {t['domain']}.

6. Future Directions and Societal Impact (150-200 words):
   a) Suggest two potential applications or extensions of your AI system in other domains.
   b) Discuss how this technology might influence education and professional practice in {t['domain']}.
   c) Propose a research agenda for further exploring the integration of AI and human expertise in abstract reasoning and critique.

Ensure your response demonstrates a deep understanding of {t['domain']}, artificial intelligence, and ethical reasoning. Use appropriate terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific and philosophical rigor.

Format your response with clear headings for each section. Your total response should be between 1450-1750 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of both the specified domain and AI capabilities.",
            "The AI system design is innovative and addresses the challenges of abstract reasoning and critique.",
            "The example interpretation and critique are coherent, relevant, and demonstrate the system's capabilities.",
            "The ethical implications are thoroughly analyzed, with a specific focus on the given ethical consideration.",
            "The response is well-structured and within the specified word count.",
            "The writing demonstrates interdisciplinary knowledge integration and creative problem-solving."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0