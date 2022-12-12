# Next.js Projects

Next.js projects obviously have a different creation/submission flow than Python project.

## Project Creation

- Base project off [Next + Tailwind Template](https://github.com/vercel/next.js/tree/canary/examples/with-tailwindcss)
- > npx create-next-app --example with-tailwindcss your-awesome-project
- > cd your-awesome-project
- > npm run dev
- Strip out un-needed template code and assets.
- Update included README.md.
- Note: create-next-app will create a git repository for you.
- You will connect your local repo with Github in next step.

## Repositories

### On Github site

- create EMPTY repository e.g. `your-awesome-project` on Github. **Do NOT** initialize with README, license or gitignore.
  - Those will be added soon
- The next screen will have a "Quick Setup" section with a url available to copy. Copy it ;)

### On local system

```sh
> git remote add origin the_url_you_copied_that_ends_with_git
> git push -u origin main
```

Now everything is wired up between local machine and Github.

If you run into issues grab a TA.
