## CI pipeline

1. Triggers on commit to fork with opened PR to main repository
1. Validates PR name - [skip-ci]
1. Runs Stage 1 script - check `requirements.txt` or add to requirements of the lab
1. **1A** Validates Stage CLI (Milestone 1)
    1. Wrong URL - exit code? message?
    1. Too big N
    1. Incorrect N
    1. Is `tmp/articles` populated?
    1. stages.txt -> 1
1. **1B** Validates raw data with proper messaging
    1. Can I open this URL?
    1. Can a title be found by the given xpath?
    1. Is a date in given format?
    1. Can a date be found by the given xpath?
    1. Does texts quantity match requested volume?
    1. Are IDs from 1 to the N without any misorders?
1. Runs Stage 2 script
1. **2A** Validates Stage 1 CLI
1. **2B** Validates processed data with proper messaging
    1. Does the `-1_raw.txt` result in `-1_processed.txt`?
    1. Does `-1_processed.txt` contain only lemmas and tags without punctuation signs?
    1. Does `-1_processed.txt` contains tags of proper format?
1. (Always) Publishes build artifacts (a.k.a. dataset) on AWS S3
1. (Optional) Puts a link to artifact to the PR

### Milestones

1. `scrapper.py` with CLI and fake files creation passing CI 1A
1. `scrapper.py` passing 1B (11 February)
1. public repository with tests for 1A/1B (11 February) - stages?
1. `pipeline.py` with CLI and fake files creation passing CI 2A
1. `pipeline.py` passing CI 2B (18 February)
1. artifacts on S3 (18 February)

## Configuring Python for course development

Instructions below are validated on macOS. For Windows setup replace `python3` with `py`.
**TBD** how to provide python path on Windows.

```
python3 -m pip install --user virtualenv
python3 -m virtualenv -p `which python3` venv
source venv/bin/activate
python -m pip install -r requirements.txt
```
