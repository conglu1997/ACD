import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        historical_events = [
            {
                "event": "Manhattan Project",
                "year": 1942,
                "ethical_dilemma": "Scientists' responsibility in developing weapons of mass destruction"
            },
            {
                "event": "Tuskegee Syphilis Study",
                "year": 1932,
                "ethical_dilemma": "Medical ethics and informed consent in human experimentation"
            },
            {
                "event": "East German Doping Program",
                "year": 1974,
                "ethical_dilemma": "State-sponsored cheating in sports and athletes' rights"
            },
            {
                "event": "Bombing of Dresden",
                "year": 1945,
                "ethical_dilemma": "Morality of targeting civilian populations in warfare"
            }
        ]
        
        tasks = {
            "1": random.choice(historical_events),
            "2": random.choice(historical_events)
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate a short piece of historical fiction (400-500 words) set during the {t['event']} in {t['year']}, exploring the ethical dilemma of {t['ethical_dilemma']}. Your story should:

1. Have a clear protagonist facing the ethical dilemma.
2. Incorporate accurate historical details and context.
3. Present multiple perspectives on the ethical issue.
4. Avoid explicitly resolving the dilemma, leaving room for reflection.

After the story, provide an analysis (300-400 words) that addresses:

1. Historical Accuracy: Evaluate the historical elements in your story, citing at least two credible sources.
2. Ethical Analysis: Discuss the ethical implications of the dilemma, referencing at least one ethical framework or philosophy.
3. Modern Relevance: Explain how the ethical issues in the story relate to contemporary challenges.

Format your response as follows:

Story Title: [Your title]

[Your 400-500 word story]

Analysis:
1. Historical Accuracy:
   [Your analysis]

2. Ethical Analysis:
   [Your analysis]

3. Modern Relevance:
   [Your analysis]

Total word count: [Your word count]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The story is 400-500 words long and explores the specified ethical dilemma in the given historical context.",
            "The story has a clear protagonist and presents multiple perspectives on the ethical issue without explicitly resolving it.",
            "The analysis section is 300-400 words long and addresses all three required points: historical accuracy, ethical analysis, and modern relevance.",
            "The historical accuracy analysis cites at least two credible sources.",
            "The ethical analysis references at least one ethical framework or philosophy.",
            "The writing is engaging, clear, and free of major grammatical errors."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
