set -x
# helm upgrade -f qa-values.yaml -n helm policy-mgmt .

helm upgrade -f prod-values.yaml -n helm policy-mgmt .  --recreate-pods