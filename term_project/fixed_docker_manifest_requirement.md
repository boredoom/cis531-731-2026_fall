# Fixed Docker Manifest Requirement

As part of the term project deliverable, any Docker-based solution must demonstrate a **fixed Docker manifest requirement**. The goal is to ensure that your application can be built and deployed reproducibly by referencing **specific, immutable container images** rather than mutable tags such as `latest`.

## What This Means

When using Docker, container images should be referenced by their **SHA256 digest** instead of a tag.

Do not use:

```dockerfile
FROM ubuntu:latest
```

Use:

```dockerfile
FROM ubuntu@sha256:26c68657abce813fc315b0b1008c07f1a79d7d11e3b2e5302ac74c7e890c4d0a
```

A digest is a cryptographic identifier for a specific image build. Unlike tags, digests cannot be changed after publication. This guarantees that anyone rebuilding your project receives the exact same container image.

---

## How to Obtain an Image Digest

If you already have the image locally:

```bash
docker images --digests
```

Or inspect a specific image:

```bash
docker inspect --format='{{index .RepoDigests 0}}' ubuntu:latest
```

Example output:

```text
ubuntu@sha256:26c68657abce813fc315b0b1008c07f1a79d7d11e3b2e5302ac74c7e890c4d0a
```

---

## Docker Compose Example

If your project uses Docker Compose, the image reference should also be pinned by digest:

```yaml
services:
  web:
    image: nginx@sha256:e99b0d363db8efcb2b7f369d72c1c68fa82b5fae5349f2b18aa218f2f4e3f3b9
    ports:
      - "80:80"
```

---

## What to Submit

If your project includes Docker:

- Include your `Dockerfile` and/or `compose.yaml` file(s).
- Ensure all externally referenced container images are pinned to a specific SHA256 digest.
- Do not rely on mutable tags such as `latest`, `stable`, or `v1`.

If your project does **not** use Docker or containerized components, this requirement does not apply.

---

## Why This Requirement Exists

Using fixed image digests provides:

- **Reproducibility:** Future builds use the same container image.
- **Traceability:** The exact image version used for development and testing can be identified.
- **Supply-chain security:** Builds are protected from unexpected changes caused by tag updates or tag overwrites.

### Trade-Off

Pinned images do **not** automatically receive security patches or bug fixes. In production environments, organizations typically pair digest pinning with automated dependency-management tools (such as Renovate or Dependabot) to track and update pinned images over time.

---

## Grading Note

For projects that use Docker, graders will verify that container images are referenced using immutable SHA256 digests rather than mutable tags. Failure to pin container images may result in loss of credit for the fixed Docker manifest requirement.
