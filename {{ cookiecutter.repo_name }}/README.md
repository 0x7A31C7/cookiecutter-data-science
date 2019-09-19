
# {{ cookiecutter.project_name }}

## Steps to Reproduce Results

1. Navigate to the root directory of the repo.
2. Run `invoke environment` to reproduce the analysis environment.

## Project Organization

```
├── README.md               <- The top-level README for developers using this project.
│
├── tasks.py                <- Script with Invoke tasks for running commands like `invoke init` 
│                              or `invoke environment`.
│
├── environment.yml         <- The conda environment file for reproducing the analysis environment, e.g.
│                              generated with `invoke freeze`.
│
├── data
│   ├── raw                 <- The original, immutable data dump.
│   ├── external            <- Data from third party sources.
│   ├── interim             <- Intermediate data that has been transformed.
│   └── processed           <- The final, canonical data sets for modeling.
│
├── models                  <- Trained and serialized models, model predictions, or model summaries.  
│
├── notebooks               <- Jupyter notebooks. Naming convention is a number (for ordering),
│                              the creator's initials, and a short `-` delimited description, e.g.
│                              `1.0-jqp-initial-data-exploration`.   
│
└── references              <- Data dictionaries, manuals, and all other explanatory materials.   
```
