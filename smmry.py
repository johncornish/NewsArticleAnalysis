from subprocess import call
import pycurl
import json
import glob
from io import BytesIO
from shutil import copyfile

# def downl():
#     # hids = ['7CA490274345','7CA489447974','7CA487852427','7CA486758507','7CA485712748','7CA485543825','7CA483715708','7CA482226795','7CA481401839','7CA480519733','7CA479741650','7CA479014395','7CA478128036','7CA477235186','7CA476622692']
#     # rs = range(1,23)
#     # ps = range(1,21)
#     rs = range(1,10)
#     ps = range(1,10)
#     urls = []
#     for r in rs:
#         for pos in ps:
#             url = "http://go.galegroup.com/ps/retrieve.do?tabID=T003&resultListType=RESULT_LIST&searchResultsType=SingleTab&searchType=AdvancedSearchForm&currentPosition={}&docId=GALE%7CA490274345&docType=Article&sort=Relevance&contentSegment=&prodId=GRGM&contentSet=GALE%7CA490274345&searchId=R{}&userGroupName=colomines&inPS=true".format(pos,r)
#             urls.append(url)
#
#     fids = [(i + 1,u) for i,u in enumerate(urls)]
#     [call(['wget','-q','-O','html/{}.html'.format(i),u]) for (i,u) in fids]

def downl_url_list():
    with open('article_urls') as f:
        fids = [(i + 1,l) for i, l in enumerate(f)]
        [call(['wget','-q','-O','html/{}.html'.format(i),u]) for (i,u) in fids]
        with open('id_url','w') as f:
            [f.write('{},{}'.format(i,u)) for (i,u) in fids]

def sum_arts():
    for pth in glob.glob('text/*'):
        fname = pth.split('/')[-1]

        with open(pth) as f:
            txt = f.read()

            data = BytesIO()

            c = pycurl.Curl()
            c.setopt(c.URL, 'http://api.smmry.com/&SM_API_KEY=A7A20F6483&SM_LENGTH=10&SM_WITH_BREAK')

            c.setopt(c.HTTPHEADER, ["Expect:"]);
            c.setopt(c.POST, True);
            c.setopt(c.POSTFIELDS, "sm_api_input={}".format(txt.replace(u'\xa0',' ')));
            c.setopt(c.FOLLOWLOCATION, True);
            c.setopt(c.CONNECTTIMEOUT, 20);
            c.setopt(c.TIMEOUT, 20);
            c.setopt(c.WRITEFUNCTION, data.write)

            c.perform()

            r = json.loads(data.getvalue().decode('ascii'))

            print(str(r))
            with open('summaries/{}'.format(fname),'w') as sm:
                if 'sm_api_content' in r:
                    sm.write(r['sm_api_content'].replace('[BREAK]','\n'))

            c.close()

sum_arts()
