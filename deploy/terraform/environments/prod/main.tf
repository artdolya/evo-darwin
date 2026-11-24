module "service" {
  source = "../../modules/service"

  namespace              = "evo-darwin"
  aspnetcore_environment = "Production"

  # TODO: set the replica count from the expected load. Two is a placeholder
  # that keeps the service available while one pod restarts.
  replica_count = 2

  image_repository = var.image_repository
  image_tag        = var.image_tag
}
