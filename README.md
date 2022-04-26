# "Hello World" Python Lamdba Functions Using Serverless

## Step 1: Package And Deploy The Infrastructure

```bash
sls package
```

```bash
sls deploy
```

## Step 2: Test The Lambda Functions

```bash
sls invoke -f hello-string -d "World"
```

```bash
sls invoke -f hello-json --path data/data.json
```

## Step 3: Remove The Deployed Infrastructure

```bash
sls remove
```
