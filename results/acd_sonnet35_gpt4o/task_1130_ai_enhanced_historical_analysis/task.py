import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        historical_events = [
            "French Revolution",
            "Industrial Revolution",
            "American Civil War",
            "World War I",
            "Russian Revolution",
            "Great Depression",
            "World War II",
            "Cold War",
            "Civil Rights Movement",
            "Fall of the Berlin Wall"
        ]
        ai_techniques = [
            "Natural Language Processing",
            "Machine Learning",
            "Computer Vision",
            "Network Analysis",
            "Sentiment Analysis",
            "Topic Modeling",
            "Time Series Analysis",
            "Clustering Algorithms",
            "Anomaly Detection",
            "Predictive Modeling"
        ]
        return {
            "1": {
                "event": random.choice(historical_events),
                "ai_technique": random.choice(ai_techniques)
            },
            "2": {
                "event": random.choice(historical_events),
                "ai_technique": random.choice(ai_techniques)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        ai_technique_explanations = {
            "Natural Language Processing": "analyzing and generating human language",
            "Machine Learning": "algorithms that improve through experience",
            "Computer Vision": "analyzing and interpreting visual information",
            "Network Analysis": "studying relationships and connections in data",
            "Sentiment Analysis": "determining the emotional tone of text",
            "Topic Modeling": "discovering abstract topics in a collection of documents",
            "Time Series Analysis": "analyzing time-ordered data points",
            "Clustering Algorithms": "grouping similar data points together",
            "Anomaly Detection": "identifying unusual patterns in data",
            "Predictive Modeling": "using data to predict future outcomes"
        }
        return f"""Design an AI-enhanced historical analysis methodology to study the {t['event']} using {t['ai_technique']} ({ai_technique_explanations[t['ai_technique']]}). Your response should include:

1. Methodology Design (250-300 words):
   a) Describe how you would apply {t['ai_technique']} to analyze the {t['event']}.
   b) Explain the specific historical data or sources you would use for this analysis.
   c) Outline the steps in your methodology, from data collection to interpretation.
   d) Discuss any potential limitations or biases in your approach.

2. Expected Insights (200-250 words):
   a) Hypothesize three new insights or alternative interpretations that your AI-enhanced method might uncover about the {t['event']}.
   b) Explain how these insights differ from traditional historical analyses.
   c) Discuss the potential implications of these new interpretations for our understanding of the event and its historical context.

3. Comparative Analysis (200-250 words):
   a) Compare your AI-enhanced method with traditional historical research methods.
   b) Discuss the advantages and disadvantages of your approach.
   c) Explain how your method might complement or challenge existing historiographical approaches.

4. Ethical Considerations (150-200 words):
   a) Discuss potential ethical issues arising from using AI to analyze historical events.
   b) Address concerns about algorithmic bias and its impact on historical interpretation.
   c) Propose guidelines for responsible use of AI in historical research.

5. Future Directions (150-200 words):
   a) Suggest two potential extensions or improvements to your methodology.
   b) Propose a new research question about the {t['event']} that could be explored using your AI-enhanced approach.
   c) Discuss how this methodology could be applied to other historical events or periods.

Ensure your response demonstrates a deep understanding of both the historical event and the AI technique. Be innovative in your approach while maintaining historical rigor and plausibility. Use appropriate terminology from both history and AI fields.

Format your response with clear headings for each section. Your total response should be between 950-1200 words, with each section adhering to the specified word limits."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response accurately describes how {t['ai_technique']} can be applied to analyze the {t['event']}.",
            "The methodology is well-structured and logically sound.",
            "The hypothesized insights are novel and plausible given the AI-enhanced approach.",
            "The comparative analysis demonstrates a clear understanding of both AI and traditional historical methods.",
            "Ethical considerations are thoughtfully addressed.",
            "The response shows creativity and innovation while maintaining historical accuracy.",
            "The proposed future directions are relevant and promising.",
            "The answer demonstrates a deep understanding of both historical analysis and AI techniques.",
            "The response addresses all required sections with appropriate detail and length.",
            "The total response is between 950-1200 words.",
            f"The response specifically addresses the {t['ai_technique']} technique and the {t['event']}."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
