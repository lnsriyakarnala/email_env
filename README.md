Email Automation Environment (OpenEnv)
Overview

        This project simulates a real-world email triage system similar to those used in customer support operations. It processes incoming emails by classifying them, determining their priority, and generating appropriate responses.

        The goal is to provide a realistic environment for evaluating how well AI agents can handle practical communication tasks in a structured and measurable way.

Motivation

        Managing large volumes of emails is a common challenge for businesses. Automating this process can significantly improve efficiency, reduce response times, and enhance overall customer experience.

        This environment serves as a standardized benchmark to assess how effectively AI systems can perform these tasks.

OpenEnv Compliance

        The environment follows the OpenEnv interface, ensuring consistency and ease of integration.

        reset() initializes a new task and returns the first observation
        step(action) executes an action and returns the updated observation, reward, completion status, and additional information
        state() provides the current state of the environment
        Data Models

The system uses structured data models:

        Observation: contains email content and related metadata
        Action: represents the classification or generated response
        Reward: a score between 0.0 and 1.0 indicating performance
        Tasks

        The environment includes three levels of difficulty:

        Easy — Email Classification

        The task is to determine whether an email is a refund request.

        Medium — Complaint Detection and Prioritization

        The task is to identify complaint emails and assign an appropriate level of urgency.

        Hard — Response Generation

        The task is to generate a relevant and useful reply to the email.

Grading System

        Each task is evaluated using a deterministic grading system. This ensures that results are consistent and reproducible across runs.

        Scores range from 0.0 to 1.0 and are based on correctness and relevance.

Reward Function

        The reward function provides continuous feedback:

        Correct and relevant outputs receive higher scores
        Incorrect or irrelevant outputs are penalized
        The system encourages gradual improvement over time
        Baseline Agent

        A baseline agent is included in run.py to demonstrate how the environment can be used.

        It uses the OpenAI API when available and falls back to a simple heuristic model for consistency. This ensures reproducible results.

Baseline performance:
Final Score: 0.66

Setup and Usage
Install dependencies

pip install openai pydantic

(Optional) Set API key

setx HF_TOKEN "your_api_key_here"

Run the environment

python run.py

Docker Support

The environment can also be run using Docker.

Build the image:

docker build -t email-env .

Run the container:

docker run email-env

Deployment

        This project is designed to run on platforms such as Hugging Face Spaces and supports containerized deployment.

Key Features

        Simulation of real-world email workflows
        Standardized OpenEnv interface
        Multiple task difficulty levels
        Deterministic and reproducible evaluation
        Continuous reward-based feedback
        Built-in baseline agent
        Future Improvements

Potential enhancements include:

        Expanding the diversity of email datasets
        Supporting multi-turn interactions
        Incorporating more advanced evaluation methods
        Integrating with real customer support systems

Conclusion

        This environment provides a practical and scalable way to evaluate AI agents on real-world communication tasks. It strikes a balance between simplicity, reproducibility, and real-world applicability, making it useful for both research and production use.