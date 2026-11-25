variable "image_repository" {
  description = "Container image repository without a tag, for example <registry>/<path>/evo-darwin."
  type        = string

  validation {
    condition     = length(var.image_repository) > 0
    error_message = "image_repository must not be empty. In the pipeline it comes from the repository variable IMAGE_REPOSITORY."
  }
}

variable "image_tag" {
  description = "Container image tag to deploy. The Release workflow passes the version tag, for example 0.0.1 or 0.0.1-PR2-003."
  type        = string

  validation {
    condition     = length(var.image_tag) > 0
    error_message = "image_tag must not be empty."
  }
}
