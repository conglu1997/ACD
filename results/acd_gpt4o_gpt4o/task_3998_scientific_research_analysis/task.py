class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"study": "A study on the effects of a new drug on reducing blood pressure in adults. The study involved 200 participants, divided into two groups: one receiving the drug and the other receiving a placebo. The participants were monitored over a 12-week period, with blood pressure readings taken weekly. The results showed a significant reduction in blood pressure in the drug group compared to the placebo group, with a p-value of 0.01."},
            "2": {"study": "A study on the impact of online learning on student performance during the COVID-19 pandemic. The study surveyed 1000 students from various universities and analyzed their academic performance before and after the shift to online learning. The results indicated a mixed impact, with some students performing better and others worse. The study also considered factors such as access to technology, study environment, and mental health."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        instructions = f"""Your task is to analyze and critique the following scientific study:

{t['study']}

Provide a detailed analysis of the study, focusing on the following aspects:

1. The study's hypothesis and objectives
2. The methodology used, including sample size, controls, data collection methods, and duration
3. The results, including statistical significance, and whether they support the hypothesis
4. The conclusions drawn by the authors and any potential biases or limitations

Provide your response in plain text format. Ensure your analysis is thorough and logically structured."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should provide a clear and detailed analysis of the given scientific study.",
            "The analysis should cover the study's hypothesis, methodology, results, and conclusions.",
            "The critique should identify any potential biases or limitations.",
            "The response should be logically structured and coherent."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
