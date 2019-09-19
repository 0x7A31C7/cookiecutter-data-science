import yaml
from invoke import Collection, task


@task
def environment(ctx, force=False, no_verbose=False):
    force_opt = '--force' if force else ''
    verbose_opt = '' if no_verbose else '--verbose'

    ctx.run(f'conda env create -f environment.yml {force_opt} {verbose_opt}')
    # Command to create an environment using a spec file: 
    # conda create --name {{ cookiecutter.repo_name }} --file spec-file.txt

    with open('environment.yml') as f:
        env_yml = yaml.load(f, Loader=yaml.FullLoader)

    channels = env_yml['channels']
    with ctx.prefix('source activate {{ cookiecutter.repo_name }}'):
        for channel in channels[::-1]:
            ctx.run(f'conda config --env --add channels {channel}')


@task(post=[environment])
def init(ctx):
    ctx.run('git init && '
            'git add --all && '
            'git commit -m "Initial Commit"')


@task
def freeze(ctx, from_history=False):
    history_opt = '--from-history' if from_history else ''
    env_name = '--name {{ cookiecutter.repo_name }}'

    ctx.run(f'conda env export {env_name} {history_opt} > environment.yml')
    ctx.run(f'conda list {env_name} --explicit > spec-file.txt')


ns = Collection()
ns.add_task(init)
ns.add_task(environment)
ns.add_task(freeze)
ns.configure({'run': {'echo': True, 'warn': False}})
