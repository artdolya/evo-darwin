.PHONY: format

# Formats the C# code and the Terraform code in place.
# The C# rules are in .editorconfig. Needs the .NET SDK and Terraform.
# src/Krapka links to another repository. Its files are left as they are.
format:
	dotnet format --exclude src/Krapka
	terraform fmt -recursive deploy/terraform
