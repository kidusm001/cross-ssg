# cross-ssg

**cross-ssg** is a static site generator written in Python, designed to convert Markdown files into HTML pages. It uses a custom template for consistent styling and supports various Markdown features.

## Features

-   **Markdown Parsing:** Converts Markdown files to HTML.
-   **Supports:** bold, italic, code, links and images
-   **Templating:** Uses a custom HTML template (#template.html) to wrap content.
-   **Static Asset Handling:** Copies static assets (CSS, images) from the `static/` directory to the output `docs/` directory.
-   **Directory Structure:** Supports nested content directories for generating multiple pages.
-   **Base Path:**  Allows specifying a base path for the site, useful for deployment in subdirectories.

## Directory Structure

```
cross-ssg/
├── content/                # Markdown content files
│   ├── index.md            # Main page content
│   ├── blog/               # Blog posts
│   │   ├── glorfindel/
│   │   │   └── index.md
│   │   ├── tom/
│   │   │   └── index.md
│   │   └── majesty/
│   │       └── index.md
│   └── contact/            # Contact page
│       └── index.md
├── docs/                   # Output directory for generated HTML
│   ├── index.html          # Main page
│   ├── blog/               # Blog posts
│   │   ├── glorfindel/
│   │   │   └── index.html
│   │   ├── tom/
│   │   │   └── index.html
│   │   └── majesty/
│   │       └── index.html
│   ├── contact/            # Contact page
│   │   └── index.html
│   ├── index.css           # Stylesheet
│   └── images/             # Images
│       ├── glorfindel.png
│       ├── rivendell.png
│       ├── tolkien.png
│       └── tom.png
├── src/                    # Source code
│   ├── block_converter.py  # Converts Markdown into blocks
│   ├── block_func.py       # Determines block types
│   ├── blocknode.py        # Defines BlockType enum
│   ├── extract_md.py       # Extracts Markdown links and images
│   ├── htmlnode.py         # Defines HTML node structure
│   ├── main.py             # Main script for site generation
│   ├── markdown_to_html.py # Converts Markdown to HTML
│   ├── node_converter.py   # Converts text nodes to HTML nodes
│   ├── split_nodes_delimiter.py # Splits text nodes by delimiters
│   ├── test_blocks.py      # Unit tests for block conversion
│   ├── test_htmlnode.py    # Unit tests for HTML node conversion
│   ├── test_main.py        # Unit tests for main script
│   ├── test_textnode.py    # Unit tests for text nodes
│   ├── text_converter.py   # Converts text to text nodes
│   └── textnode.py         # Defines TextNode class
├── static/                 # Static assets (CSS, images)
│   ├── index.css           # Main stylesheet
│   └── images/             # Images
│       ├── glorfindel.png
│       ├── rivendell.png
│       ├── tolkien.png
│       └── tom.png
├── template.html           # HTML template file
├── .gitignore              # Specifies intentionally untracked files that Git should ignore
├── README.md               # This file
├── test.sh                 # Script to run unit tests
├── build.sh                # Script to build the site
└── main.sh                 # Script to run the project and serve the docs directory
```

## Installation

1.  **Clone the repository:**

    ```sh
    git clone https://github.com/kidusm001/cross-ssg.git
    cd cross-ssg
    ```

2.  **Create a virtual environment (optional):**

    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Dependencies:**

    This project relies only on the Python standard library.

## Usage

### Building the Site

Run the `build.sh` script (#build.sh) to generate the static site:

```sh
./build.sh
```

This script executes main.py (#src/main.py), which:

-   Copies static assets from the static directory to the docs directory.
-   Reads Markdown files from the content directory.
-   Uses template.html (#template.html) to generate HTML files in the docs directory.
-   Applies a base path (specified in build.sh) to all links and image sources.

You can customize the base path by directly executing main.py:

```sh
python3 src/main.py "/custom-base/"
```

### Running a Local Server

To preview the generated site, use the main.sh script (#main.sh):

```sh
./main.sh
```

This script first builds the site and then starts a simple HTTP server in the docs directory, making the site accessible at `http://localhost:8888`.

### Testing

Run the test.sh script (#test.sh) to execute the unit tests:

```sh
./test.sh
```

This script uses the `unittest` module to discover and run all tests in the src directory.

### GitHub Pages Deployment

To deploy your `cross-ssg` site using GitHub Pages, follow these steps:

1.  **Configure the Base Path:**

    -   In `build.sh`, ensure the base path matches your repository name. For example, if your repository is `https://github.com/yourusername/cross-ssg`, the base path should be `/cross-ssg/`.

    ```bash
    #!/bin/sh
    # filepath: /home/kidus/workspace/github.com/kidusm001/cross-ssg/build.sh
    python3 src/main.py "/cross-ssg/"
    ```

2.  **Build the Site:**

    ```sh
    ./build.sh
    ```

3.  **Initialize a Git Repository (if you haven't already):**

    ```sh
    git init
    ```

4.  **Commit and Push to GitHub:**

    ```sh
    git add .
    git commit -m "Initial commit"
    git branch -M main
    git remote add origin https://github.com/yourusername/cross-ssg.git
    git push -u origin main
    ```

5.  **Enable GitHub Pages:**

    -   Go to your repository on GitHub.
    -   Navigate to "Settings" -> "Pages".
    -   In the "Source" section, select "Deploy from a branch".
    -   Choose the `main` branch and `/docs` folder as the source.
    -   Click "Save".

    GitHub Pages will now build and deploy your site from the `docs` directory.  It might take a few minutes for the site to become live.  You can check the status under "Settings" -> "Pages".

6.  **Access Your Site:**

    Your site will be available at `https://yourusername.github.io/cross-ssg/`.

## Contributing

Contributions are welcome! Fork the repository and submit pull requests. For major changes, please open an issue first to discuss the proposed changes.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgments

-   Inspired by the [Boot.dev](https://www.boot.dev) static site generator course.
-   Demonstrates text parsing, modular design, and static site generation in Python.
