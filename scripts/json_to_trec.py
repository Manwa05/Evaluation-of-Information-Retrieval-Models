# -*- coding: utf-8 -*-


import json
# if you are using python 3, you should 
import urllib.request
import urllib.parse
#import urllib2

# change the url according to your own corename and query
inurl = "http://18.218.122.49:8983/solr/IRBM25/select?q=%3A{}%20&fl=id%2Cscore&wt=json&indent=true&rows=20"


# change query id and IRModel name accordingly
qid = ''
IRModel='BM25Model'
#outf = open(outfn, 'a+', encoding='utf-8')

# get all queries
with open('test_queries.txt', encoding='utf-8') as qfile:
    q = qfile.readline()
    while q:
        q = q.strip().replace(" ", "*", 1)
        query_str = q.split('*')
        qid = query_str[0]
        outfn = 'BM25'+qid+'.txt'
        outf = open(outfn, 'a+', encoding='utf-8')
        query = query_str[1]
        query = urllib.parse.quote(query)
        cur_url = inurl.format(query,query,query)
        #print(cur_url)
        
        # data = urllib2.urlopen(inurl)
        # if you're using python 3, you should use
        try:
            data = urllib.request.urlopen(cur_url)
        except:
            #print("An exception occurred for Query: " + qid)
            continue

        docs = json.load(data)['response']['docs']
        # the ranking should start from 1 and increase
        rank = 1
        for doc in docs:
            outf.write(qid + ' ' + 'Q0' + ' ' + str(doc['id']) + ' ' + str(rank) + ' ' + str(doc['score']) + ' ' + IRModel + '\n')
            rank += 1
        q = qfile.readline()
        outf.close()
qfile.close()

