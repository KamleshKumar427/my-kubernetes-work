# DevOps with Kubernetes 2026 - submissions

Each exercise is tagged with its number (1.1, 1.2, ...).

## Exercise 1.1 - Log output

`log_output/app.py` generates a random UUID on startup and prints it with a timestamp every 5 seconds.

Build and push the image (run inside `log_output/`):

```bash
docker build -t kkumar42721/log-output:1.1 .
docker push kkumar42721/log-output:1.1
```

Create the deployment:

```bash
kubectl create deployment log-output-dep --image=kkumar42721/log-output:1.1
```

Check the output:

```bash
kubectl get pods
kubectl logs -f <pod-name>
```

## Exercise 1.3 - Declarative approach

Replace the imperative deployment with the manifest in `log_output/manifests/`:

```bash
kubectl delete deployment log-output-dep
kubectl apply -f log_output/manifests/deployment.yaml
kubectl logs -f <pod-name>
```
