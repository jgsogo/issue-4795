# issue-4795
Repo for Conan issue 4795

## Local workflow

```bash
$> git clone https://github.com/jgsogo/issue-4795.git
$> cd issue-4795
$> mkdir _build
$> cd _build
$> conan install ..
$> conan source ..
$> conan build ..
$> ./iprc
```

If you try to run this steps again, the `conan source ..` one will 
fail because you cannot clone a repository over an existing one.

## Cache build

```bash
$> git clone https://github.com/jgsogo/issue-4795.git
$> cd issue-4795
$> conan create . issue/testing
```
