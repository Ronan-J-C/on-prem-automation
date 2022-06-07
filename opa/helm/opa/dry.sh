set -x
helm install -f qa-values.yaml -o yaml  --dry-run --debug -n helm policy-mgmt .