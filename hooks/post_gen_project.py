import subprocess

print()
print("----- [*] INSTALLING PACKAGES [*] -----")
print()

subprocess.run(["poetry", "install", "--with=dev", "--no-root"])

print()
print("----- [*] GENERATING PROJECT [*] -----")

if "{{cookiecutter.initialize_git}}":
    subprocess.run(["git", "init", "."])
else:
    pass

# print(f"----- [*] GENERATING PROJECT [*] ----- {{cookiecutter.setup_pre_commit_hooks}}")
# if "{{cookiecutter.setup_pre_commit_hooks}}":
#     subprocess.run(["pre-commit", "install", "--install-hooks"])
# else:
#     subprocess.run(["rm", ".pre-commit-config.yml"])


# Check if setup_pre_commit_hooks is True
if "{{cookiecutter.setup_pre_commit_hooks}}":
    try:
        # Attempt to install pre-commit hooks
        subprocess.run(["pre-commit", "install", "--install-hooks"], check=True)
    except subprocess.CalledProcessError as e:
        # Handle error if pre-commit installation fails
        print("Error installing pre-commit hooks:", e)
else:
    try:
        # Attempt to remove .pre-commit-config.yml
        subprocess.run(["rm", ".pre-commit-config.yml"], check=True)
    except subprocess.CalledProcessError as e:
        # Handle error if removal fails
        print("Error removing .pre-commit-config.yml:", e)
