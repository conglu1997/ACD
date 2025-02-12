import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        languages = ['Mandarin Chinese', 'Arabic', 'Pirahã', 'German']
        decision_domains = ['Resource Allocation', 'Ethical Dilemmas', 'Risk Assessment', 'Social Interactions']
        linguistic_features = ['Tense System', 'Gendered Nouns', 'Evidentiality Markers', 'Honorifics']
        
        tasks = {
            "1": {
                "language": random.choice(languages),
                "decision_domain": random.choice(decision_domains),
                "linguistic_feature": random.choice(linguistic_features)
            },
            "2": {
                "language": random.choice(languages),
                "decision_domain": random.choice(decision_domains),
                "linguistic_feature": random.choice(linguistic_features)
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that makes decisions based on input in {t['language']}, focusing on the decision domain of {t['decision_domain']} and the linguistic feature of {t['linguistic_feature']}. Then, analyze how these language-specific features influence the AI's decision-making process. Your response should include the following sections:

1. AI System Architecture (250-300 words):
   a) Describe the key components of your AI decision-making system.
   b) Explain how it processes input in the specified language.
   c) Detail how it incorporates the given linguistic feature into its decision-making process.
   d) Include a simple diagram of your system architecture using ASCII art or Unicode characters.

2. Language-Specific Processing (200-250 words):
   a) Explain how your system handles the specified linguistic feature in {t['language']}.
   b) Describe any unique challenges or advantages this feature presents for decision-making in the given domain.
   c) Discuss how your system might behave differently if it were processing a language without this feature.

3. Decision-Making Algorithm (200-250 words):
   a) Outline the step-by-step process your AI uses to make decisions in the specified domain.
   b) Explain how language input is weighted and evaluated in this process.
   c) Describe any measures taken to mitigate potential language-based biases in decision-making.

4. Comparative Analysis (200-250 words):
   a) Compare how your AI system might make decisions differently when processing the same information in {t['language']} versus English.
   b) Analyze potential cognitive biases that might emerge from the linguistic features of {t['language']}.
   c) Discuss how these language-specific influences relate to theories of linguistic relativity.

5. Ethical Implications (150-200 words):
   a) Discuss the ethical considerations of using language-specific AI for decision-making in {t['decision_domain']}.
   b) Propose guidelines for ensuring fairness and reducing bias in multilingual AI decision-making systems.

6. Experimental Design (200-250 words):
   a) Propose an experiment to test how your AI system's decisions might vary across different languages.
   b) Describe the methodology, including input data, evaluation metrics, and analysis techniques.
   c) Explain how you would isolate the effects of linguistic features on decision outcomes.

Ensure your response demonstrates a deep understanding of computational linguistics, cognitive psychology, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative in your approach while maintaining scientific plausibility.

Format your answer with clear headings for each section, numbered as above. Your total response should be between 1200-1500 words.

For the system architecture diagram, use ASCII art or Unicode characters to create a clear and informative representation. The diagram should be no larger than 20 lines by 80 characters."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response addresses all required sections comprehensively",
            f"The AI system design clearly incorporates the specified language ({t['language']}), decision domain ({t['decision_domain']}), and linguistic feature ({t['linguistic_feature']})",
            "The language-specific processing and decision-making algorithm are well-defined and logically consistent",
            "The comparative analysis demonstrates insightful reasoning about language-thought interactions",
            "The experimental design shows a deep understanding of linguistic and cognitive factors in AI decision-making",
            "The response includes a clear and informative ASCII art or Unicode diagram of the system architecture"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
