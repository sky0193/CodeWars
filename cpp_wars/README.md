# Codewars training area

## Clang Format

<https://eellaup.medium.com/how-to-set-up-clang-format-in-visual-studio-code-in-a-vagrant-environment-georgiatech-gios-1935ed73efd1>

### Step 1: Install clang-format

```bash
sudo apt-get install clang-format-9
sudo apt-get install clang-format-9
```

### Step 2: Install the clang-format VS Code extension

### Step 3: Edit your VS Code settings.json file

```json

  "editor.codeActionsOnSave": {
    "source.fixAll": true
  },
  "editor.formatOnSave": true,
  "clang-format.executable": "/usr/bin/clang-format-9",
  "clang-format.style": "google",
  "clang-format.language.c.enable": true,
  "[c]": {
    "editor.defaultFormatter": "xaver.clang-format",
    "editor.wordBasedSuggestions": false,
    "editor.suggest.insertMode": "replace",
    "editor.semanticHighlighting.enabled": true
  }
```
