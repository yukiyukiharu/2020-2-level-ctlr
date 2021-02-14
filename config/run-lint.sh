echo -e '\n'
echo 'Running lint check...'

TARGET_SCORE=$(cat target_score.txt)

lint_output=$(python -m pylint scrapper.py article.py pipeline.py constants.py)
python3 config/lint_level.py --lint-output "$lint_output" --target-score "$TARGET_SCORE"
