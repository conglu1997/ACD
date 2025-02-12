class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            '1': {
                'experiment': 'A ball is dropped from a height of 5 meters. Predict the time it takes for the ball to hit the ground, assuming no air resistance.'
            },
            '2': {
                'experiment': 'A car accelerates from rest at a constant rate of 2 m/s². Predict the distance it covers in 10 seconds.'
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        experiment = t['experiment']
        return f'Predict the outcome of the following physical experiment based on the given initial conditions and principles of physics. Provide your answer with a brief explanation of the reasoning and calculations involved.\n\nExperiment: {experiment}\n\nSubmit your prediction as a plain text string in the following format:\nPrediction: [Your prediction]\nExplanation: [Your explanation]'

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            'The prediction should be physically accurate based on the given initial conditions.',
            'The explanation should logically follow from the principles of physics and clearly outline the steps taken to arrive at the prediction.'
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
