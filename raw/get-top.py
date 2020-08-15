import datetime
import json
import os


def main():
    scores = []
    now = datetime.datetime.now()
    for filename in os.listdir('.'):
        if not filename.endswith('-posts.jsonl'):
            continue
        print(filename)
        with open(filename, 'r') as f:
            for line in f:
                line = json.loads(line)
                scores.append({
                    'view_count': line['view_count'],
                    'score': line['view_count'] /
                    (
                        now-datetime.datetime.strptime(line['created_at'], '%a, %d %b %Y %H:%M:%S %Z')
                    ).total_seconds(),
                    'id': line['id']
                })
    scores = sorted(scores, key=lambda x: x['score'], reverse=True)
    with open('video-high.jsonl', 'w') as f:
        f.write('\n'.join([json.dumps(d) for d in scores[:500000]]))

if __name__ == '__main__':
    main()

