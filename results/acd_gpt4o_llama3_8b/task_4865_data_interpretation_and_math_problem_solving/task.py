class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        import matplotlib.pyplot as plt
        import numpy as np
        from io import BytesIO
        import base64

        # Generate sample data and create graphs as images
        x = np.linspace(0, 10, 100)
        y1 = 2 * x + 1
        y2 = x ** 2

        fig1, ax1 = plt.subplots()
        ax1.plot(x, y1, label='y = 2x + 1')
        ax1.set_xlabel('x')
        ax1.set_ylabel('y')
        ax1.legend()
        buf1 = BytesIO()
        plt.savefig(buf1, format='png')
        buf1.seek(0)
        img_str1 = base64.b64encode(buf1.read()).decode('utf-8')
        plt.close(fig1)

        fig2, ax2 = plt.subplots()
        ax2.plot(x, y2, label='y = x^2')
        ax2.set_xlabel('x')
        ax2.set_ylabel('y')
        ax2.legend()
        buf2 = BytesIO()
        plt.savefig(buf2, format='png')
        buf2.seek(0)
        img_str2 = base64.b64encode(buf2.read()).decode('utf-8')
        plt.close(fig2)

        return {
            "1": {
                "graph": img_str1,
                "instructions": "Analyze the provided graph which shows the linear equation y = 2x + 1. Based on the graph, calculate the value of y when x = 5 and when x = 7. Provide a detailed explanation of how you arrived at your answers. Submit your response as a plain text string in the following format:\nExplanation: [Your detailed explanation here]\nAnswers: [Calculated values of y]"
            },
            "2": {
                "graph": img_str2,
                "instructions": "Analyze the provided graph which shows the quadratic equation y = x^2. Based on the graph, calculate the value of y when x = 3 and when x = 6. Provide a detailed explanation of how you arrived at your answers. Submit your response as a plain text string in the following format:\nExplanation: [Your detailed explanation here]\nAnswers: [Calculated values of y]"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Complete the following task based on the given instructions.

Instructions: {t['instructions']}"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The explanation should correctly interpret the graph.",
            "The calculations should be accurate.",
            "The explanation should be clear and logical."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
