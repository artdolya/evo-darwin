variable "namespace" {
  description = "Kubernetes namespace the service is deployed to. The module creates it."
  type        = string
  default     = "evo-darwin"
}

variable "image_repository" {
  description = "Container image repository without a tag, for example <registry>/<path>/evo-darwin."
  type        = string
}

variable "image_tag" {
  description = "Container image tag to deploy. The Release workflow passes the version tag, for example 0.0.1 or 0.0.1-PR2-003."
  type        = string
}

variable "aspnetcore_environment" {
  description = "Value of ASPNETCORE_ENVIRONMENT in the container: Development, Staging or Production."
  type        = string

  validation {
    condition     = contains(["Development", "Staging", "Production"], var.aspnetcore_environment)
    error_message = "aspnetcore_environment must be Development, Staging or Production."
  }
}

variable "replica_count" {
  description = "Number of pods."
  type        = number
  default     = 1
}
