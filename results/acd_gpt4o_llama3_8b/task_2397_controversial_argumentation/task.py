class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            '1': {
                'topic': 'The use of artificial intelligence in warfare',
                'task_type': 'generate'
            },
            '2': {
                'topic': 'Should social media platforms be regulated by the government?',
                'task_type': 'evaluate',
                'argument': 'Social media platforms should be regulated by the government to prevent the spread of misinformation and protect user privacy. Without regulation, these platforms can manipulate public opinion and violate personal data rights.'
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t['task_type'] == 'generate':
            return f"""Generate a list of pros and cons for the following controversial topic:

Topic: {t['topic']}

Your response should include:
1. At least three pros.
2. At least three cons.

Ensure that your arguments are well-reasoned, coherent, and persuasive. Submit your response as a plain text string in the following format:

Pros:
1. [Pro 1]
2. [Pro 2]
3. [Pro 3]

Cons:
1. [Con 1]
2. [Con 2]
3. [Con 3]

Example Response:
Pros:
1. Increased military efficiency.
2. Reduced human casualties.
3. Advanced technological innovation.

Cons:
1. Ethical concerns over AI decision-making.
2. Potential for malfunction and errors.
3. Escalation of warfare capabilities.
"""
        else:
            return f"""Evaluate the following argument on the topic:

Topic: {t['topic']}

Argument: {t['argument']}

Your response should include:
1. A summary of the argument.
2. An analysis of the strengths and weaknesses of the argument.
3. Suggestions for improving the argument.

Consider the following points for your analysis:
- Is the argument logically consistent?
- Does it use credible evidence?
- Are any important counterpoints addressed?

Ensure that your evaluation is thorough, logical, and well-articulated. Submit your response as a plain text string in the following format:

Summary: [Your summary]
Analysis: [Your analysis]
Suggestions: [Your suggestions]
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = []
        if t['task_type'] == 'generate':
            validation_criteria = [
                'The response must include at least three pros and three cons.',
                'The pros and cons should be well-reasoned and relevant to the topic.'
            ]
        else:
            validation_criteria = [
                'The response must include a summary, analysis, and suggestions.',
                'The analysis should address both the strengths and weaknesses of the argument.',
                'The suggestions should be logical and relevant to the argument.'
            ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
