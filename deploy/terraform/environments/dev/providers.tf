# TODO: configure access to the dev cluster in both providers (host, cluster
# CA certificate and credentials, or an exec plugin of the cloud provider).
# With no arguments the providers read the KUBE_* environment variables, for
# example KUBE_CONFIG_PATH.
#
# The namespace is named "evo-darwin" in every environment. If two
# environments share one cluster, give each a different namespace in main.tf.

provider "kubernetes" {}

provider "helm" {}
