import os
import json
import base64

os.chdir('workDIR/')
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'GTT/gcloud_token.json'
text_file = 'GTT/text.txt'
json_file = 'GTT/request.json'

with open(json_file, 'r', encoding='utf8') as fp:
    data = json.load(fp)
    print(data)
fp.close()

f = open(text_file, 'r')  
lines = f.readlines()
i = 1
for line in lines:
    line = line.strip('\n')
    if line == '':
        continue
    data['input']['text'] = line
    with open('GTT/myrequest.json', 'w', encoding='utf8') as fp:
        json.dump(data, fp)
    fp.close()

    process = os.popen('curl -X POST \
    -H "Authorization: Bearer "$(gcloud auth application-default print-access-token) \
    -H "Content-Type: application/json; charset=utf-8" \
    -d @GTT/myrequest.json \
    https://texttospeech.googleapis.com/v1/text:synthesize') # return file
    res = process.read()
    process.close() 
    # print(res)
    json_data = json.loads(res)

    # process responding data
    mp3_file = 'GTT/voice_%s.mp3' % i

    mp3 =  base64.b64decode(json_data['audioContent'])
    fout = open(mp3_file, 'wb')
    fout.write(mp3)
    fout.close()
    print('Finished voice_%s!' % i)
    i += 1

print('\nEnjoy your voice!')