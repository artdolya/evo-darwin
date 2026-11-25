.PHONY: format up down

# Formats the C# code and the Terraform code in place.
# The C# rules are in .editorconfig. Needs the .NET SDK and Terraform.
# src/Krapka links to another repository. Its files are left as they are.
format:
	dotnet format --exclude src/Krapka
	terraform fmt -recursive deploy/terraform

# Builds the images of the complete stack and starts it in the background. Needs Docker.
# The stack is the Docker Compose project in src/Docker. See src/Docker/README.md.
up:
	docker compose --project-directory src/Docker up --build --detach

# Stops the complete stack and removes its containers. The data of PostgreSQL stays.
down:
	docker compose --project-directory src/Docker down
