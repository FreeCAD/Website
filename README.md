> [!NOTE]
> This is the `pages` branch of the FreeCAD website repository.
> Only the temporary build artifacts are stored here. Do not use for development. Use the `main` branch instead.
> See [FreeCAD Website](https://github.com/FreeCAD/Website) repository.


# FreeCAD website `pages` branch

This branch is built automatically with GitHub CI/CD.

For the `main` branch, `hugo-main.yaml` action workflow is used.

For Pull Request temporary builds triggering a Preview, `pr-preview.yaml` action workflow is used. PR Preview artifacts are stored in sub-directories named `/pr-<number>`.

The resulting website is visible at https://freecad.github.io/website/.