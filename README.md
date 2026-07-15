# Cloudflare R2 Uploader

A simple Python script to upload and update files in a Cloudflare R2 bucket.

## Overview

While this tool is versatile and can be used for any file upload use case, it is specifically designed to facilitate easy updates to hosted files via Cloudflare R2.

### Personal Use Case: CV Management

I use this repository to maintain an up-to-date version of my CV across all platforms. By uploading the latest CV to a fixed location in an R2 bucket, any links pointing to that bucket's public URL (e.g., on LinkedIn, personal website, or portfolio) will always serve the most recent version without needing to update the links themselves.

## Prerequisites

- A Cloudflare R2 bucket.
- Python 3.x installed.
- Environment variables configured (see [Configuration](#configuration)).

## Configuration

### Local Development
Create a `.env` file in the root directory with the following variables:

```env
R2_ENDPOINT_URL=your_r2_endpoint_url
R2_ACCESS_KEY_ID=your_access_key_id
R2_SECRET_ACCESS_KEY=your_secret_access_key
BUCKET_NAME=your_bucket_name
FILE_TO_UPLOAD=your_file_to_upload.txt
```

### GitHub Actions (Automation)
To enable automated deployment via GitHub Actions, add the following secrets to your GitHub repository (`Settings > Secrets and variables > Actions`):

- `R2_ENDPOINT_URL`
- `R2_ACCESS_KEY_ID`
- `R2_SECRET_ACCESS_KEY`
- `BUCKET_NAME`
- `FILE_TO_UPLOAD`

## Installation

1. Clone the repository.
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Automated Deployment
The repository is configured with a GitHub Action that automatically uploads your file to your R2 bucket. This action is triggered when you push changes to the `main` branch involving `CV.pdf` (or related script files) **AND** the commit message contains the phrase `upload new cv`.

Simply update your file and push to GitHub with the required commit message:
```bash
git add CV.pdf
git commit -m "upload new cv"
git push origin main
```

### Manual Upload
Ensure your `.env` is configured correctly with `BUCKET_NAME` and `FILE_TO_UPLOAD`, then simply run the script:

```bash
python upload.py
```

*Note: The script will dynamically read the target bucket and file path from your environment configuration.*
