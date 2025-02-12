class TaskFamily:
    import matplotlib.pyplot as plt
    import numpy as np
    import io
    import base64

    @staticmethod
    def get_tasks() -> dict[str, dict]:
        import numpy as np
        import matplotlib.pyplot as plt
        import io
        import base64

        # Generate a simple line plot and a complex bar chart as examples
        x = np.linspace(0, 10, 100)
        y = np.sin(x)

        fig, ax = plt.subplots()
        ax.plot(x, y)
        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        line_plot = base64.b64encode(buf.read()).decode('utf-8')
        plt.close()

        categories = ['A', 'B', 'C', 'D']
        values = [10, 23, 38, 5]

        fig, ax = plt.subplots()
        ax.bar(categories, values)
        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        bar_chart = base64.b64encode(buf.read()).decode('utf-8')
        plt.close()

        return {
            "1": {"dataset": "x = np.linspace(0, 10, 100), y = np.sin(x)", "visualization": line_plot},
            "2": {"dataset": "categories = ['A', 'B', 'C', 'D'], values = [10, 23, 38, 5]", "visualization": bar_chart}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        dataset = t['dataset']
        return f"""Based on the provided dataset below, generate a clear and accurate description of the corresponding data visualization. Your description should include the type of chart, key elements, and any notable trends or insights.

Dataset: {dataset}

Provide your description in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The description should accurately identify the type of chart.", "The description should include key elements of the chart.", "The description should highlight any notable trends or insights."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
