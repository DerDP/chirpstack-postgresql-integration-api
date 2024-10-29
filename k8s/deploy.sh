kubectl  create secret generic fastapi-chirpstack-secrets --from-env-file=../code/app/.env
kubectl apply -f .