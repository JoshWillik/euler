mkdir -p challenges
for i in $(seq 1 549); do
  page=$(curl -ss https://projecteuler.net/problem\=$i)
  echo $page | pup '#content h2 text{}' > $i
  echo $page | pup '#problem_content text{}' >> $i
done

python scripts/parse-scrape-result.py > challenges.json
rm -rf challenges
