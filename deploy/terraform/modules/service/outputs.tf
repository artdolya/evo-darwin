output "namespace" {
  description = "Namespace the service is deployed to."
  value       = kubernetes_namespace_v1.this.metadata[0].name
}

output "release_name" {
  description = "Name of the Helm release."
  value       = helm_release.this.name
}
