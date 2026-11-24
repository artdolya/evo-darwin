terraform {
  required_version = "~> 1.15"

  required_providers {
    helm = {
      source  = "hashicorp/helm"
      version = "~> 3.3"
    }
    kubernetes = {
      source  = "hashicorp/kubernetes"
      version = "~> 3.5"
    }
  }

  # TODO: configure the remote backend that stores the staging state (type,
  # location, state key and locking). Without a backend Terraform keeps the
  # state in a local file, which the pipeline loses at the end of every run.
}
