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

print(f"----- [*] GENERATING PROJECT [*] ----- {{cookiecutter.setup_pre_commit_hooks}}")
if "{{cookiecutter.setup_pre_commit_hooks}}":
    subprocess.run(["pre-commit", "install", "--install-hooks"])
else:
    subprocess.run(["rm", ".pre-commit-config.yml"])

