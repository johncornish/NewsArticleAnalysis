from subprocess import call
import pycurl
import json
import glob
from io import BytesIO
from shutil import copyfile

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
