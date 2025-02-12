import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO, StringIO
import base64
from PIL import Image
import numpy as np

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "dataset": "name,age,income\nAlice,30,70000\nBob,45,80000\nCharlie,25,50000\nDavid,35,60000\nEve,40,90000\nFrank,50,100000",
                "task": "Generate a bar plot showing the income distribution by age group (20-30, 31-40, 41-50)."
            },
            "2": {
                "dataset": "date,sales\n2022-01-01,150\n2022-01-02,200\n2022-01-03,250\n2022-01-04,300\n2022-01-05,350\n2022-01-06,400",
                "task": "Generate a line plot showing the sales trend over the given dates."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Analyze the following dataset and generate the specified visualization:

Dataset:
{t['dataset']}

Task: {t['task']}

Submit your visualization as a base64-encoded PNG image string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        try:
            # Decode the base64 image string
            image_data = base64.b64decode(submission)
            image = Image.open(BytesIO(image_data))
            image_array = np.array(image)
        except Exception as e:
            return 0.0

        # Load the dataset
        dataset = pd.read_csv(StringIO(t['dataset']))

        # Generate the expected plot
        if t['task'].startswith('Generate a bar plot'):
            # Expected plot: bar plot
            dataset['age_group'] = pd.cut(dataset['age'], bins=[20, 30, 40, 50], labels=['20-30', '31-40', '41-50'])
            income_by_age_group = dataset.groupby('age_group')['income'].mean().reset_index()
            fig, ax = plt.subplots()
            ax.bar(income_by_age_group['age_group'].astype(str), income_by_age_group['income'])
            plt.xlabel('Age Group')
            plt.ylabel('Average Income')
            plt.title('Income Distribution by Age Group')
        elif t['task'].startswith('Generate a line plot'):
            # Expected plot: line plot
            dataset['date'] = pd.to_datetime(dataset['date'])
            fig, ax = plt.subplots()
            ax.plot(dataset['date'], dataset['sales'])
            plt.xlabel('Date')
            plt.ylabel('Sales')
            plt.title('Sales Trend Over Time')

        # Convert the expected plot to an array
        buffer = BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        expected_image = Image.open(buffer)
        expected_image_array = np.array(expected_image)

        # Compare the generated and expected images
        try:
            # Allow for slight variations in the images
            difference = np.mean((image_array - expected_image_array) ** 2)
            if difference < 1000:  # Further increased threshold for acceptable difference
                return 1.0
            else:
                return 0.0
        except Exception as e:
            return 0.0
