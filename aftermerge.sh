current_branch=$(git rev-parse --abbrev-ref HEAD)

git checkout main
git pull origin
git branch -d $current_branch