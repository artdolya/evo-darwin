locals {
  name       = "evo-darwin"
  chart_path = "${path.module}/../../../helm/evo-darwin"
}

resource "kubernetes_namespace_v1" "this" {
  metadata {
    name = var.namespace
  }
}

resource "helm_release" "this" {
  name      = local.name
  namespace = kubernetes_namespace_v1.this.metadata[0].name
  chart     = local.chart_path

  # Terraform waits until the new pods are ready. If they are not ready in
  # time, Helm rolls the release back and the apply fails.
  atomic  = true
  timeout = 300

  values = [
    yamlencode({
      replicaCount = var.replica_count
      image = {
        repository = var.image_repository
        tag        = var.image_tag
      }
      env = {
        ASPNETCORE_ENVIRONMENT = var.aspnetcore_environment
      }
    })
  ]
}
