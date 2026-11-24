module "service" {
  source = "../../modules/service"

  namespace              = "evo-darwin"
  aspnetcore_environment = "Staging"
  replica_count          = 1

  image_repository = var.image_repository
  image_tag        = var.image_tag
}
