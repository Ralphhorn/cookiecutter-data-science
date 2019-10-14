import os
from subprocess import call

def create_envrc(filepath):
    # make backup of original envrc
    if os.path.exists(filepath):
        os.rename(filepath, f"{filepath}.bak")
        print(f"Saved original .envrc at {filepath}")

    env_variables = dict()
    env_variables["DOCKER_PASSWORD"] = input("Docker password:\n")
    env_variables["LOCAL_USERNAME"] = input("Local username:\n")
    env_variables["DOCKER_NAME"] = os.path.split(os.path.split(filepath)[0])[1]
    env_variables["WORKSPACE_ROOT"] = '$( cd "$(dirname "${BASH_SOURCE[0]}")" >/dev/null 2>&1 && pwd )'

    with open(filepath, "w+") as file:
        for key, value in env_variables.items():
            file.write(f"{key}={value}\n")


def create_env(filepath):
    # make backup of original env
    if os.path.exists(filepath):
        os.rename(filepath, f"{filepath}.bak")
        print(f"Saved original .env at {filepath}")

    with open(filepath, "w+") as file:
        file.write(
            f"# Environment variables go here, can be read by `python-dotenv` package:\n"
            f"#   `src/script.py`\n"
            f"#   ----------------------------------------------------------------\n"
            f"#    import dotenv\n"
            f"#\n"
            f"#    project_dir = os.path.join(os.path.dirname(__file__), os.pardir)\n"
            f"#    dotenv_path = os.path.join(project_dir, '.env')\n"
            f"#    dotenv.load_dotenv(dotenv_path)\n"
            f"#   ----------------------------------------------------------------\n"
            f"#\n"
            f"# DO NOT ADD THIS FILE TO VERSION CONTROL!\n\n"
            f"source .envrc\n")


def main():
    path = os.path.split(os.path.realpath(__file__))[0]
    env_path = os.path.join(path, '.env')
    envrc_path = os.path.join(path, '.envrc')
    docker_path = os.path.join(path, '.envrc')

    # make .env file
    if not os.path.exists(env_path):
        create_env(env_path)
    else:
        if input('.env exists \n Overwrite .env? \n[0]: No\n[1]: Yes\n') == '1':
            create_env(env_path)
            print('overwritten .env')
    # make .envrc file
    if not os.path.exists(envrc_path):
        create_envrc(envrc_path)
    else:
        if input('.envrc exists \n Overwrite .envrc? \n[0]: No\n[1]: Yes\n') == '1':
            create_envrc(envrc_path)
            print('overwritten .envrc')
    if os.path.exists(docker_path):
        if input('Docker found\nBuild Docker Container? \n[0]: No\n[1]: Yes\n') == '1':
            call(os.path.join(docker_path,"build_container.sh"))


if __name__ == '__main__':
    main()
