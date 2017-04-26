from subprocess import call

def downl():
    hids = ['7CA490274345','7CA489447974','7CA487852427','7CA486758507','7CA485712748','7CA485543825','7CA483715708','7CA482226795','7CA481401839','7CA480519733','7CA479741650','7CA479014395','7CA478128036','7CA477235186','7CA476622692']
    urls = []
    for hid in hids:
        for pos in range(1,21):
        # for pos in range(1,2):
            url = "http://go.galegroup.com/ps/retrieve.do?tabID=T003&resultListType=RESULT_LIST&searchResultsType=SingleTab&searchType=AdvancedSearchForm&currentPosition={}&docId=GALE%{}&docType=Article&sort=Relevance&contentSegment=&prodId=GRGM&contentSet=GALE%{}&searchId=R1&userGroupName=colomines&inPS=true".format(pos,hid,hid)
            urls.append(url)

    fids = [(i + 1,u) for i,u in enumerate(urls)]
    [call(['wget','-O','html/{}.html'.format(i),u]) for (i,u) in fids]
    with open('id_url','w') as f:
        [f.write('{},{}\n'.format(i,u)) for (i,u) in fids]
