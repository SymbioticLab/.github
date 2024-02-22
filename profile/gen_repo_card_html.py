import sys

HTML_TEMPLATE = r"""<a href="https://github.com/{username}/{repo}">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://github-readme-stats.vercel.app/api/pin/?username={username}&repo={repo}&theme=github_dark&hide_border=true&description_lines_count=2&show_owner=false">
    <source media="(prefers-color-scheme: light)" srcset="https://github-readme-stats.vercel.app/api/pin/?username={username}&repo={repo}&theme=default_repocard&hide_border=true&description_lines_count=2&show_owner=false">
    <img src="https://github-readme-stats.vercel.app/api/pin/?username={username}&repo={repo}&theme=default_repocard&hide_border=true&description_lines_count=2&show_owner=false" alt="{repo} repo card">
  </picture>
</a>
"""


def main():
    if len(sys.argv) != 3:
        print("Usage: python gen_repo_card_html.py <username> <repo>")
        sys.exit(1)

    username = sys.argv[1]
    repo = sys.argv[2]
    print(HTML_TEMPLATE.format(username=username, repo=repo), end="")


if __name__ == "__main__":
    main()
