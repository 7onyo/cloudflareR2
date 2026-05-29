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

Create a `.env` file in the root directory with the following variables:

```env
R2_ENDPOINT_URL=your_r2_endpoint_url
R2_ACCESS_KEY_ID=your_access_key_id
R2_SECRET_ACCESS_KEY=your_secret_access_key
```

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

Run the `upload.py` script and pass the path to your file as an argument:

```bash
python upload.py path/to/your/file.ext
```

*Note: By default, the current script is configured to upload to a bucket named `myresume` and save the file as `CV.pdf`. This can be easily modified in `upload.py` to suit other filenames or buckets.*
