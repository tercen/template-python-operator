
# Template Python Operator

Cell-wise mean calculated implemented in Python.

## Python operator - Development workflow

* Set up [the Tercen Studio development environment](https://github.com/tercen/tercen_studio)
* Create a new git repository based on the [template Python operator](https://github.com/tercen/template-python-operator)
* Open VS Code Server by going to: http://127.0.0.1:8443
* Clone this repository into VS Code (using the 'Clone from GitHub' command from the Command Palette for example)
* Load the environment and install core requirements by running the following commands in the terminal:

```bash
source /config/.pyenv/versions/3.9.0/bin/activate
pip install -r requirements.txt
```

* Develop your operator. Note that you can interact with an existing data step by specifying arguments to the `TercenContext` function:

```python
tercenCtx = ctx.TercenContext()
```

```python
tercenCtx = ctx.TercenContext(
    workflowId="YOUR_WORKFLOW_ID",
    stepId="YOUR_STEP_ID",
    username="admin", # if using the local Tercen instance
    password="admin", # if using the local Tercen instance
    serviceUri = "http://tercen:5400/" # if using the local Tercen instance 
)
```

* Generate requirements

```bash
python3 -m tercen.util.requirements . > requirements.txt
```

* Push your changes to GitHub: triggers CI GH workflow
* Tag the repository: triggers Release GH workflow
* Go to tercen and install your operator


## Helpful Commands

### Install Tercen Python Client

```bash
python3 -m pip install --force git+https://github.com/tercen/tercen_python_client@0.7.1
```

### Wheel

Though not strictly mandatory, many packages require it.

```bash
python3 -m pip install wheel
```


## Required GitHub secrets (release workflow)

| Secret | Purpose |
|---|---|
| `TERCEN_TEST_OPERATOR_USERNAME` / `_PASSWORD` / `_URI` | Tercen instance used by the release install check |
| `TERCEN_GITHUB_TOKEN` | **Classic** personal access token with `repo` scope, set as an org secret. Needed so the Tercen server can download this repo's zipball during the install check (required for private repos). Fine-grained tokens (`github_pat_...`) do **not** work on the zipball endpoint; the built-in `GITHUB_TOKEN` gives a 404. |

## GitHub Container Registry Visibility

Every ghcr.io package starts **private** the first time an image is pushed, **whatever the repository's visibility**. A public repository does not make its package public: on 2026-10-07 the public repositories `pamgene/dotplot_operator`, `pamgene/combat_operator` and `pamgene/ps12image_operator` all had private packages. Repository and package visibility are set independently.

A private package cannot be pulled by Tercen/BioNavigator. The release install check or a run fails with one of:

```
reading manifest <tag> in ghcr.io/<org>/<name>: denied
unable to retrieve auth token: invalid username/password: unauthorized
```

Both are ghcr's answer to an anonymous request for a private package.

**To make the package public** (once, after the first image push):

1. If the "Public" option is not available, an org owner must first allow public packages at `https://github.com/organizations/YOUR_ORG/settings/packages` ("Package creation"). If that setting is locked, it is set by an enterprise policy.
2. Open `https://github.com/orgs/YOUR_ORG/packages/container/YOUR_PACKAGE/settings`.
3. Under "Danger Zone", click "Change visibility", select "Public" and confirm with the package name.

There is no REST endpoint to change package visibility; it is a manual step. Per GitHub, a public package cannot be made private again.

**Verify without credentials** (200 = public, 403 = private or tag missing):

```bash
PKG=YOUR_ORG/YOUR_PACKAGE
TOKEN=$(curl -s "https://ghcr.io/token?scope=repository:$PKG:pull" | python3 -c "import json,sys; print(json.load(sys.stdin)['token'])")
curl -s -o /dev/null -w '%{http_code}\n' -H "Authorization: Bearer $TOKEN" "https://ghcr.io/v2/$PKG/tags/list"
```
