output "namespace" {
  description = "Namespace the service is deployed to."
  value       = module.service.namespace
}

output "image_tag" {
  description = "Image tag deployed by the last apply."
  value       = var.image_tag
}
